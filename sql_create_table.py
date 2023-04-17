# import the mysql client for python

import pymysql

 

# Create a connection object

dbServerName    = "localhost"

dbUser          = "root"

dbPassword      = "jonathandu07"

dbName          = "passwords"

charSet         = "utf8mb4"

cusrorType      = pymysql.cursors.DictCursor

 

connectionObject   = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,

                                     db=dbName, charset=charSet,cursorclass=cusrorType)

try:

                                     

    # Create a cursor object

    cursorObject        = connectionObject.cursor()                                     

 

    # SQL query string

    sqlQuery            = "CREATE TABLE passwords_list(id int NOT NULL AUTO_INCREMENT PRIMARY KEY, passwords varchar(255), sha512_password varchar(255), sha256_password varchar(255))"   

 

    # Execute the sqlQuery

    cursorObject.execute(sqlQuery)

   

    # SQL query string

    sqlQuery            = "show tables"   

 

    # Execute the sqlQuery

    cursorObject.execute(sqlQuery)

   

 

    #Fetch all the rows

    rows                = cursorObject.fetchall()

 

    for row in rows:

        print(row)

except Exception as e:

    print("Exeception occured:{}".format(e))

finally:

    connectionObject.close()