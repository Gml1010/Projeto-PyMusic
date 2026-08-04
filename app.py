from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
    played_at = db.Column(db.DateTime, default=datetime.utcnow) # Salva a hora exata
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

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        capa_queen = "https://images.suamusica.com.br/sJlnrXsIB8PWWeyaVZf4o8kRQIU=/240x240/filters:format(webp)/27944531/4423516/cd_cover.jpeg"
        capa_acdc = "https://images.suamusica.com.br/AIIkrhnECFveyy_WIZtl1DtTVsA=/240x240/filters:format(webp)/35716229/4398173/cd_cover.png"
        
        queen = Artist(name="Queen", bio="Formada em Londres em 1970, o Queen é uma das maiores bandas de rock da história...", image=capa_queen)
        acdc = Artist(name="AC/DC", bio="Formada em Sydney, Austrália, em 1973, pelos irmãos Angus e Malcolm Young...", image=capa_acdc)
        
        db.session.add(queen)
        db.session.add(acdc)
        db.session.commit()
        
        sample_songs = [
            Song(title="Love of My Life", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/Love.of.My.Life.mp3", artist_id=queen.id),
            Song(title="Radio Ga Ga", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/Radio.Ga.Ga.mp3", artist_id=queen.id),
            Song(title="Somebody To Love", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/Somebody.To.Love.mp3", artist_id=queen.id),
            Song(title="Under Pressure", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/Under.Pressure.mp3", artist_id=queen.id),
            Song(title="We Are The Champions", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/We.Are.The.Champions.mp3", artist_id=queen.id),
            Song(title="We Will Rock You", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/We.Will.Rock.You.mp3", artist_id=queen.id),
            Song(title="Another One Bites The Dust", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/Another.One.Bites.The.Dust.mp3", artist_id=queen.id),
            Song(title="Bohemian Rhapsody", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/Bohemian.Rhapsody.mp3", artist_id=queen.id),
            Song(title="Don't Stop Me Now", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/Dont.Stop.Me.Now.mp3", artist_id=queen.id),
            Song(title="Forever", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/For.ever.mp3", artist_id=queen.id),
            Song(title="I Want To Break Free", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/I.Want.To.Break.Free.mp3", artist_id=queen.id),
            Song(title="I Was Born To Love You", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/I.Was.Born.To.Love.You.mp3", artist_id=queen.id),
            Song(title="Killer Queen", album_cover=capa_queen, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/Add/Killer.Queen.mp3", artist_id=queen.id),
            
            Song(title="Are You Ready", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Are.You.Ready.mp3", artist_id=acdc.id),
            Song(title="Back In Black", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Back.In.Black.mp3", artist_id=acdc.id),
            Song(title="Beating Around the Bush", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Beating.Around.the.Bush.mp3", artist_id=acdc.id),
            Song(title="Black Ice", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Black.Ice.mp3", artist_id=acdc.id),
            Song(title="Demon Fire", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Demon.Fire.mp3", artist_id=acdc.id),
            Song(title="Fire Your Guns", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Fire.Your.Guns.mp3", artist_id=acdc.id),
            Song(title="Get It Hot", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Get.It.Hot.mp3", artist_id=acdc.id),
            Song(title="Girls Got Rhythm", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Girls.Got.Rhythm.mp3", artist_id=acdc.id),
            Song(title="Hells Bells", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Hells.Bells.mp3", artist_id=acdc.id),
            Song(title="High Voltage", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/High.Voltage.mp3", artist_id=acdc.id),
            Song(title="Highway to Hell", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Highway.to.Hell.mp3", artist_id=acdc.id),
            Song(title="If You Want Blood You've Got It", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/If.You.Want.Blood.You.ve.Got.It.mp3", artist_id=acdc.id),
            Song(title="Love Hungry Man", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Love.Hungry.Man.mp3", artist_id=acdc.id),
            Song(title="Night Prowler", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Night.Prowler.mp3", artist_id=acdc.id),
            Song(title="Rock N Roll Train", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Rock.N.Roll.Train.mp3", artist_id=acdc.id),
            Song(title="Shot Down In Flames", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Shot.Down.In.Flames.mp3", artist_id=acdc.id),
            Song(title="T.N.T.", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/T.N.T.mp3", artist_id=acdc.id),
            Song(title="Thunderstruck", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Thunderstruck.mp3", artist_id=acdc.id),
            Song(title="Touch Too Much", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Touch.Too.Much.mp3", artist_id=acdc.id),
            Song(title="Walk All Over You", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/Walk.All.Over.You.mp3", artist_id=acdc.id),
            Song(title="War Machine", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/War.Machine.mp3", artist_id=acdc.id),
            Song(title="You Shook Me All Night Long", album_cover=capa_acdc, audio_url="https://github.com/Gml1010/musicas-pymusic/releases/download/ad/You.Shook.Me.All.Night.Long.mp3", artist_id=acdc.id)
        ]
        
        db.session.bulk_save_objects(sample_songs)
        db.session.commit()
            
    app.run(host='0.0.0.0', port=5000, debug=True)