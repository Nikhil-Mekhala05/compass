# Steps to run the scripts

Prerequisite to run the python file
Run the command on the linux command prompt
pip3 install pokebase
This will install pokebase python API

Prerequisite to run the part_x_2.py

please run all the create table scripts as mentioned in part_x_1.txt and proceed to below steps

Command to run part_x_2:
python3 part_x_2.py #number of pokemons to download #path of sqllite database

example command:
python3 pokemon_download.py 15 /Users/nikhilsagarmekhala/Desktop/sqlLiteDB.db

This command will load all 15 pokemons data into tables pokemon,pokemonMove,pokemonType

Command to run part_x_3:

NOTE: part_x_3.py contains all the functions which pulls data from sqlite and generates the matrix required

1.averageWtByPokemonType(): Returns the average weight of the pokemon by type
2.maxAccuracyByPokemonType():Returns the maximum accuracy move of a pokemon type with in the number of pokemon types downloaded
3.movesByPokemon():Returns Total moves by pokemon
4.movesByPokemonOnlyByType(): Returns total moves by pokemon with only the types mentioned in their data

python3 part_x_3.py #path of the sqlite database folder

example command:
python3 part_x_3.py /Users/nikhilsagarmekhala/Desktop/sqlLiteDB.db



This command will generate all the summaries as requested.



