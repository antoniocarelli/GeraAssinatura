from flask import Flask, render_template_string, request
import imgkit

app = Flask(__name__)

# Ler o arquivo HTML (agora um template Jinja2)
with open('assinatura.html', 'r') as f:
  template = f.read()

@app.route('/gerarAssinatura', methods=['GET'])
def webhook():
  dados = request.args.to_dict()

  # Renderizar o template Jinja2 com os dados
  html_final = render_template_string(template, **dados)
  
  # Converter html_final para PNG
  imgkit.from_string(html_final, 'assinatura.png')


  return 'Arquivo salvo com sucesso!'

if __name__ == '__main__':
  app.run(debug=True)
