import sqlite3
conn = sqlite3.connect('loginfo.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE Users (Id INTEGER, Email TEXT, Password TEXT, Friends INTEGER)")

cursor.execute("INSERT INTO Users VALUES(1, 'yuva', 'webdevvYuva', 65)")
cursor.execute("INSERT INTO Users VALUES(2, 'spider@avengers.com', 'homeAway', 112)")
cursor.execute("INSERT INTO Users VALUES(3, 'iron@avengers.com', 'iDiedAgain', 927)")
cursor.execute("INSERT INTO Users VALUES(4, 'hulk@avengers.com', 'greenMan', 27)")

user_email = input('Provide your email: ')
provided_pass = input('Now, provide your password: ')

cursor.execute("select * from Users where email = :email", {'email': user_email})
user = cursor.fetchone()

if user is not None and user[2] == provided_pass:
   print('Welcome '+user_email)
else:
   print('Invalid user email or password')

conn.commit()
conn.close()
