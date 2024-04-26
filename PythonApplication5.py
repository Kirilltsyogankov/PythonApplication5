from pickle import NONE
from sqlite3 import *
from sqlite3 import Error
from os import *

def create_connect(path:str):
    connection=None 
    try:
        connection=connect(path)
        print("Uhendus on olemas!")
    except Error as e:
        print(f"Tekkis viga: {e}")
def execute_query(connection,query):
    try:
        cursor=connection.curseer

filename=path.abspath(__file__)
dbdir=filename.rstrip('Tee_andmebaasiga.py')
dbpath=path.join(dbdir,"data.db")
conn=create_connect(dbpath)