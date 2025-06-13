crie uma env com:

python -m venv env

execute a env com:

./env/Scripts/activate

para instalar as biblitecas necessarias do projeto use:

pip install -r requirements.txt

Por fim, execute com:

python ./manage.py runserver


caso ocorra algum erro com o banco de dados apague:

db.sqlite3
./migrations
./__pycache__ (Os dois, do projeto e do app)

em seguida use:

python ./manage.py makemigrations app

python ./manage.py migrate

para subir as planilhas para as respectivas tabelas use o arquivo uploadDB.py, na variavel filename, coloque entre as aspas o nome do arquivo que deseja subir: 

filename = "contador"

execute com:

python ./uploadDB.py

faça isso para cada arquivo que deseja subir (apenas uma vez para cada, ou haverão registros repetidos e voce precisara apagar e começar novamente)