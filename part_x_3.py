import sys
import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def getConn():
    #database = "/Users/nikhilsagarmekhala/Desktop/sqlLiteDB.db"
    database=sys.argv[1]
    # create a database connection
    conn = create_connection(database)
    return conn

def averageWtByPokemonType():
     sql = '''select a.name,avg(b.weight) as average_weight from pokemonType a join pokemon b on 
     a.pokemon_id=b.id group by a.name '''
     conn=getConn() 
     cur = conn.cursor()
     cur.execute(sql)
     for row in cur:
       print(row)
     cur.close()  

def maxAccuracyByPokemonType():
     sql = '''select max(a.accuracy),b.name as type,a.name as move from pokemonMove a join pokemonType b 
     on a.type_id=b.id group by b.id  '''
     conn=getConn()
     cur = conn.cursor()
     cur.execute(sql)
     for row in cur:
       print(row)
     cur.close()   

def movesByPokemon():
     sql = '''select count(*) as moves ,a.name,a.id from pokemon a join pokemonMove b 
     on a.id=b.pokemon_id group by a.id order by moves desc;  '''
     conn=getConn()
     cur = conn.cursor()
     cur.execute(sql)
     for row in cur:
       print(row)
     cur.close()

def movesByPokemonOnlyByType():
     sql = '''select count(*) as moves ,a.name,a.id from pokemon a join pokemonMove b on a.id=b.pokemon_id 
     where b.type_id in (select distinct(id) from pokemonType)  
     group by a.id order by moves desc;'''
     conn=getConn()
     cur = conn.cursor()
     cur.execute(sql)
     for row in cur:
       print(row)
     cur.close()

if __name__ == '__main__':
    
    print ("=================================================================")
    print("Average weight by pokemon type:")
    print()
    print("Name, Average_Weight")
    averageWtByPokemonType()
    print ("=================================================================")
    print("Maximum Accuracy by pokemon type:")
    print()
    print("Accuracy, Type, Move")
    maxAccuracyByPokemonType()
    print ("=================================================================")
    print("Moves count by pokemon")
    print()
    print("Moves,Pokemon_name,Pokemon_id")
    movesByPokemon()
    print ("=================================================================")
    print("Moves count by pokemon only By type")
    print()
    print("Moves,Pokemon_name,Pokemon_id")
    movesByPokemonOnlyByType()
    print ("=================================================================")
    