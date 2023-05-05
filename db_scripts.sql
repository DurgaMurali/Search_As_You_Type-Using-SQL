CREATE TABLE paperdb.dblp ( 
    RecordID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Title varchar(255) NOT NULL,
    Authors varchar(255) NOT NULL,
    Booktitle varchar(255) NOT NULL,
    Year int NOT NULL
);

create table paperdb.KeywordTable (
KeywordID int PRIMARY KEY NOT NULL,
Keyword varchar(255));

create table paperdb.InvertedIndexTable (
KeywordID int,
RecordID int,
PRIMARY KEY (KeywordID, RecordID)
);

create table paperdb.PrefixTable (
Prefix varchar(255),
LowerKID int,
UpperKID int,
PRIMARY KEY (Prefix, LowerKID, UpperKID)
);

create table paperdb.NgramsTable (
Prefix varchar(255),
Ngram varchar(10),
PRIMARY KEY (Prefix, Ngram)
);

create table paperdb.NeighborhoodDeletionTable (
Prefix varchar(255),
iDeletedString varchar(255),
iDeletion int,
PRIMARY KEY (Prefix, iDeletedString, iDeletion)
);

