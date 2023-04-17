import pymysql.cursors
import hashlib
import asyncio
#fichier = open("passwords.txt", "r", encoding="utf-8")

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='jonathandu07',
                             database='passwords',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def Sha512Hash(Password):
    HashedPassword=hashlib.sha512(Password.encode('utf-8')).hexdigest()
    return HashedPassword

def Sha256Hash(Password):
    HashedPassword=hashlib.sha256(Password.encode('utf-8')).hexdigest()
    return HashedPassword

def Sha256Hash(Password):
    HashedPassword=hashlib.sha256(Password.encode('utf-8')).hexdigest()
    return HashedPassword

with connection:

        # Create a new record
        async def insert1():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        async def insert2():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        async def insert3():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        async def insert4():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        async def insert5():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        async def insert6():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert7():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert8():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert9():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert10():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert11():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert12():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert13():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert14():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert15():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert16():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert17():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert18():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert19():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert20():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()


        async def insert21():
            with connection.cursor() as cursor:
                fichier = open("super-list.txt.001", "r", encoding="utf-8")
                for i in fichier:
                    #u = i.encode('utf-8')
                    s515= Sha512Hash(i)
                    s256= Sha512Hash(i)
                    sql = "INSERT INTO `passwords_list` (passwords, sha512, sha256) VALUES (%s,%s,%s)"
                    cursor.execute(sql, (i, s515, s256))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

"""
with connection.cursor() as cursor:
    # Read a single record
    sql = "SELECT * FROM `passwords_list`"
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
"""

asyncio.run(insert1())
asyncio.run(insert2())
asyncio.run(insert3())
asyncio.run(insert4())
asyncio.run(insert5())
asyncio.run(insert6())
asyncio.run(insert7())
asyncio.run(insert8())
asyncio.run(insert9())
asyncio.run(insert10())
asyncio.run(insert11())
asyncio.run(insert12())
asyncio.run(insert13())
asyncio.run(insert14())
asyncio.run(insert15())
asyncio.run(insert16())
asyncio.run(insert17())
asyncio.run(insert18())
asyncio.run(insert19())
asyncio.run(insert20())
asyncio.run(insert21())
