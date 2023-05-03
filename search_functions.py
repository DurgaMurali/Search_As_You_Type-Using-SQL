from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


# Update the listbox
def update(data,keyword_list):
	# Clear the listbox
	keyword_list.delete(0, END)

	# Add keywords to listbox
	for item in data:
		keyword_list.insert(END, item)	

# # Create function to implement different search_exact_index algorithms 
def search_exact_index(typed,dbpl_table,keyword_list):
	# print("search_exact_index")
	# print("typed - ",typed)
	connection=mysql.connect (host="localhost", user="root", password="Mydatabase", database="paperdb")
	cursor=connection.cursor()

	## query from paper Section 3.2 
	query1 = "SELECT Keyword from paperdb.keywordtable where paperdb.keywordtable.keyword LIKE %s"
	# print("typed",typed)
	keyword = (typed + '%', )
	cursor.execute(query1,keyword)
	data = cursor.fetchall()
	update(data,keyword_list)

	## query from paper Section 3.2 
	query2 = """SELECT Title, Authors, Booktitle, Year FROM paperdb.exactprefixtable, paperdb.exactinvertedindextable, paperdb.dblp 
			WHERE paperdb.exactprefixtable.Prefix = %s
			AND paperdb.exactprefixtable.UpperKID >= paperdb.exactinvertedindextable.KeywordID 
			AND paperdb.exactprefixtable.LowerKID <= paperdb.exactinvertedindextable.KeywordID  
			AND paperdb.exactinvertedindextable.RecordID = paperdb.dblp.RecordID"""
	# print("typed",typed)
	keyword = (typed, )
	cursor.execute(query2,keyword)

	# clearing table view
	for item in dbpl_table.get_children():
			dbpl_table.delete(item)

	# printing the new view use typed string as prefix keyword
	cpt = 0 # Counter representing the ID
	for row in cursor:   
		dbpl_table.insert('', 'end', text=str(cpt), values=(row[0], row[1], row[2], row[3]))
	cpt += 1 

	connection.close()


# Create function to implement different search_fuzzy_gram algorithms 
def search_fuzzy_gram(typed,dbpl_table,keyword_list):
	# print("search_fuzzy_gram")
	# print("typed - ",typed)
	connection=mysql.connect (host="localhost", user="root", password="Mydatabase", database="paperdb")
	cursor=connection.cursor()

	## query from paper Section 3.2 
	query1 = "SELECT Keyword from paperdb.keywordtable where paperdb.keywordtable.keyword LIKE %s"
	# print("typed",typed)
	keyword = ('%' + typed + '%', )
	cursor.execute(query1,keyword)
	data = cursor.fetchall()
	update(data,keyword_list)

	query = """ select Title, Authors, Booktitle, Year FROM paperdb.PrefixTable, paperdb.NgramsTable, paperdb.invertedindextable, paperdb.dblp 
	where paperdb.NgramsTable.Prefix = paperdb.PrefixTable.Prefix
	AND paperdb.PrefixTable.UpperKID >= paperdb.invertedindextable.KeywordID 
	AND paperdb.PrefixTable.LowerKID <= paperdb.invertedindextable.KeywordID 
	AND paperdb.invertedindextable.RecordID = paperdb.dblp.RecordID
	AND paperdb.NgramsTable.Ngram = %s """
	keyword = (typed, )
	cursor.execute(query, keyword)

	# clearing table view
	for item in dbpl_table.get_children():
			dbpl_table.delete(item)

	# printing the new view use typed string as prefix keyword
	cpt = 0 # Counter representing the ID
	for row in cursor:   
		dbpl_table.insert('', 'end', text=str(cpt), values=(row[0], row[1], row[2], row[3]))
	cpt += 1 

	connection.close()



# Create function to implement differeent search_fuzzy_neighborhood algorithms 
def search_fuzzy_neighborhood(typed,dbpl_table,keyword_list):
	# print("search_fuzzy_neighborhood")
	# print("typed - ",typed)
	connection=mysql.connect (host="localhost", user="root", password="Mydatabase", database="paperdb")
	cursor=connection.cursor()
	query = """ select Title, Authors, Booktitle, Year FROM paperdb.PrefixTable, paperdb.NeighborhoodDeletionTable, paperdb.invertedindextable, paperdb.dblp 
	where paperdb.NeighborhoodDeletionTable.Prefix = paperdb.PrefixTable.Prefix
	AND paperdb.prefixtable.UpperKID >= paperdb.invertedindextable.KeywordID 
	AND paperdb.prefixtable.LowerKID <= paperdb.invertedindextable.KeywordID 
	AND paperdb.invertedindextable.RecordID = paperdb.dblp.RecordID
	AND paperdb.NeighborhoodDeletionTable.iDeletedString = %s 
	AND paperdb.NeighborhoodDeletionTable.iDeletion<=2 """
	keyword = (typed, )
	cursor.execute(query, keyword)

	# clearing table view
	for item in dbpl_table.get_children():
			dbpl_table.delete(item)

	# printing the new view use typed string as prefix keyword
	cpt = 0 # Counter representing the ID
	for row in cursor:   
		dbpl_table.insert('', 'end', text=str(cpt), values=(row[0], row[1], row[2], row[3]))
	cpt += 1 

	connection.close()