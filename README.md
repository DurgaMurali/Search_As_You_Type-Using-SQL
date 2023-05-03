# Search As You Type Using SQL

Search-as-you-type (SAYT) has become an essential feature for online marketplaces, search engines, recommendation systems, etc., as it improves user engagement and helps users find relevant information quickly. SAYT or autocomplete predicts the search key in real time while users type their search queries. Many applications like Google, Amazon, Netflix, etc. offer this feature to help customers find their search results quickly and easily. Typically, applications use an extra layer on top of a database to create indexes and algorithms for predicting search terms. Although this approach is efficient, it results in duplicated data and increased hardware expenses. While some relational databases, such as Oracle and SQL Server, offer prefix search capabilities, it is not widely used. Database extensions, such as Informix Data Blades and DB2 extenders, are available to expand a database's functionality, but they are known to cause reliability and security issues and are not easily transferable across different vendor databases. Therefore, a better solution is to implement autocomplete using SQL, which is a portable query language that can be used across different databases. 

Our aim is to implement the solution presented in the paper, which utilizes the full potential of the query engine and auxiliary tables to improve search performance.

## Getting Started

### Pre-requisites
* Python and pip (latest version)
* MySQL Workbench (latest version)

### Installing

```
pip install tkinter
pip install mysql-connector-python
```

### Executing program
Run the main.py file
```
python main.py
```

## Authors

Charul Rathore and Durga Muralidharan 


## Acknowledgments

Reference Paper
* [Supporting Search-As-You-Type Using SQL in Databases](https://ieeexplore.ieee.org/abstract/document/5936070?casa_token=5B3wtSLJYogAAAAA:fUUrfiPFc-oxgxxS_F5KC63TleGnYyx0Q-jrpLQC1im2SEimM3dyN93ihuPHjLsJdSxxZcIjZA)
