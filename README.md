<!--
*** Modelo de README: Best-README-Template.
*** https://github.com/othneildrew/Best-README-Template
-->
<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![MIT License][license-shield]][license-url]

</br>
<div align="center">
  <h3>Gerador-Assinatura-Email</h3>
</div>

Este projeto Flask simples gera imagens de assinatura personalizadas a partir de um modelo HTML, usando dados fornecidos por meio de parâmetros de consulta em uma solicitação GET.

O aplicativo irá gerar uma imagem PNG da assinatura com os dados fornecidos e baixá-la automaticamente.



<!-- TABLE OF CONTENTS -->
## Conteúdo
<details>
  <summary>Expandir</summary>

- [Conteúdo](#conteúdo)
- [Construído com](#construído-com)
- [Como usar](#como-usar)
      - [Exemplos](#exemplos)
- [Personalização](#personalização)
      - [Exemplos](#exemplos-1)
- [Dependências](#dependências)
- [Pré Requisitos](#pré-requisitos)
- [Como contribuir](#como-contribuir)
- [Direitos Autorais](#direitos-autorais)
</details>


## Construído com
[![Python][python]][Python-url] [![flask][flask]][flask-url] [![imgkit][imgkit]][imgkit-url] [![jinja2][jinja2]][jinja2-url]


<!-- GETTING STARTED -->
## Como usar

1. **Executar** `flask run`

1. **Enviar solicitação GET** na URL http://127.0.0.1:5000/gerarAssinatura, passando os seguintes parâmetros:
 * nome
 * cargo
 * telefone (opcional)
 * skype (opcional)

##### Exemplos
    http://127.0.0.1:5000/gerarAssinatura?nome=João%20Neto&cargo=Gerente%20de%20Projetos&telefone=+55%20(11)%2099999-9999&skype=joaoneto

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Personalização
Edite o arquivo _assinatura.html_ para personalizar o modelo da assinatura. Use a sintaxe do Jinja2 para determinar como os dados serão exibidos.

##### Exemplos
Variável: `{{ telefone }}`
Condicional: `{% if telefone %}` | `{% else %}` | `{% endif %}`

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Dependências
Este projeto utiliza basicamente estes dois pacotes, com as suas respectivas dependências:
* flask
* imgkit

Para instalá-las, use o comando:
```console
pip install -r requirements.txt
```

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Pré Requisitos
Certifique-se de ter o _wkhtmltopdf_ instalado em seu sistema para que o imgkit funcione corretamente.
```console
dnf install wkhtmltopdf
```

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>


<!-- CONTRIBUTING -->
## Como contribuir
Gostou do projeto e tem ideias para deixá-lo ainda melhor? Fique a vontade para fazer um fork e criar um pull request!
Não se esqueça de dar uma estrela ao projeto!

1. Faça o Fork do Project
2. Crie uma branch nova (`git checkout -b feature/AmazingFeature`)
3. Commit suas alterações (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

<!--

### Top contributors

<a href="https://github.com/antoniocarelli/GeraAssinatura/graphs/contributors">
  <img src="https://contrib.rocks/preview?repo=antoniocarelli%2FGeraAssinatura"/>
</a>

-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## Direitos Autorais

Este projeto utiliza o modelo de licenciamento do MIT.

[![MIT License][license-shield]][license-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- BADGES -->
<!-- https://shields.io -->
[contributors-shield]: https://img.shields.io/github/contributors/antoniocarelli/GeraAssinatura?style=for-the-badge
[contributors-url]: https://github.com/antoniocarelli/GeraAssinatura/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/antoniocarelli/GeraAssinatura?style=for-the-badge
[forks-url]: https://github.com/antoniocarelli/GeraAssinatura/network/members

[stars-shield]: https://img.shields.io/github/stars/antoniocarelli/GeraAssinatura?style=for-the-badge
[stars-url]: https://github.com/antoniocarelli/GeraAssinatura/stargazers

[python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://pypi.org/project/Flask/

[imgkit]: https://img.shields.io/badge/Imgkit-800000?style=for-the-badge&logo=imgkit&logoColor=white
[imgkit-url]: https://pypi.org/project/imgkit/

[jinja2]: https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white
[jinja2-url]: https://jinja.palletsprojects.com/en/stable/

[MIT]: https://img.shields.io/badge/opensource-B41717?style=for-the-badge&logo=opensource&logoColor=white
[MIT-url]: https://opensource.org/license/mit

[license-shield]: https://img.shields.io/github/license/antoniocarelli/GeraAssinatura?style=for-the-badge
[license-url]: https://github.com/antoniocarelli/GeraAssinatura/blob/master/LICENSE.txt