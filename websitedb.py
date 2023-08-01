import mysql.connector 

dataBase = mysql.connector.connect(
	host= 'localhost',
	user='root',
	passwd='443512257@Ta',
	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE tameemco")

print('all Done!')