# -*- coding: utf-8 -*-
# HuFu-DB

import uuid
import datetime
import os.path
import sys
import random
import time
from cassandra.cluster import Cluster

def createTable(dbSession):
#	result = dbSession.execute("DROP TABLE fuhu;")
	result = dbSession.execute("CREATE TABLE emprogria.fuhu (	\
									userid uuid PRIMARY KEY,	\
									name text,					\
									passwd int					\
								);﻿")

def insertRow(dbSession):
	global userIDs
	
	userID = uuid.uuid1()
	userIDs.append(userID)
	
	userName = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	userPasswd = random.randint(1, 100)
	
	sql = "INSERT INTO fuhu (userid, name, passwd) VALUES ('%s', '%s', %d);" % (userID, userName, userPasswd)
	result = dbSession.execute(sql)
	
def insertBatch(dbSession, recNum):
	for i in range(0, recNum):
		insertRow(dbSession)
		
def guessPasswd(dbSession, userID, fromNum, toNum):
	userPasswd = random.randint(fromNum, toNum)
	
	sql = "SELECT passwd FROM fuhu WHERE userid='%s';" % (userID)
	userIDtable = dbSession.execute(sql)
	
	if userIDtable is not None:
		print "%s=(%d\t%d)" % (userID, userPasswd, userIDtable[0].passwd)
		if (userPasswd > userIDtable[0].passwd):
			guessPasswd(dbSession, userID, fromNum, userIDtable[0].passwd)
		elif (userPasswd < userIDtable[0].passwd):
			guessPasswd(dbSession, userID, userIDtable[0].passwd, toNum)
		else:
			print "%s=%d" % (userID, userPasswd)
		
############################################################################		
startTime = time.clock()

cluster = Cluster()
session = cluster.connect('emprogria')

dbCluster = Cluster()
dbSession = dbCluster.connect('emprogria')

result = dbSession.execute('TRUNCATE fuhu;')

recNum = 100
if len(sys.argv) > 1:
        recNum = int(sys.argv[1])

############################################################################		
userIDs = []
insertBatch(dbSession, recNum)

for userID in userIDs:
	guessPasswd(dbSession, userID, 1, 100)

############################################################################		
stopTime = time.clock()
print (stopTime - startTime)
