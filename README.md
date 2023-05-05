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
1. Run all the queries from db_scripts.sql file to create schema in MySQL Workbench
2. Run the exact_search.py and fuzzy_search.py to populate the schemas 
```
python exact_search.py
python fuzzy_search.py
```
3. Run the main.py file to test the search features
```
python main.py
```

## Authors

Charul Rathore and Durga Muralidharan 


## Acknowledgments

Reference Paper
* [Supporting Search-As-You-Type Using SQL in Databases](https://ieeexplore.ieee.org/abstract/document/5936070?casa_token=5B3wtSLJYogAAAAA:fUUrfiPFc-oxgxxS_F5KC63TleGnYyx0Q-jrpLQC1im2SEimM3dyN93ihuPHjLsJdSxxZcIjZA)
