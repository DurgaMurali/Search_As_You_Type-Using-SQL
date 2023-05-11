from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from search_functions import search_exact_index, search_fuzzy_gram, search_fuzzy_neighborhood
import fuzzy_search
import exact_search
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--populateTables", help="Populates the database tables",
                    action="store_true")
parser.add_argument("dbHost", help="The host IP of database connection")
parser.add_argument("dbUser", help="The username of database connection")
parser.add_argument("dbPassword", help="Password of database connection")
args = parser.parse_args()

if args.populateTables == True:
	print("Populating Tables")
	fuzzy_search.fuzzyTableFunctions(args.dbHost, args.dbUser, args.dbPassword)
	exact_search.exactTableFunctions(args.dbHost, args.dbUser, args.dbPassword)

root=Tk()
root.geometry("940x600+20+20")
root.configure(background='white')
root.title("Search As You Type")


#-------------- insert_button functionality -----------------------
def insert_record():
	title=title_entry.get()
	author=author_entry.get()
	booktitle=booktitle_entry.get()
	year=year_entry.get()
	if(title=="" or author=="" or booktitle=="" or year==""):
		MessageBox.showinfo("Insert Status", "All Fields are required")
	else:
		connection=mysql.connect(host=args.dbHost, user=args.dbUser, password=args.dbPassword, database="paperdb")
		cursor=connection.cursor()
		cursor.execute("INSERT INTO paperdb.dblp (Title, Authors, Booktitle, Year) VALUES('"+ title +"','"+ author +"','"+ booktitle +"','"+ year +"')")
		cursor.execute("COMMIT")

		#deleting enteries from the entry box
		title_entry.delete (0, 'end')
		author_entry.delete (0, 'end')
		booktitle_entry.delete (0, 'end')
		year_entry.delete (0, 'end')	
		
		MessageBox.showinfo("Insert Status", "Inserted Successfully")
		connection.close()


#-------------------Check funtion for search bar------------------
# Update entry box with listbox clicked
def fillout(event):
	# Delete whatever is in the entry box
	search_bar.delete(0, END)

	# Add clicked list item to entry box
	search_bar.insert(0, keyword_list.get(ANCHOR))
	

# Create function to check entry vs listbox
def check(e):
	# grab what was typed
	typed = search_bar.get()

	if typed == '':
		# data = ''
		keyword_list.delete(0,END)	
		for item in dbpl_table.get_children():
			dbpl_table.delete(item)
	else:
		if clicked.get() == options[0]:
			if(typed):
				search_bar.delete(0, END)
				keyword_list.delete(0,END)	
				MessageBox.showinfo("Incorrect Choice", "Please select an Algorithm!")		

		if clicked.get() == options[1]:
			# print("options[1] selected")
			search_exact_index(typed, dbpl_table,keyword_list, args.dbHost, args.dbUser, args.dbPassword)
		
		if clicked.get() == options[2]:
			# print("options[2] selected")
			search_fuzzy_gram(typed, dbpl_table,keyword_list, args.dbHost, args.dbUser, args.dbPassword)
		
		if clicked.get() == options[3]:
			# print("options[3] selected")
			search_fuzzy_neighborhood(typed, dbpl_table,keyword_list, args.dbHost, args.dbUser, args.dbPassword)	


#--------------------------- Creating the Edit Table bar --------------------------------------------
data_frame = LabelFrame(root, text="Edit Table")
data_frame.pack(fill="x", expand="yes", padx=20)
data_frame.place(x=20,y=20,width=900,height=70)

title_label = Label(data_frame, text="Title")
title_label.grid(row=0, column=0, padx=10, pady=10)
title_entry = Entry(data_frame)
title_entry.grid(row=0, column=1, padx=10, pady=10)

author_label = Label(data_frame, text="Author")
author_label.grid(row=0, column=2, padx=10, pady=10)
author_entry = Entry(data_frame)
author_entry.grid(row=0, column=3, padx=10, pady=10)

booktitle_label = Label(data_frame, text="BookTitle")
booktitle_label.grid(row=0, column=4, padx=10, pady=10)
booktitle_entry = Entry(data_frame)
booktitle_entry.grid(row=0, column=5, padx=10, pady=10)

year_label = Label(data_frame, text="Year")
year_label.grid(row=0, column=6, padx=10, pady=10)
year_entry = Entry(data_frame)
year_entry.grid(row=0, column=7, padx=10, pady=10)

insert_button = Button(data_frame, text=" Insert ",command=insert_record)
insert_button.grid(row=0, column=8, padx=10, pady=10)


# ------------------------ Creating the Search bar -------------------------------------------------
search_frame = LabelFrame(root, text="Search Record")
search_frame.pack(fill="x", expand="yes", padx=20)
search_frame.place(x=20,y=110,width=900,height=290)


# Dropdown menu 
options = ["Select Algorithm ... ", "Exact: Index-Based Method", "Fuzzy: Gram-Based Method", "Fuzzy: Levenshtein Distance"]
clicked = StringVar()
clicked.set(options[0])
dropdown_menu = OptionMenu(root, clicked, *options)
dropdown_menu.place(x=60,y=137,width=220,height=29)


#Search bar
search_bar = Entry()
search_bar.place(x=300,y=140,width=320,height=20)


# # Create a binding on the entry box
search_bar.bind("<KeyRelease>", check)


# Create a listbox
keyword_list = Listbox(root, width=50)
keyword_list.place(x=300,y=180,width=320,height=200)


# Create a binding on the listbox onclick
keyword_list.bind("<<ListboxSelect>>", fillout)


# ------------------- view --------------------------------
table_frame = LabelFrame(root, text="Matched Records")
table_frame.pack(fill="x", expand="yes", padx=20)
table_frame.place(x=20,y=410,width=900,height=180)
# Add a Treeview widget
dbpl_table = ttk.Treeview(table_frame, column=("Title", "Author", "BookTitle", "Year"), show='headings', height=8)
dbpl_table.column("# 1", anchor=CENTER)
dbpl_table.heading("# 1", text="Title")
dbpl_table.column("# 2", anchor=CENTER)
dbpl_table.heading("# 2", text="Author")
dbpl_table.column("# 3", anchor=CENTER)
dbpl_table.heading("# 3", text="BookTitle")
dbpl_table.column("# 4", anchor=CENTER)
dbpl_table.heading("# 4", text="Year")

dbpl_table.pack()
root.mainloop()

