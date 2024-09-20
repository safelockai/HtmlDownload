#!/data/data/com.termux/files/usr/bin/bash

# Atualiza os repositórios
pkg update && pkg upgrade -y

# Instala o Python
pkg install python -y

# Verifica se o pip está instalado e instala se necessário
if ! command -v pip &> /dev/null
then
    echo "Instalando pip..."
    pkg install python-pip -y
fi

# Instala o Flask
pip install flask

# Instala um editor de texto
pkg install nano -y  # ou pkg install vim -y, se preferir vim

# Configura permissões de armazenamento, se necessário
termux-setup-storage

echo "Todas as ferramentas necessárias foram instaladas!"
