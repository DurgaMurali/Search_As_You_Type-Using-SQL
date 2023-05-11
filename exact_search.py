from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from rake_nltk import Rake

##--------------------------------AuxiliaryTables Functionality----------------------------------------------------------------------------------
# Create Prefix tables for EXACT search
def createAuxiliaryTables_exact(dbHost, dbUser, dbPassword):
	connection=mysql.connect (host=dbHost, user=dbUser, password=dbPassword, database="paperdb")
	cursor=connection.cursor()
	cursor.execute("SELECT keywordid, keyword from paperdb.keywordtable")
	keyword_tuple_list = cursor.fetchall()
	alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for alpha in alphabet_list:
		computePrefix_exact(alpha, keyword_tuple_list, dbHost, dbUser, dbPassword)



def computePrefix_exact(alphabet, keyword_list, dbHost, dbUser, dbPassword):	
	alpha_list = []
	for tuple in keyword_list:
		if tuple[1][0] == alphabet:
			alpha_list.append(tuple)
	
	len_alpha = len(alpha_list)

	if len_alpha == 0:
		return

	tuple_list=[]
	for word in alpha_list:
		for i in range(1, len(word[1])+1):
			tuple_list.append((word[1][:i], word[0], word[0]))
			
	
	tuple_list.sort()

	connection=mysql.connect (host=dbHost, user=dbUser, password=dbPassword, database="paperdb")
	cursor=connection.cursor()
	query = """	INSERT INTO paperdb.exactPrefixTable(Prefix, LowerKID, UpperKID) values (%s, %s, %s) """
	cursor.executemany(query, tuple_list)
	cursor.execute("COMMIT")

	cursor.close()


def TruncateTables(dbHost, dbUser, dbPassword):
	connection=mysql.connect (host=dbHost, user=dbUser, password=dbPassword, database="paperdb")
	cursor=connection.cursor()
	cursor.execute("TRUNCATE paperdb.exactprefixtable")
	cursor.close()

def exactTableFunctions(dbHost, dbUser, dbPassword):
	TruncateTables(dbHost, dbUser, dbPassword)
	createAuxiliaryTables_exact(dbHost, dbUser, dbPassword)