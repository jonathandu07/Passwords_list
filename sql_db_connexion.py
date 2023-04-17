
# import the mysql client for python

import pymysql
 

# Create a connection object

databaseServerIP            = "localhost"  # IP address of the MySQL database server

databaseUserName            = "root"       # User name of the database server

databaseUserPassword        = "jonathandu07"           # Password for the database user

 

newDatabaseName             = "passwords" # Name of the database that is to be created

charSet                     = "utf8mb4"     # Character set

cusrorType                  = pymysql.cursors.DictCursor

 

connectionInstance   = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,

                                     charset=charSet,cursorclass=cusrorType)

 

try:

    # Create a cursor object

    cursorInsatnce        = connectionInstance.cursor()                                    

 

    # SQL Statement to create a database

    sqlStatement            = "CREATE DATABASE "+newDatabaseName  

 

    # Execute the create database SQL statment through the cursor instance

    cursorInsatnce.execute(sqlStatement)

 

    # SQL query string

    sqlQuery            = "SHOW DATABASES"

 

    # Execute the sqlQuery

    cursorInsatnce.execute(sqlQuery)

 

    #Fetch all the rows

    databaseList                = cursorInsatnce.fetchall()

 

    for datatbase in databaseList:

        print(datatbase)

 

except Exception as e:

    print("Exeception occured:{}".format(e))

 

finally:

    connectionInstance.close()
    
