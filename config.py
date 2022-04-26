import pyodbc 
def connection():
    database_name = "DB_NAME"
    database_user = "DB_USER"
    database_password = "DB_PASSWORD"
    database_server = "SERVER"
    dbms_driver = "DRIVER"
    ConnectionString = "DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4}".format(dbms_driver, database_server, database_name, database_user, database_password
                                                                               )
    try:
        conn = pyodbc.connect(ConnectionString)
        # cursor = conn.cursor()
        # cursor.execute("SELECT @@version;")
        # row = cursor.fetchone() 
        # while row: 
        #     print(row[0])
        #     row = cursor.fetchone()
    except Exception as e:
        print("Error connecting to database "+ str(e))

    return conn