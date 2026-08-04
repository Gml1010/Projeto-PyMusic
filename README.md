<div align="center">
  <!-- Você pode trocar este link pela URL da sua própria logo depois -->
  <img src="https://dummyimage.com/150x150/1a1a1a/28a745.png&text=PyMusic" alt="Logo PyMusic" style="border-radius: 20px;">
  
  <h1>🎵 PyMusic</h1>
  
  <p><em>Plataforma pessoal de streaming de música construída com Python e Flask</em></p>
</div>

<hr>

## 📖 Sobre o Projeto

O **PyMusic** é uma aplicação web leve que é executada diretamente na sua máquina. Ele organiza seus artistas favoritos, mantém um histórico detalhado das faixas reproduzidas e inclui um player de áudio integrado que toca músicas (arquivos `.mp3`) hospedadas diretamente de forma gratuita.

## ✨ Funcionalidades

<ul>
  <li><strong>Página de Artistas:</strong> Navegue pelas suas músicas de forma fácil.</li>
  <li><strong>Player Interno Dinâmico:</strong> Um player fixo no rodapé.</li>
  <li><strong>Histórico de Reprodução:</strong> Registro de data e hora de todas as faixas que você ouviu.</li>
  <li><strong>Hospedagem feita por você:</strong> Otimizado para usar o <em>Repositório do GitHub</em> como um servidor gratuito para os arquivos de áudio.</li>
</ul>

## 🛠️ Tecnologias Utilizadas

<ul>
  <li><strong>Backend:</strong> Python, Flask, Flask-SQLAlchemy e API pública do GitHub</li>
  <li><strong>Banco de Dados:</strong> SQLite (com geração automática do arquivo <code>music.db</code>)</li>
  <li><strong>Frontend:</strong> HTML5, CSS3, Bootstrap 5, JavaScript Vanilla</li>
  <li><strong>Gerenciamento de Pacotes:</strong> uv</li>
</ul>

## 🚀 Como Instalar e Rodar Localmente

<p>Siga o passo a passo abaixo para rodar o PyMusic localmente:</p>

### 1. Clone o repositório
<p>Abra o seu terminal e clone o projeto:</p>
<pre><code class="language-bash">git clone https://github.com/Gml1010/musicas-pymusic.git
cd musicas-pymusic
</code></pre>

### 2. Configure o ambiente virtual e instale as dependências
<p>Utilize o <code>uv</code> para configurar o ambiente e instalar os pacotes necessários:</p>
<pre><code class="language-bash"># Cria o ambiente virtual isolado
uv venv

# Instala o Flask e o SQLAlchemy no ambiente
uv pip install Flask Flask-SQLAlchemy
</code></pre>

### 3. Ative o ambiente virtual
<p>Escolha o comando correspondente ao seu sistema operacional:</p>
<pre><code class="language-bash"># Se estiver no Windows:
.venv\Scripts\activate

# Se estiver no Linux/Mac:
source .venv/bin/activate
</code></pre>

### 4. Inicie a aplicação
<p>Execute o script principal para criar o banco de dados e iniciar o servidor:</p>
<pre><code class="language-bash">python app.py
</code></pre>

<p>Pronto! Agora basta abrir o seu navegador e acessar: <a href="http://localhost:5000" target="_blank">http://localhost:5000</a></p>

<hr>

## 🔄 Teste do Sync

<p>Para testar a sincronização com os repositórios do GitHub, siga os passos:</p>

<ol>
  <li>Vá na opção de sincronizar repositório.</li>
  <li>Utilize o repositório de teste abaixo:</li>
</ol>

<ul>
  <li><strong>Em "Link do Repositório do GitHub" cole:</strong><br>
    <code>https://github.com/Gml1010/Teste-sync</code>
  </li>
  <li><strong>Em "Nome do Artista / Banda" cole:</strong><br>
    <code>Michael-Jackson</code>
  </li>
  <li><strong>Em "Link da Foto de Capa (Opcional)" cole:</strong><br>
    <code>https://images.suamusica.com.br/P-PS32976whGM4gT-K_UeJ69CII=/240x240/filters:format(webp)/47004357/4350830/cd_cover.jpg</code>
  </li>
</ul>
