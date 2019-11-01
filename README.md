# Steps to run the scripts

Prerequisite to run the python file
Run the command on the linux command prompt
pip3 install pokebase
This will install pokebase python API

Prerequisite to run the part_x_2.py

please run all the create table scripts as mentioned in part_x_1.txt and proceed to below steps

Command to run part_x_2:
python3 part_x_2.py <number of pokemons to download> <path of sqllite database>

example command:
python3 pokemon_download.py 15 /Users/nikhilsagarmekhala/Desktop/sqlLiteDB.db

This command will load all 15 pokemons data into tables pokemon,pokemonMove,pokemonType

Command to run part_x_3:

NOTE: part_x_3.py contains all the functions which pulls data from sqlite and generates the matrix required

1.averageWtByPokemonType(): Returns the average weight of the pokemon by type
2.maxAccuracyByPokemonType():Returns the maximum accuracy move of a pokemon type with in the number of pokemon types downloaded
3.movesByPokemon():Returns Total moves by pokemon
4.movesByPokemonOnlyByType(): Returns total moves by pokemon with only the types mentioned in their data

python3 part_x_3.py <path of the sqlite database folder>

example command:
python3 part_x_3.py /Users/nikhilsagarmekhala/Desktop/sqlLiteDB.db



This command will generate all the summaries as requested:

=================================================================
Average weight by pokemon type:

Name, Average_Weight
('bug', 145.83333333333334)
('fire', 393.3333333333333)
('flying', 612.5)
('grass', 399.6666666666667)
('poison', 271.0)
('water', 390.0)
=================================================================
Maximum Accuracy by pokemon type:

Accuracy, Type, Move
(100, 'flying', 'wing-attack')
(100, 'poison', 'sludge')
(100, 'bug', 'signal-beam')
(100, 'fire', 'fire-punch')
(100, 'water', 'water-gun')
(100, 'grass', 'vine-whip')
=================================================================
Moves count by pokemon

Moves,Pokemon_name,Pokemon_id
(108, 'charizard', 6)
(93, 'charmander', 4)
(93, 'blastoise', 9)
(91, 'squirtle', 7)
(84, 'charmeleon', 5)
(78, 'bulbasaur', 1)
(77, 'venusaur', 3)
(77, 'butterfree', 12)
(76, 'wartortle', 8)
(75, 'beedrill', 15)
(66, 'ivysaur', 2)
(5, 'caterpie', 10)
(5, 'metapod', 11)
(5, 'kakuna', 14)
(4, 'weedle', 13)
=================================================================
Moves count by pokemon only By type

Moves,Pokemon_name,Pokemon_id
(29, 'bulbasaur', 1)
(29, 'charizard', 6)
(29, 'butterfree', 12)
(26, 'beedrill', 15)
(24, 'venusaur', 3)
(21, 'ivysaur', 2)
(20, 'charmander', 4)
(20, 'squirtle', 7)
(18, 'charmeleon', 5)
(18, 'blastoise', 9)
(16, 'wartortle', 8)
(3, 'weedle', 13)
(2, 'caterpie', 10)
(2, 'metapod', 11)
(2, 'kakuna', 14)
=================================================================





