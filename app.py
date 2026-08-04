from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import urllib.request
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(500), nullable=False)
    songs = db.relationship('Song', backref='band', lazy=True)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    album_cover = db.Column(db.String(500), nullable=False) 
    audio_url = db.Column(db.String(500), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    played_at = db.Column(db.DateTime, default=datetime.utcnow)
    song = db.relationship('Song', backref='plays')

@app.route('/')
def index():
    artists = Artist.query.all()
    return render_template('index.html', artists=artists)

@app.route('/artist/<int:id>')
def artist_page(id):
    artist = Artist.query.get_or_404(id)
    return render_template('artist.html', artist=artist)

@app.route('/history')
def history():
    played_songs = History.query.order_by(History.played_at.desc()).limit(30).all()
    return render_template('history.html', played_songs=played_songs)

@app.route('/record_play/<int:song_id>', methods=['POST'])
def record_play(song_id):
    new_play = History(song_id=song_id)
    db.session.add(new_play)
    db.session.commit()
    return jsonify({"status": "success"})

@app.route('/sync', methods=['GET', 'POST'])
def sync_repo():
    message = None
    if request.method == 'POST':
        repo_url = request.form.get('repo_url')
        artist_name = request.form.get('artist_name')
        artist_image = request.form.get('artist_image') or "https://images.suamusica.com.br/sJlnrXsIB8PWWeyaVZf4o8kRQIU=/240x240/filters:format(webp)/27944531/4423516/cd_cover.jpeg"
        
        try:
            clean_url = repo_url.strip().rstrip('/')
            parts = clean_url.split('/')
            if len(parts) < 2:
                raise ValueError("Link do repositório inválido.")
            
            repo = parts[-1]
            owner = parts[-2]
            
            api_url = f"https://api.github.com/repos/{owner}/{repo}/releases"
            req = urllib.request.Request(api_url, headers={'User-Agent': 'PyMusic-App'})
            
            with urllib.request.urlopen(req) as response:
                releases = json.loads(response.read().decode())
                
            artist = Artist.query.filter_by(name=artist_name).first()
            if not artist:
                artist = Artist(name=artist_name, bio=f"Banda sincronizada automaticamente do repositório {repo}.", image=artist_image)
                db.session.add(artist)
                db.session.commit()
                
            added_count = 0
            for release in releases:
                for asset in release.get('assets', []):
                    name = asset.get('name', '')
                    download_url = asset.get('browser_download_url', '')
                    
                    if name.lower().endswith('.mp3'):
                        clean_title = name[:-4].replace('.', ' ').replace('_', ' ')
                        
                        existing = Song.query.filter_by(audio_url=download_url).first()
                        if not existing:
                            new_song = Song(
                                title=clean_title,
                                album_cover=artist.image,
                                audio_url=download_url,
                                artist_id=artist.id
                            )
                            db.session.add(new_song)
                            added_count += 1
                            
            db.session.commit()
            message = f"Sucesso! {added_count} nova(s) música(s) sincronizada(s) para o artista {artist_name}!"
        except Exception as e:
            message = f"Erro ao sincronizar: {str(e)}"
            
    return render_template('sync.html', message=message)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        capa_queen = "https://images.suamusica.com.br/sJlnrXsIB8PWWeyaVZf4o8kRQIU=/240x240/filters:format(webp)/27944531/4423516/cd_cover.jpeg"
        capa_acdc = "https://images.suamusica.com.br/AIIkrhnECFveyy_WIZtl1DtTVsA=/240x240/filters:format(webp)/35716229/4398173/cd_cover.png"
        
        queen = Artist(name="Queen", bio="Formada em Londres em 1970...", image=capa_queen)
        acdc = Artist(name="AC/DC", bio="Formada em Sydney, Austrália...", image=capa_acdc)
        db.session.add(queen)
        db.session.add(acdc)
        db.session.commit()
        
        sample_songs = [
            Song(title="Love of My Life", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/Love.of.My.Life.mp3", artist_id=queen.id),
            Song(title="Back In Black", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Back.In.Black.mp3", artist_id=acdc.id)
        ]
        db.session.bulk_save_objects(sample_songs)
        db.session.commit()
            
    app.run(host='0.0.0.0', port=5000, debug=True)