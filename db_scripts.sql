-- Database name: PaperDB

-- "dblp" contains all the records on which the search feature will be tested.
CREATE TABLE paperdb.dblp ( 
    RecordID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Title varchar(255) NOT NULL,
    Authors varchar(1000) NOT NULL,
    Booktitle varchar(255) NOT NULL,
    Year int NOT NULL
);

-- "KeywordTable" contains all the keywords picked from dblp records
create table paperdb.KeywordTable (
KeywordID int PRIMARY KEY NOT NULL,
Keyword varchar(255));


-- Auxiliary Tables 
-- Inverted Index Table used for Exact Search
CREATE TABLE paperdb.exactinvertedindextable (
KeywordID int,
RecordID int,
PRIMARY KEY (KeywordID, RecordID)
);

-- Inverted Index Table used for Fuzzy Search
create table paperdb.InvertedIndexTable (
KeywordID int,
RecordID int,
PRIMARY KEY (KeywordID, RecordID)
);

-- Prefix Table used for Exact Search
CREATE TABLE paperdb.exactPrefixTable (
Prefix varchar(255),
LowerKID int,
UpperKID int,
PRIMARY KEY (Prefix, LowerKID, UpperKID)
);

-- Prefix Table used for Fuzzy Search
create table paperdb.PrefixTable (
Prefix varchar(255),
LowerKID int,
UpperKID int,
PRIMARY KEY (Prefix, LowerKID, UpperKID)
);

-- Ngrams Table used for fuzzy and Levenshtein Distance Search
create table paperdb.NgramsTable (
Prefix varchar(255),
Ngram varchar(10),
PRIMARY KEY (Prefix, Ngram)
);


-- Indexes created to improve performance
create index ngramIndex on paperdb.NgramsTable (Ngram, Prefix);
create index invertedRecordIDIndex on paperdb.InvertedIndexTable (RecordID);
create index keywordIndex on paperdb.KeywordTable (KeywordID);
create index PrefixIndex on paperdb.PrefixTable (Prefix);
create index ExactPrefixIndex on paperdb.exactPrefixTable (Prefix);
create index ExactinvertedRecordIDIndex on paperdb.exactInvertedIndexTable (RecordID);