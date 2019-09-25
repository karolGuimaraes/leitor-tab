# leitor-tab
Interface que permite a leitura de um arquivo .tab

# Configurando
 - Clonar o projeto: git clone https://github.com/karolGuimaraes/leitor-tab
 - ` python3 -m venv env` ( Criar um ambiente virtual )
 - ` source env/bin/activate ` ( Iniciar o ambiente virtual )
 - Acesse a pasta /leitor-tab
 - ` python manage.py makemigrations && python manage.py migrate `
 - Para executar o projeto ` python manage.py runserver `
 - Acessar : ` localhost:8000 `


### Teste 

Para executa os teste unitários: 

` python manage.py test `

Resposta similar:

        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        ....
        ----------------------------------------------------------------------
        Ran 4 tests in 0.041s

        OK
        Destroying test database for alias 'default'...


