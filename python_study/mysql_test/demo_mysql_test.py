import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123456",
    database = "huadu-test"
)
# 查询是否连接
# print(mydb)

mycursor = mydb.cursor()

mycursor.execute("select * from bd_community")

result = mycursor.fetchall()

for x in result:
    print(x)

