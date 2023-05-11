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
pip install rake-nltk
```

### Executing program
1. Run all the queries from *db_scripts.sql* file to create schemas in MySQL Workbench. You can use the Edit table section of UI to populate original *DBPL prototype table*.
2. To get information about command-line parameters please use *--help* option as shown below.
```
python main.py --help
```
3. In order to populate tables from the *DBLP2.csv* file and also execute the search functionality, 4 command-line parameters are to be passed as shown below.
```
python main.py --populateTables hostIP username password
```
```
--populateTables - Populates the database tables
hostIP           - The host IP of database connection
username         - The username of database connection
password         - Password of database connection
For example, python main.py --populateTables localhost root Mydata@123
```
4. In order to only execute the search functionality without populating database tables, 3 command-line parameters are to be passed as shown below. 
```
python main.py hostIP username password
```
5. If a set of new records are inserted using UI, then step 3 needs to be excuted again as well to populate the information of new record in auxiliary tables.
## Authors

1. Charul Rathore [45% code, 45% report and presentation]  
2. Durga Muralidharan [45% code, 45% report and presentation]
3. Swati SVM [10% code, 10% report and presentation]


## Acknowledgments

Reference Paper
* [Supporting Search-As-You-Type Using SQL in Databases](https://ieeexplore.ieee.org/abstract/document/5936070?casa_token=5B3wtSLJYogAAAAA:fUUrfiPFc-oxgxxS_F5KC63TleGnYyx0Q-jrpLQC1im2SEimM3dyN93ihuPHjLsJdSxxZcIjZA)
