# Conversor de Moedas

Este projeto é um conversor de moedas desenvolvido em Python com o objetivo de praticar alguns conceitos que venho aprendendo durante meus estudos, principalmente o consumo de APIs, validação de dados e organização do código em diferentes módulos.

Para obter as cotações e as moedas disponíveis, o projeto utiliza a API Frankfurter.

## Funcionalidades

O programa possui um menu com três operações principais:

* Converter um valor de uma moeda para outra.
* Converter um mesmo valor para várias moedas de destino.
* Consultar a cotação entre duas moedas sem realizar uma conversão.

As moedas disponíveis são buscadas diretamente na API, então não é necessário manter uma lista fixa de moedas no código.

O programa também possui algumas validações para evitar entradas inválidas, como moedas inexistentes, valores menores ou iguais a zero e opções inválidas no menu.

Além disso, foram adicionados tratamentos para alguns problemas que podem ocorrer durante as requisições à API, como erros de conexão, timeout, erros HTTP e respostas que não estejam em um formato JSON válido.

## Estrutura do projeto

```text
Conversor_Moedas/
│
├── main.py
├── api.py
├── validacoes.py
├── utilidades.py
├── requirements.txt
├── .gitignore
└── README.md
```

### main.py

É onde fica o fluxo principal do programa e o menu de opções.

### api.py

Contém as funções relacionadas às operações do conversor e à consulta dos dados necessários na API.

### validacoes.py

Responsável pelas entradas do usuário, validações e pelas requisições realizadas com a biblioteca `requests`.

### utilidades.py

Possui pequenas funções auxiliares utilizadas pelo restante do projeto.

### requirements.txt

Contém as dependências utilizadas pelo projeto.

### .gitignore

Define arquivos e pastas que não devem ser enviados para o repositório, como o ambiente virtual e arquivos gerados pelo Python.

## API utilizada

O projeto utiliza a API Frankfurter:

https://api.frankfurter.dev/

São utilizados dois endpoints:

* `/v2/currencies` para obter as moedas disponíveis.
* `/v2/rates` para consultar as taxas de câmbio.

As moedas são identificadas através de seus códigos ISO, como `BRL`, `USD` e `EUR`.

## Como executar

Primeiro, clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta do projeto:

```bash
cd Conversor_Moedas
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

No Windows PowerShell, ative o ambiente virtual:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Depois, execute o programa:

```bash
python main.py
```

## Exemplo

Ao iniciar o programa, o menu apresentado é:

```text
MENU DE CONVERSÕES
1 - CONVERTER MOEDA ÚNICA
2 - CONVERTER MOEDAS
3 - BUSCAR COTAÇÃO
4 - SAIR
OPÇÃO:
```

Na conversão de uma moeda, o programa solicita a moeda base, a moeda de destino e o valor que será convertido.

Por exemplo:

```text
Informe a moeda base: BRL
Informe a moeda destino: USD
Valor em BRL: 100
```

Depois disso, a aplicação consulta a API, obtém a cotação e apresenta o resultado da conversão.

## O que pratiquei neste projeto

Este projeto foi desenvolvido principalmente como exercício de aprendizado. Durante seu desenvolvimento, pratiquei:

* Consumo de APIs;
* Requisições HTTP com `requests`;
* Manipulação de dados retornados em JSON;
* Funções e separação de responsabilidades;
* Listas e estruturas de repetição;
* Estruturas condicionais;
* Validação de entradas;
* Tratamento de exceções;
* Organização do projeto em módulos;
* Uso de ambiente virtual;
* Gerenciamento de dependências com `requirements.txt`.

## Sobre o projeto

Este é um projeto de estudo e faz parte do meu processo de aprendizado em Python.

A ideia não foi criar um conversor com muitas funcionalidades, mas utilizar um problema relativamente simples para praticar conceitos importantes e entender melhor como uma aplicação Python pode consumir e trabalhar com dados de uma API externa.

As taxas de câmbio exibidas pelo programa são fornecidas pela API Frankfurter.
