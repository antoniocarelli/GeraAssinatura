from flask import Flask, render_template_string, request, send_file
import imgkit

app = Flask(__name__)

# Ler o arquivo HTML (agora um template Jinja2)
with open('assinatura.html', 'r') as f:
    template = f.read()

@app.route('/gerarAssinatura', methods=['GET'])
def webhook():
    dados = request.args.to_dict()

    # Obter nome do parâmetro 'nome' ou usar 'assinatura' como padrão
    nome_arquivo = dados.get('nome', 'assinatura')
    nome_arquivo = nome_arquivo.replace(" ", "_")
    nome_arquivo += '.png'

    # Renderizar o template Jinja2 com os dados
    html_final = render_template_string(template, **dados)

    # Converter html_final para PNG
    options = {
        'transparent': '',
        'width': 718
    }
    imgkit.from_string(html_final, nome_arquivo, options=options)

    # Retornar o arquivo como resposta
    return send_file(nome_arquivo, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
