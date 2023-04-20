import aoisqlite
from sqlite3 import Error

#name the DB

NAME = 'password.db'

class Database():
    async def ConnectDatabase(**kwargs):
        try:
            db = await aoisqlite.connect(NAME)
            c = await db.cursor()
            await c.execute("CREATE TABLE IF NOT EXISTS passwordTable (id INTEGER PRIMARY KEY)")
            await  db.commit()
            return db
        except Error:
            print (Error)
