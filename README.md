## O que é WebScraping?

Extrair informações da internet de forma automatizada. Existem diversas maneiras de fazer isso, nesse tutorial vamos ver algumas delas, por meio de bibliotecas de python.

## Porque é útil?

- Automatizar processos
- Gerar Leads
- Acompanhar produtos
- Fazer projetos!!!

## É legal?

Bom, é legal, mas nem sempre é legal. Em geral, criar *web scrapers* é muito divertido, mas nem sempre é uma coisa legalizada. Por isso é importante ficar atento aos termos de uso dos sites. O linkedin, por exemplo, não permite que sejam utilizados *scrapers* em nenhuma situação.

## Quais as ferramentas utilizadas nesse tutorial?

Todos os códigos são feitos em Python 3. Além disso, são utilizadas algumas bibliotecas, as principais são:

- [requests](https://pypi.org/project/requests/)
- [requests-html](https://pypi.org/project/requests-html/)
- [selenium](https://pypi.org/project/selenium/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [Lxml](https://pypi.org/project/lxml/)

Outras bibliotecas são utilizadas de apoio, e para instalar tudo, basta utilizar o arquivo [requirements.txt](https://github.com/lusmoura/WebScraping-workshop/blob/main/requirements.txt) presente nesse repositório por meio do comando:

```python
pip3 install -r requirements.txt
```

## O projeto

O projeto tem uma ideia bem direta: descobrir quais palavras os artistas mais utilizam em suas músicas. Para isso vamos *scrapar* o site [letras.mus](https://www.letras.mus.br/), buscando todas as músicas de um dado artista.

### Versão 1
Nessa [versão do projeto](https://github.com/lusmoura/WebScraping-workshop/blob/main/requests_letras.py), pegamos as letras do [letras.mus](https://www.letras.mus.br/) e contamos a palavras. 

### Versão 2
A [segunda versão](https://github.com/lusmoura/WebScraping-workshop/blob/main/requests_html_lastfm.py) do projeto envolve pegar os artistas mais relevantes do [lastfm](https://www.last.fm) e, para cada um desses artistas, fazer a contagem das palavras. Nessa versão usamos requests-html para renderizar a página.

### Versão 3
Na terceira [versão do projeto](https://github.com/lusmoura/WebScraping-workshop/blob/main/requests_endpoint_lastfm.py), fazemos o mesmo que na versão 2, porém dessa vez é feita a requisição direto em um *endpoint* com a biblioteca requests.

### Versão 4
A [última versão](https://github.com/lusmoura/WebScraping-workshop/blob/main/selenium_spotify.py) do projeto envolve buscar a quantidade de ouvintes mensais dos artistas no [spotify](https://open.spotify.com/). Para isso usamos selenium.

## Sobre as ferramentas

### Requests

- Biblioteca para fazer requisições web.
- Pode ser utilizada para *get*, *post*, *delete*...
- Precisa de outra biblioteca para fazer parsing do html.

### Lxml

- Biblioteca para fazer parsing do html.
- Útil pois permite busca por *xpath* de forma nativa.
- Minha queridinha s2

### BeautifulSoup

- Biblioteca para fazer parsing do html.
- Tem muita documentação e perguntas na internet (alo *stackoverflow*)
- É bem flexível, permite o uso de diversos *parsers,* mas não tem *xpath* =(

### Requests-html

- Em muitos casos só a requisição não basta. É preciso também renderizar o javascript da página. A biblioteca *requests* não tem essa funcionalidade.
- A requests-html pode ser usada da mesma maneira que a requests, mas possui essa nova funcionalidade de renderização.
- Precisa de outra biblioteca para fazer parsing do html (pode usar qualquer uma das duas citadas acima).

### Selenium

- Selenium é uma ferramenta de automatização de *software* e é muito utilizada para realização de testes. MAS é super útil para scraping também.
- Como o *software* simula um navegador, muitas vezes "engana" melhor os antibots. Além disso, renderiza o javascript normalmente, então serve para esses casos também.
- Na maioria das vezes, usar selenium é matar uma barata com um canhão, mas em alguns momentos pode ser útil.
- **Truque:** se nada que você fizer funcionar naquele site, tenta usar o selenium e fazer requisições para outros sites com aquele *driver*. Isso vai gerar cookies no navegador e vai ser mais fácil se passar por um usuário comum.

### Truque endpoint

- Um dos melhores truques de *scraping* é buscar *enpoints* na aba de *network* do navegador.
- Isso permite fazer uma requisição direta sem precisar fazer *parsing* de html, o que facilita nossa vida e ainda é mais rápido.
- É o jeito mais fácil de codar, mas as vezes exige paciência para encontrar o *endpoint* certo.
- Para o código basta:
    1. Clicar em network 
    2. Encontrar endpoint
    3. Clicar com botão direito
    4. Clicar em "Copiar como Curl" 
    5. Ir para [esse site](https://curl.trillworks.com/) 
    6. Copiar resultado como requests
    7. Ta pronto o sorvetinho

### Passo a passo que >eu< uso

<img src="https://i.ibb.co/q13dm75/Screenshot-from-2021-06-17-14-09-50.png">

## Onde aprender mais?

Existem muuuuitos sites com tutoriais por aí, mas eu gosto bastante de usar o Medium para aprender esse tipo de coisa. Algumas sugestões de texto são:
- [Data Science Skills: Web scraping using python](https://towardsdatascience.com/data-science-skills-web-scraping-using-python-d1a85ef607ed)
- [Learn Web Scraping using Python in under 5 minutes](https://medium.com/@kaustumbhjaiswal7/learn-web-scraping-using-python-in-under-5-minutes-36a7d4d6e1e7)
- [Como fazer Web Scraping em Python](https://medium.com/data-hackers/como-fazer-web-scraping-em-python-23c9d465a37f)

Além disso, também tem [esse projeto](https://www.coursera.org/projects/web-scraping) guiado no Coursera que é bem legal.

No mais, pega alguns sites e vai tentando. Se der errado, pesquisa no StackOverflow e tenta entender o que rolou, isso é um processo importante também! 

E uma última dica, tem muuuitos sites diferentes por ai, cada um com sua própria peculiaridade. Não dá para aprender TUDO de scraping sem ir treinando, então recomendo aprender o básico e depois ir pesquisando sob demanda as coisas mais complexas =D

## Último aviso

Vocês tem meus contatos, então podem ficar a vontade pra mandar mensagem/email sempre que precisarem =D
