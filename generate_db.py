import mysql.connector

host = input("Host : ")
user = input("Username : ")
password = input("Password : ")
db = input("Database : ")

def buatDatabase(host, user, password, db):
    myDB = mysql.connector.connect(
        host = host,
        user = user,
        password = password
    )
    cursor = myDB.cursor()
    cursor.execute(f"CREATE DATABASE {db}")
    
def buatTable(host, user, password, db):
    myDB = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = db
    )
    cursor = myDB.cursor()
    cursor.execute("CREATE TABLE db_produk (id INT AUTO_INCREMENT PRIMARY KEY, kodeBarang VARCHAR(255), namaBarang VARCHAR(255), stokBarang INT(11), hargaBarang INT(255), deskripsiBarang TEXT)")

f = open("data.log",'w')
f.write(f"{host}\n{user}\n{password}\n{db}")    
f.close()
    
if __name__ == '__main__':
    buatDatabase(host, user, password, db)
    buatTable(host, user, password, db)