import dataclasses
import aiofiles
import asyncio
import sqlite3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic.dataclasses import dataclass

#from dataclasses import dataclass
#
#@dataclass(frozen=True)
#class Links:
#    title: str
#    url: str


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

# Read from Database with SQLite
#connection = sqlite3.connect('/home/ilmare/.local/share/url-bot-rs/history.dtek.db')
connection = sqlite3.connect('history.dtek.db')
cursor = connection.cursor()


def readFromDB():
    cursor.execute('SELECT title, url FROM posts')
    data = cursor.fetchall()
    #print(data)
    #for row in data:
    #    print(row)
    return(data)


# GET request for root.
@app.get("/")
async def root_get():
   #return {"message": "All your GET is belong to us."}
   data = readFromDB()
   return {"message": data }

@app.get("static/")
async def static_get():
    return {"message": "All your static/GET is belong to us."}



def main():
    readFromDB()
    #cursor.close()
    #connection.close()


main()
