import sys
import pokebase
import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def pokemonMove_insert(conn, pokemon_move):
    
 
    sql = ''' INSERT INTO pokemonMove(name,pokemon_id,id,accuracy,type_id)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    
    cur.execute(sql, pokemon_move)
    cur.execute("commit")
    return cur.lastrowid
def pokemonType_insert(conn, pokemon_type):
    
 
    sql = ''' INSERT INTO pokemonType(name,pokemon_id,id)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    
    cur.execute(sql, pokemon_type)
    cur.execute("commit")
    return cur.lastrowid

def pokemon_insert(conn, pokemon):
    
 
    sql = ''' INSERT INTO pokemon(id,name,weight)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    
    cur.execute(sql, pokemon)
    cur.execute("commit")
    return cur.lastrowid

def getConn():
    #database = "/Users/nikhilsagarmekhala/Desktop/sqlLiteDB.db"
    database=sys.argv[2]
    # create a database connection
    conn = create_connection(database)
    return conn

def truncateTables(conn=getConn()):
  sql = '''delete from pokemon;delete from pokemonMove;delete from pokemonType'''
  cur = conn.cursor()  
  cur.executescript(sql)
  cur.close()
  




def getPokemonData(pokemon_id):
 truncateTables()
 for n in range(1,pokemon_id+1):
  p1=pokebase.pokemon(n)
  pokemon=(p1.id,p1.name,p1.weight)
  conn=getConn()
  lstRowid=pokemon_insert(conn,pokemon)
 
  for i in range(0,len(p1.moves)):
   try:
    move=p1.moves[i].move.name
    accuracy=pokebase.move(move).accuracy
    if (accuracy==None):
     accuracy=0
    type=pokebase.move(move).type.name
    print("pokemon name:"+p1.name)
    print("pokemon id:"+str(p1.id))
    print("move name :"+move)
    print("move id:"+str(p1.moves[i].move.id))
    print ("type="+type)
    pokemon_move=(move,p1.id,p1.moves[i].move.id,accuracy,pokebase.move(move).type.id)
    conn=getConn()
    lstRowid=pokemonMove_insert(conn,pokemon_move)
   except:
    continue 
  
 
  
  for i in range(0,len(p1.types)):
   print("pokemon type:"+p1.types[i].type.name)
   pokemon_type=(p1.types[i].type.name,p1.id,p1.types[i].type.id)
   conn=getConn()
   lstRowid=pokemonType_insert(conn,pokemon_type)
   print("pokemon weight:"+str(p1.weight))
   



if __name__ == '__main__':
    getPokemonData(int(sys.argv[1]))
    




