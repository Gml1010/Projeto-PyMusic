<div align="center">
  <!-- Você pode trocar este link pela URL da sua própria logo depois -->
  <img src="https://dummyimage.com/150x150/1a1a1a/28a745.png&text=PyMusic" alt="Logo PyMusic" style="border-radius: 20px;">
  
  <h1>🎵 PyMusic</h1>
  
  <p><em>Sua plataforma pessoal de streaming de música construída com Python e Flask!</em></p>
</div>

<hr>

## 📖 Sobre o Projeto

O **PyMusic** é uma aplicação web leve e responsiva de streaming de música. Ele organiza seus artistas favoritos, mantém um histórico detalhado das faixas reproduzidas e inclui um player de áudio integrado que toca músicas (arquivos `.mp3`) hospedadas diretamente de forma gratuita.

## ✨ Funcionalidades

<ul>
  <li><strong>Página de Artistas:</strong> Navegue pelas suas bandas favoritas (como Queen e AC/DC) com biografias e capas personalizadas.</li>
  <li><strong>Player Interno Dinâmico:</strong> Um player fixo no rodapé construído com JavaScript que permite tocar músicas perfeitamente.</li>
  <li><strong>Histórico de Reprodução:</strong> Registro automático de data e hora (em tempo real) de todas as faixas que você ouviu no servidor.</li>
  <li><strong>Hospedagem Inteligente:</strong> Otimizado para usar o <em>GitHub Releases</em> como um servidor gratuito para os arquivos de áudio.</li>
</ul>

## 🛠️ Tecnologias Utilizadas

<ul>
  <li><strong>Backend:</strong> Python, Flask, Flask-SQLAlchemy</li>
  <li><strong>Banco de Dados:</strong> SQLite (com geração automática do arquivo <code>music.db</code>)</li>
  <li><strong>Frontend:</strong> HTML5, CSS3, Bootstrap 5, JavaScript Vanilla</li>
  <li><strong>Gerenciamento de Pacotes:</strong> uv</li>
</ul>

<h2>🚀 Como Instalar e Rodar Localmente</h2>

<p>Siga o passo a passo abaixo para rodar o PyMusic na sua máquina:</p>

<h3>1. Clone o repositório</h3>
<p>Abra o seu terminal e clone o projeto:</p>
<pre><code class="language-bash">git clone https://github.com/Gml1010/musicas-pymusic.git
cd musicas-pymusic
</code></pre>

# Configure o ambiente virtual e instale as dependências
<p>Utilize o <code>uv</code> para configurar o ambiente e instalar os pacotes necessários:</p>
<pre><code class="language-bash"># Cria o ambiente virtual isolado
uv venv

# Instala o Flask e o SQLAlchemy no ambiente
uv pip install Flask Flask-SQLAlchemy
</code></pre>

# Ative o ambiente virtual
<p>Escolha o comando correspondente ao seu sistema operacional:</p>
<pre><code class="language-bash"># Se estiver no Windows:
.venv\Scripts\activate

# Se estiver no Linux/Mac:
source .venv/bin/activate
</code></pre>

<h3>4. Inicie a aplicação</h3>
<p>Execute o script principal para criar o banco de dados e iniciar o servidor:</p>
<pre><code class="language-bash">python app.py
</code></pre>

<p>Pronto! Agora basta abrir o seu navegador e acessar: <a href="http://localhost:5000" target="_blank">http://localhost:5000</a></p>
