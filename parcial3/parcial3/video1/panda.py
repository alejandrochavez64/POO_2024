import pymysql

miConexion = pymysql.connect(host="localhost", user = "root", paswod="12345678", db="usuarios")
cur = miconexion.Cursor()
cur.execute("select nombre, email from persona")
for nombre, email in cur.fetchall():
    print(nombre, " ! ", email)

miConexion.Close()