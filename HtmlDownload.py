from flask import Flask, send_file, render_template_string

app = Flask(__name__)

# Pergunta o caminho do arquivo que deseja baixar
file_path = input("Digite o caminho do arquivo que será baixado: ")

# Pergunta o caminho do HTML existente
html_path = input("Digite o caminho do arquivo HTML que será modificado: ")

# Carrega o HTML existente
with open(html_path, 'r') as file:
    original_html = file.read()

# Modifica o HTML para incluir um script que faz o download automaticamente
modified_html = original_html.replace('</head>', '''
    <script>
        window.onload = function() {
            window.location.href = '/download';
        };
    </script>
</head>
''')

@app.route('/')
def home():
    return render_template_string(modified_html)

@app.route('/download')
def download_file():
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
