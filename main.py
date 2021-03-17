from sqlite3.dbapi2 import OperationalError
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sqlite3

from datetime import datetime
from pydantic.dataclasses import dataclass

@dataclass(frozen=True)
class linkCollection:
    title: str
    uri:   str
    time_created: datetime

app = FastAPI()

# https://fastapi.tiangolo.com/tutorial/cors/
origins = [
    "http://ilmare.familjenberger.com:8000",
    "https://ilmare.familjenberger.com:8000",
    "http://ilmare.familjenberger.com:80",
    "https://ilmare.familjenberger.com:80",
    "http://localhost:8000/",
    "https://localhost:8000/",
    "http://localhost:80/",
    "https://localhost:80/",
]

app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins,
    allow_origins=['*'], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


try:
    connection = sqlite3.connect('history.dtek.db')
    # connection = sqlite3.connect(':memory:')
except FileNotFoundError as error:
    print(error)
    print("Database file not found.")
try: 
    cursor = connection.cursor()
    # cursor.execute("CREATE TABLE stuff(name text, num integer)")
    # cursor.execute("INSERT INTO stuff VALUES(?, ?)", ("Spotify", 3))
    # connection.commit()
except OperationalError as error:
    print(error)
    print("SQL operation failed.")


## @app.get("/")
## async def read_root():
##     return {"Message": "All your GET are belong to us!"}
##     #envarre = "%Spotify%"
##     #cursor.execute("SELECT * FROM stuff WHERE name LIKE ?", ("%Spotify%",))
##     #cursor.execute("SELECT * FROM stuff WHERE name LIKE ?", (envarre,))
## 
##     #data = cursor.fetchall()
##     #return(data)

@app.get("/Allitems")
async def readAllFromDB():
    cursor.execute('SELECT title, url FROM posts ORDER BY id DESC')
    data = cursor.fetchall()
    return(data)

@app.get("/PDF")
async def readPDFs():
    #cursor.execute('SELECT * FROM posts WHERE title LIKE '%YouTube%'')
    
    sql = """
    SELECT title, url FROM posts 
    WHERE url LIKE '%.pdf'
    ORDER BY id DESC"""
    cursor.execute(sql)

    data = cursor.fetchall()
    print(data)
    return(data)

@app.get("/Spotify")
async def readSpotify():

    # Original SQL search
    sql = """
    SELECT title, url FROM posts 
    WHERE title LIKE '%Spotify%'
    ORDER BY id DESC"""
    cursor.execute(sql)

    #envarre = "%Spotify%"
    #cursor.execute("SELECT title, url FROM posts WHERE title LIKE ?", (envarre,))

    data = cursor.fetchall()
    return(data)

@app.get("/Youtube")
async def readYouTube():
    #cursor.execute('SELECT * FROM posts WHERE title LIKE '%YouTube%'')
    
    sql = """
    SELECT title, url FROM posts 
    WHERE url LIKE '%youtube%' OR '%youtu.be%'
    ORDER BY id DESC"""
    cursor.execute(sql)

    data = cursor.fetchall()
    return(data)
    

# @app.get("/doc")
# async def read_root():
#     return {"Message": "All your GET are belong to us!"}
# 
# @app.get("/redoc")
# async def read_root():
#     return {"Message": "All your GET are belong to us!"}
