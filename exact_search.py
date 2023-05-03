from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from rake_nltk import Rake

##--------------------------------AuxiliaryTables Functionality----------------------------------------------------------------------------------
# Create Keyword, Inverted Index and Prefix tables for EXACT search
def createAuxiliaryTables_exact():
	connection=mysql.connect (host="localhost", user="root", password="Mydatabase", database="paperdb")
	cursor=connection.cursor()
	cursor.execute("SELECT RecordID, Title, Booktitle from paperdb.dblp")
	rake = Rake()
	records = cursor.fetchall()

	keyword_dict = dict()
	sorted_keyword_dict = dict()

	for record in records:
		rake.extract_keywords_from_text(record[1])
		word_list = rake.get_ranked_phrases()
		word_list.append(record[2].lower())
		for word in word_list:
			key_list = word.split(' ')		
			for key in key_list:
				if(key not in keyword_dict):
					keyword_dict[key] = []

				keyword_dict[key].append(record[0])
				

	# Sort the keywords
	for keyword in sorted(keyword_dict.keys()):
		# print(keyword)
		sorted_keyword_dict[keyword] = []
		sorted_keyword_dict[keyword].append(keyword_dict[keyword])

	# print("sorted_keyword_dict:", sorted_keyword_dict)
	
	keyword_tuple_list = []
	inverted_index_tuple_list = []
	index = 1

	# Create tuple list for keyword and inverted index tables
	for keyword in sorted_keyword_dict.keys():
		keyword_tuple = tuple((index, keyword))
		keyword_tuple_list.append(keyword_tuple)
		record_id_list = keyword_dict[keyword]
		for record_id in record_id_list:
			inverted_index_tuple = tuple((index, record_id))
			inverted_index_tuple_list.append(inverted_index_tuple)
		
		index = index + 1

	keyword_query = """	INSERT INTO paperdb.keywordtable(KeywordID, Keyword) values (%s, %s) """
	cursor.executemany(keyword_query, keyword_tuple_list)
	inverted_index_query = """ INSERT INTO paperdb.exactinvertedindextable(KeywordID, RecordID) values (%s, %s) """
	cursor.executemany(inverted_index_query, inverted_index_tuple_list)
	cursor.execute("COMMIT")
	cursor.close()

	# print("Prefix table")
	alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for alpha in alphabet_list:
		computePrefix_exact(alpha, keyword_tuple_list)



def computePrefix_exact(alphabet, keyword_list):	
	alpha_list = []
	for tuple in keyword_list:
		if tuple[1][0] == alphabet:
			alpha_list.append(tuple)

	# print("alpha_list",alpha_list)

	
	len_alpha = len(alpha_list)

	if len_alpha == 0:
		return

	tuple_list=[]
	for word in alpha_list:
		for i in range(1, len(word[1])+1):
			tuple_list.append((word[1][:i], word[0], word[0]))
			
	
	tuple_list.sort()

	# for value in tuple_list:
	# 	while (value[1])

	# print(tuple_list)
	connection=mysql.connect (host="localhost", user="root", password="Mydatabase", database="paperdb")
	cursor=connection.cursor()
	query = """	INSERT INTO paperdb.exactPrefixTable(Prefix, LowerKID, UpperKID) values (%s, %s, %s) """
	cursor.executemany(query, tuple_list)
	cursor.execute("COMMIT")

	cursor.close()

#---------------------------------------------------------------------------------------------------------------------------------------