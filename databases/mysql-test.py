# download mysql connector from http://dev.mysql.com/downloads/connector/python/
# check C:\Python27\Lib\site-packages to see if it is installed
# create your database and your user for mysql
# create the table contacts and insert one record
import mysql.connector

cnx = mysql.connector.connect(user='mycontact', password='mycontact', host='localhost', database='contactdbs')
cursor = cnx.cursor()

query = ("SELECT contactid, firstname, lastname, email FROM contact ")

cursor.execute(query)

for (contactid, firstname, lastname, email) in cursor:
  print("{}, {}, {} has email {}".format(
    contactid, firstname, lastname, email))

cursor.close()
cnx.close()
