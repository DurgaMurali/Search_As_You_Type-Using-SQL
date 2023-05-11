from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import Levenshtein
from Levenshtein import distance
from time import time

# Update the listbox
def update(data,keyword_list):
	# Clear the listbox
	keyword_list.delete(0, END)

	# Add keywords to listbox
	for item in data:
		keyword_list.insert(END, item)	

# # Create function to implement different search_exact_index algorithms 
def search_exact_index(typed,dbpl_table,keyword_list, dbHost, dbUser, dbPassword):
	connection=mysql.connect (host=dbHost, user=dbUser, password=dbPassword, database="paperdb")
	cursor=connection.cursor()

	## query from paper Section 3.2 
	query1 = "SELECT Keyword from paperdb.keywordtable where paperdb.keywordtable.keyword LIKE %s"
	keyword = (typed + '%', )
	cursor.execute(query1,keyword)
	data = cursor.fetchall()
	update(data,keyword_list)

	## query from paper Section 3.2 
	query2 = """SELECT Title, Authors, Booktitle, Year FROM paperdb.exactprefixtable, paperdb.invertedindextable, paperdb.dblp 
			WHERE paperdb.exactprefixtable.Prefix = %s
			AND paperdb.exactprefixtable.UpperKID >= paperdb.invertedindextable.KeywordID 
			AND paperdb.exactprefixtable.LowerKID <= paperdb.invertedindextable.KeywordID  
			AND paperdb.invertedindextable.RecordID = paperdb.dblp.RecordID"""
	keyword = (typed, )
	start_time = time()
	cursor.execute(query2,keyword)
	end_time = time()
	print("Exact search time taken is ", end_time-start_time)

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
def search_fuzzy_gram(typed,dbpl_table,keyword_list, dbHost, dbUser, dbPassword):
	connection=mysql.connect (host=dbHost, user=dbUser, password=dbPassword, database="paperdb")
	cursor=connection.cursor()

	## query from paper Section 3.2 
	query1 = "SELECT Keyword from paperdb.keywordtable where paperdb.keywordtable.keyword LIKE %s"
	keyword = ('%' + typed + '%', )
	cursor.execute(query1,keyword)
	data = cursor.fetchall()
	update(data,keyword_list)

	query = """ select distinct Title, Authors, Booktitle, Year FROM paperdb.PrefixTable, paperdb.NgramsTable, paperdb.invertedindextable, paperdb.dblp 
	where paperdb.NgramsTable.Prefix = paperdb.PrefixTable.Prefix
	AND paperdb.PrefixTable.UpperKID >= paperdb.invertedindextable.KeywordID 
	AND paperdb.PrefixTable.LowerKID <= paperdb.invertedindextable.KeywordID 
	AND paperdb.invertedindextable.RecordID = paperdb.dblp.RecordID
	AND paperdb.NgramsTable.Ngram = %s """
	keyword = (typed, )
	start_time = time()
	cursor.execute(query, keyword)
	end_time = time()
	print("Fuzzy ngram search time taken is ", end_time-start_time)

	# clearing table view
	for item in dbpl_table.get_children():
			dbpl_table.delete(item)

	# printing the new view use typed string as prefix keyword
	cpt = 0 # Counter representing the ID
	for row in cursor:   
		dbpl_table.insert('', 'end', text=str(cpt), values=(row[0], row[1], row[2], row[3]))
	cpt += 1 

	connection.close()


# Perform fuzzy search on a list of choices with one allowed substitution and return a list of matched choices.
def fuzzy_search_one_wrong_char(query, choices, threshold=1):    
    results = []
    for choice in choices:
        if distance(query, choice) <= threshold:
            results.append(choice)
	    
    return query if len(results) == 0 else results[0]

# Create function to implement different search_fuzzy_neighborhood algorithms 
def search_fuzzy_neighborhood(typed,dbpl_table,keyword_list, dbHost, dbUser, dbPassword):
	connection=mysql.connect (host=dbHost, user=dbUser, password=dbPassword, database="paperdb")
	cursor=connection.cursor()
	query_ = "select ngram from paperdb.ngramstable;"
	cursor.execute(query_)
	data_ = cursor.fetchall()
	list_ = []
	for val in data_:
		list_.append(val[0])

	typed_ = fuzzy_search_one_wrong_char(typed,list_)

	query1 = "SELECT Keyword from paperdb.keywordtable where paperdb.keywordtable.keyword LIKE %s"
	keyword = ('%' + typed_ + '%', )
	cursor.execute(query1,keyword)
	data = cursor.fetchall()
	update(data,keyword_list)

	query = """ select distinct Title, Authors, Booktitle, Year FROM paperdb.PrefixTable, paperdb.NgramsTable, paperdb.invertedindextable, paperdb.dblp 
	where paperdb.NgramsTable.Prefix = paperdb.PrefixTable.Prefix
	AND paperdb.PrefixTable.UpperKID >= paperdb.invertedindextable.KeywordID 
	AND paperdb.PrefixTable.LowerKID <= paperdb.invertedindextable.KeywordID 
	AND paperdb.invertedindextable.RecordID = paperdb.dblp.RecordID
	AND paperdb.NgramsTable.Ngram = %s """
	keyword = (typed_, )
	start_time = time()
	cursor.execute(query, keyword)
	end_time = time()
	print("Levenshtein search time taken is ", end_time-start_time)

	# clearing table view
	for item in dbpl_table.get_children():
			dbpl_table.delete(item)

	# printing the new view use typed string as prefix keyword
	cpt = 0 # Counter representing the ID
	for row in cursor:   
		dbpl_table.insert('', 'end', text=str(cpt), values=(row[0], row[1], row[2], row[3]))
	cpt += 1 

	connection.close()