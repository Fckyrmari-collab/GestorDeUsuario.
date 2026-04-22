import mysql.connector

def conectar():
<<<<<<< HEAD
    
=======
        #conectar a la base de datos
>>>>>>> 97b7d75405575abc9eacc314ba50e0c2561240b4
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password= "",
        database = "empresa"
    )
    if conn .is_connected():
        print("conexion a la base de datos realizada correctamente")
    
    return conn
<<<<<<< HEAD
=======
conectar()
>>>>>>> 97b7d75405575abc9eacc314ba50e0c2561240b4
