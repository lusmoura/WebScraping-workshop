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
python3 install -r requirements.txt
```

## O projeto

O projeto tem uma ideia bem direta: descobrir quais palavras os artistas mais utilizam em suas músicas. Para isso vamos *scrapar* o site [https://www.letras.mus.br/](https://www.letras.mus.br/), buscando todas as músicas de um dado artista.

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

[Passo a passo para fazer scraping](https://ibb.co/vz6HLVY)
