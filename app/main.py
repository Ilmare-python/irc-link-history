from sqlite3.dbapi2 import OperationalError
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sqlite3

# from pydantic.dataclasses import dataclass

app = FastAPI()

# https://fastapi.tiangolo.com/tutorial/cors/
origins = [
    "http://ilmare.familjenberger.com:8000",
    "https://ilmare.familjenberger.com:8000",
    "http://localhost:8000",
    "https://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins,
    allow_origins=['*'],
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

@app.get("/")
async def read_root():
    return {"Message": "All your GET are belong to us!"}
    #envarre = "%Spotify%"
    #cursor.execute("SELECT * FROM stuff WHERE name LIKE ?", ("%Spotify%",))
    #cursor.execute("SELECT * FROM stuff WHERE name LIKE ?", (envarre,))

    #data = cursor.fetchall()
    #return(data)

@app.get("/Allitems")
async def readAllFromDB():
    cursor.execute('SELECT title, url FROM posts')
    data = cursor.fetchall()
    return(data)

@app.get("/PDF")
async def readPDFs():
    #cursor.execute('SELECT * FROM posts WHERE title LIKE '%YouTube%'')
    
    sql = """
    SELECT title, url FROM posts 
    WHERE url LIKE '%.pdf'"""
    cursor.execute(sql)

    data = cursor.fetchall()
    return(data)

@app.get("/Spotify")
async def readSpotify():

    # Original SQL search
    # sql = """
    # SELECT title, url FROM posts 
    # WHERE title LIKE '%Spotify%'"""
    # cursor.execute(sql)

    envarre = "%Spotify%"
    cursor.execute("SELECT title, url FROM posts WHERE title LIKE ?", (envarre,))

    data = cursor.fetchall()
    return(data)

@app.get("/Youtube")
async def readYouTube():
    #cursor.execute('SELECT * FROM posts WHERE title LIKE '%YouTube%'')
    
    sql = """
    SELECT title, url FROM posts 
    WHERE title LIKE '%YouTube%'"""
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