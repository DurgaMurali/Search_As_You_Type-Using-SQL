# Search As You Type Using SQL

Search-as-you-type has become an essential feature for online marketplaces, search engines, recommendation systems, etc., as it improves user engagement and helps users find relevant information quickly. Search-as-you-type or autocomplete predicts the search key in real time while users type their search queries. Many applications like Google, Amazon, Netflix, etc. offer this feature to help customers find their search results quickly and easily.

Our aim is to implement the prototype solution presented in the paper, which utilizes the full potential of the query engine and auxiliary tables to improve search performance.

## Getting Started

### Pre-requisites
* Python and pip 
* MySQL Workbench 

### Installing

```
pip install tkinter
pip install mysql-connector-python
pip install python-Levenshtein
```

### Executing program
1. Run all the queries from *db_scripts.sql* file to create schemas in MySQL Workbench. You can use the Edit table section of UI to populate original *DBPL prototype table* or use the queries mentioned in *db_scripts.sql*
2. Run the exact_search.py and fuzzy_search.py to populate the schemas created in step 1.
```
python exact_search.py
python fuzzy_search.py
```
3. Update 'host', 'user', 'password' with your credentials in all the statements - *mysql.connect(host="localhost", user="root", password="Mydatabase", database="paperdb")* in *main.py* file.
4. Run the main.py file to test the search features in the UI. 
```
python main.py
```
5. If a set of new records are inserted using UI, then step 2. need to be excuted again as well to populate the information of new record in auxillary tables. 
## Authors

Charul Rathore and Durga Muralidharan 


## Acknowledgments

Reference Paper
* [Supporting Search-As-You-Type Using SQL in Databases](https://ieeexplore.ieee.org/abstract/document/5936070?casa_token=5B3wtSLJYogAAAAA:fUUrfiPFc-oxgxxS_F5KC63TleGnYyx0Q-jrpLQC1im2SEimM3dyN93ihuPHjLsJdSxxZcIjZA)
