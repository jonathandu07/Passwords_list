import pymysql.cursors
import hashlib
fichier = open("passwords.txt", "r", encoding="utf-8")


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='jonathandu07',
                             database='passwords',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def Sha512Hash(Password):
    HashedPassword=hashlib.sha512(Password.encode('utf-8')).hexdigest()


with connection:
    with connection.cursor() as cursor:
        # Create a new record
        for i in fichier:
            #u = i.encode('utf-8')
            j= Sha512Hash(i)
            sql = "INSERT INTO `passwords_list` (passwords, hash_password) VALUES (%s,%s)"
            cursor.execute(sql, (i,j))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `passwords_list`"
        #cursor.execute(sql, (i))
        result = cursor.fetchone()
        print(result)
