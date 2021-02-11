import asyncio
import sqlite3

from fastapi import FastAPI
from pydantic.dataclasses import dataclass

# from dataclasses import dataclass

app = FastAPI()


# Read from Database with SQLite

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

# POST request for root.
@app.post("/")
async def root_post():
    data = readFromDB()
    return {"message": data }


#prepare_for_foo()
#task = loop.create_task(foo())
#remaining_work_not_depends_on_foo()
#loop.run_until_complete(task)

##loop = asyncio.get_event_loop()

# To be used when run as an API.
#async def main():
#    if __name__ == "__main__":
#        await readFromDB()
#        #asyncio.run(main())




def main():
    readFromDB()
    #cursor.close()
    #connection.close()


main()
