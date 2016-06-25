import sqlite3

# Create a connection and cursor with the DB
dbConnection = sqlite3.connect('Data.db')
dbCursor = dbConnection.cursor()

##### Never do this -- insecure! ####
# symbol = 'RHAT'
# dbCursor.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
dbCursor.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print dbCursor.fetchone()
print dbCursor.fetchall()

dbConnection.close()