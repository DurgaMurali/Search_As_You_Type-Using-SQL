# from tkinter import *
# from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import os.path
from rake_nltk import Rake


# Create Keyword, Inverted Index and Prefix tables --- for fuzzy search and Gram-based method
def createAuxiliaryTables():
	connection=mysql.connect (host="localhost", user="root", password="Mydatabase", database="paperdb")
	cursor=connection.cursor()
	cursor.execute("SELECT RecordID, Title, Booktitle from paperdb.dblp")
	rake = Rake()
	
	keyword_dict = dict()
	sorted_keyword_dict = dict()
	for record in cursor:
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
	
	keyword_tuple_list = []
	inverted_index_tuple_list = []
	index = 1
	# Create tuple list for keyword and inverted index tables
	for keyword in sorted_keyword_dict.keys():
		keyword_tuple = tuple((index, keyword))
		keyword_tuple_list.append(keyword_tuple)
		record_id_list = keyword_dict[keyword]
		record_set = set(record_id_list)
		for record_id in record_set:
			inverted_index_tuple = tuple((index, record_id))
			inverted_index_tuple_list.append(inverted_index_tuple)
		
		index = index + 1

	inverted_index_query = """ INSERT INTO paperdb.invertedindextable (KeywordID, RecordID) values (%s, %s) """
	cursor.executemany(inverted_index_query, inverted_index_tuple_list)
	cursor.execute("COMMIT")
	cursor.close()

	alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for alpha in alphabet_list:
		computePrefix(alpha, keyword_tuple_list)


def computePrefix(alphabet, keyword_list):	
	alpha_list = []
	for tuple in keyword_list:
		if tuple[1][0] == alphabet:
			alpha_list.append(tuple)

	x = 0
	len_alpha = len(alpha_list)

	if len_alpha == 0:
		return
	
	prefix_dict = dict()
	index = 0
	prefix_len = 0
	while index<len_alpha-1:
		nextIndex = index + 1
		if nextIndex<len_alpha:
			prefix = os.path.commonprefix([alpha_list[index][1], alpha_list[nextIndex][1]])
			if prefix not in prefix_dict:
				prefix_dict[prefix] = []

			prefix_dict[prefix].append(alpha_list[index][0])
			prefix_dict[prefix].append(alpha_list[nextIndex][0])

			prefix_len = len(prefix)

			# If prefix length is less than 3 letters
			if prefix_len < 3:
				keyword_len = len(alpha_list[index][1])
				prefix_index = 3
				if(prefix_index < keyword_len):
					sub_prefix = alpha_list[index][1][:prefix_index]
					if sub_prefix not in prefix_dict:
						prefix_dict[sub_prefix] = []

					prefix_dict[sub_prefix].append(alpha_list[index][0])
					prefix_dict[sub_prefix].append(alpha_list[index][0])

		nextIndex += 1
		index += 1

	# Do it once for the last index that does not loop through while
	if prefix_len < 3:
		keyword_len = len(alpha_list[index][1])
		prefix_index = 3
		if(prefix_index < keyword_len):
			sub_prefix = alpha_list[index][1][:prefix_index]
			if sub_prefix not in prefix_dict:
				prefix_dict[sub_prefix] = []

			prefix_dict[sub_prefix].append(alpha_list[index][0])
			prefix_dict[sub_prefix].append(alpha_list[index][0])

	sorted_prefix_dict = dict()
	tuple_list = []

	# Handle the case where only one element begins with the alphabet
	if len(prefix_dict) == 0:
		len_keyword = len(alpha_list[0][1])
		if len_keyword>1:
			half_len = int(len_keyword/2)
		else:
			half_len = 1
		data_tuple = (alpha_list[0][1][:half_len], alpha_list[0][0], alpha_list[0][0])
		tuple_list.append(data_tuple)

	# Sort the Prefix table
	else:
		for prefix in sorted(prefix_dict.keys()):
			sorted_prefix_dict[prefix] = prefix_dict[prefix]

		for prefix in sorted_prefix_dict:
			keyword_id_list = sorted(sorted_prefix_dict[prefix])
			data_tuple = (prefix, keyword_id_list[0], keyword_id_list[-1])
			tuple_list.append(data_tuple)

	connection=mysql.connect (host="localhost", user="root", password="Mydatabase", database="paperdb")
	cursor=connection.cursor()
	query = """	INSERT INTO paperdb.PrefixTable (Prefix, LowerKID, UpperKID) values (%s, %s, %s) """
	cursor.executemany(query, tuple_list)
	cursor.execute("COMMIT")

	cursor.close()


# Create Ngrams
def createNgrams():
	connection=mysql.connect (host="localhost", user="root", password="Mydatabase", database="paperdb")
	cursor=connection.cursor()
	cursor.execute("SELECT Prefix from paperdb.PrefixTable")
	prefix_list = cursor.fetchall()
	# N is the number grams allowed for search, limiting it to 2 or 3 (fix this comment)
	N = 3
	
	# print("Ngrams Table")
	for record in prefix_list:
		prefix = record[0]
		NgramList = []
		NgramSet = []
		NgramTupleList = []
		while len(prefix) >= N:
			data_tuple = tuple((record[0], prefix[:N]))
			NgramList.append(data_tuple)
			prefix = prefix[1:]

			NgramSet = set(NgramList)
			NgramTupleList = list(NgramSet)

		query = """	INSERT INTO paperdb.NgramsTable (Prefix, Ngram) values (%s, %s) """
		cursor.executemany(query, NgramTupleList)
		cursor.execute("COMMIT")

	cursor.execute("Select * from paperdb.NgramsTable")
	prefix_list = cursor.fetchall()

	cursor.close()
	

def TruncateTables():
	connection=mysql.connect (host="localhost", user="root", password="Mydatabase", database="paperdb")
	cursor=connection.cursor()
	cursor.execute("TRUNCATE paperdb.invertedindextable")
	cursor.execute("TRUNCATE paperdb.prefixtable")
	cursor.execute("TRUNCATE paperdb.ngramstable")
	cursor.close()


TruncateTables()
createAuxiliaryTables()
createNgrams()