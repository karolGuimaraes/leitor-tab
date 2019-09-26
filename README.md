# leitor-tab
Interface que permite a leitura de um arquivo .tab

## Descrição do projeto
Você recebeu um arquivo de texto com os dados de vendas da empresa. Precisamos criar uma maneira para que estes dados sejam importados para um banco de dados.

Sua tarefa é criar uma interface web que aceite upload de arquivos, normalize os dados e armazene-os em um banco de dados relacional.

Sua aplicação web DEVE:

1. Aceitar (via um formulário) o upload de arquivos separados por TAB com as seguintes colunas: purchaser name, item description, item price, purchase count, merchant address, merchant name. Você pode assumir que as colunas estarão sempre nesta ordem, que sempre haverá dados em cada coluna, e que sempre haverá uma linha de cabeçalho. Um arquivo de exemplo chamado example_input.tab está incluído neste repositório.
1. Interpretar ("parsear") o arquivo recebido, normalizar os dados, e salvar corretamente a informação em um banco de dados relacional.
1. Exibir a receita bruta total representada pelo arquivo enviado após o upload + parser.
1. Ser escrita obrigatoriamente em Ruby 2.0+, Python 2.7+, Java 7+ ou PHP 5.3+ (caso esteja entrevistando para uma vaga específica, utilize a linguagem solicitada pela vaga).
1. Ser simples de configurar e rodar, funcionando em ambiente compatível com Unix (Linux ou Mac OS X). Ela deve utilizar apenas linguagens e bibliotecas livres ou gratuitas.

Sua aplicação web não precisa:

1. Lidar com autenticação ou autorização (pontos extras se ela fizer, mais pontos extras se a autenticação for feita via OAuth).
1. Ser escrita usando algum framework específico (mas não há nada errado em usá-los também, use o que achar melhor).
1. Ter uma aparência bonita.

## Avaliação
Seu projeto será avaliado de acordo com os seguintes critérios. 

1. Sua aplicação preenche os requerimentos básicos?
1. Você documentou a maneira de configurar o ambiente e rodar sua aplicação?
1. Você seguiu as instruções de envio do desafio?
1. Qualidade e cobertura dos testes unitários.

Adicionalmente, tentaremos verificar a sua familiarização com as bibliotecas padrões (standard libs), bem como sua experiência com programação orientada a objetos a partir da estrutura de seu projeto.


## Configurando
 - Clonar o projeto: git clone https://github.com/karolGuimaraes/leitor-tab
 - ` python3 -m venv env` ( Criar um ambiente virtual )
 - ` source env/bin/activate ` ( Iniciar o ambiente virtual )
 - Acesse a pasta /leitor-tab
 - ` pip install -r requirements.txt ` ( Instalando dependências )
 - ` python manage.py makemigrations && python manage.py migrate `
 - Para executar o projeto ` python manage.py runserver `
 - Acessar : ` localhost:8000 `


### Teste 

Para executa os testes unitários: 

` python manage.py test `

Resposta similar:

        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        ....
        ----------------------------------------------------------------------
        Ran 4 tests in 0.041s

        OK
        Destroying test database for alias 'default'...


### OBS: Os arquivos estão na pasta /leitor_tab/static/arquivos

