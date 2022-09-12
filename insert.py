import pymysql.cursors

fichier = open("passwords.txt", "r")


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='jonathandu07',
                             database='passwords',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



with connection:
    with connection.cursor() as cursor:
        # Create a new record
        for i in fichier:
            sql = "INSERT INTO `passwords_list` (`passwords`) VALUES (%s)"
            cursor.execute(sql, (i))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `passwords` FROM `passwords_list`"
        #cursor.execute(sql, (i))
        result = cursor.fetchone()
        print(result)
