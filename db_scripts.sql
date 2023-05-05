CREATE TABLE paperdb.dblp ( 
	RecordID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Title varchar(255) NOT NULL,
    Authors varchar(255) NOT NULL,
    Booktitle varchar(255) NOT NULL,
    Year int NOT NULL
);

insert into paperdb.dblp (Title, Authors, Booktitle, Year) values ("K-Automorphism: A General Framework For Privacy Preserving Network Publication",
"Lei Zou, Lei Chen, M. Tamer Ozsu", "PVLDB", 2009);

insert into paperdb.dblp (Title, Authors, Booktitle, Year) values ("Privacy-Preserving Singular Value Decomposition",
"Shuguo Han, Wee Keong Ng, Philip S. Yu", "ICDE", 2009);

insert into paperdb.dblp (Title, Authors, Booktitle, Year) values ("Privacy-Preservation of Aggregates in Hidden Databases: Why and How?",
"Arjun Dasgupta, Nan Zhang, Gautam Das, Surajit Chaudhuri", "SIGMOD", 2009);

insert into paperdb.dblp (Title, Authors, Booktitle, Year) values ("Privacy-Preserving Indexing of Documents on the Network",
"Mayank Bawa, Roberto J. Bayardo, Rakesh Agarwal, Jaideep Vaidya", "VLDBJ", 2009);

insert into paperdb.dblp (Title, Authors, Booktitle, Year) values ("On Anti-Corruption Privacy Preserving Publication",
"Yufei Tao, Xiaokui Xiao, Jiexing Li, Donghui Zhang", "ICDE", 2008);


insert into paperdb.dblp (Title, Authors, Booktitle, Year) values ("Preservation of Proximity Privacy in Publishing Numerical Sensitive Data",
"Jiexing Li, Yufei Tao, Xiaokui Xiao", "SIGMOD", 2008);

insert into paperdb.dblp (Title, Authors, Booktitle, Year) values ("Hiding in the Crowd: Privacy Preservation on Evolving Streams through Correlation Tracking",
"Feifei Li, Jimeng Sun, Spiros Papadimitriou, George A. Mihaila, Ioana Stanoi", "ICDE", 2007);

insert into paperdb.dblp (Title, Authors, Booktitle, Year) values ("The Boundary Between Privacy and Utility in Data Publishing",
"Vibhor Rastogi, Sungho Hong, Dan Suciu", "VLDB", 2007);


insert into paperdb.dblp (Title, Authors, Booktitle, Year) values ("Privacy Protection in Personalized Search",
"Xuehua Shen, Bin Tan, ChengXiang Zhai", "SIGIR", 2007);

insert into paperdb.dblp (Title, Authors, Booktitle, Year) values ("Privacy in Database Publishing",
"Alin Deutsch, Yannis Papakonstantinou", "ICDT", 2005);

select * from paperdb.dblp;

drop table paperdb.KeywordTable

create table paperdb.KeywordTable (
KeywordID int PRIMARY KEY NOT NULL,
Keyword varchar(255))


insert into paperdb.KeywordTable values (1, "PVLDB")

insert into paperdb.KeywordTable values (2, "K-Automorphism")

insert into paperdb.KeywordTable values (3, "Framework")

insert into paperdb.KeywordTable values (4, "Privacy")

insert into paperdb.KeywordTable values (5, "Preserving")

insert into paperdb.KeywordTable values (6, "Network")

insert into paperdb.KeywordTable values (7, "Publication")

insert into paperdb.KeywordTable values (8, "Singular")

insert into paperdb.KeywordTable values (9, "Decomposition")

insert into paperdb.KeywordTable values (10, "ICDE")

insert into paperdb.KeywordTable values (11, "Indexing")

insert into paperdb.KeywordTable values (12, "Documents")

insert into paperdb.KeywordTable values (13, "VLDBJ")

insert into paperdb.KeywordTable values (14, "Aggregates")

insert into paperdb.KeywordTable values (15, "Hidden")

insert into paperdb.KeywordTable values (16, "Databases")

insert into paperdb.KeywordTable values (17, "SIGMOD")

insert into paperdb.KeywordTable values (18, "Anti-Corruption")

insert into paperdb.KeywordTable values (19, "Preservation")

insert into paperdb.KeywordTable values (20, "Proximity")

insert into paperdb.KeywordTable values (21, "Numerical")

insert into paperdb.KeywordTable values (22, "Sensitive")

insert into paperdb.KeywordTable values (23, "Hiding")

insert into paperdb.KeywordTable values (23, "Crowd")

insert into paperdb.KeywordTable values (24, "Evolving")

insert into paperdb.KeywordTable values (25, "Streams")

insert into paperdb.KeywordTable values (26, "Correlation")

insert into paperdb.KeywordTable values (27, "Tracking")

insert into paperdb.KeywordTable values (28, "Boundary")

insert into paperdb.KeywordTable values (29, "Utility")

insert into paperdb.KeywordTable values (30, "VLDB")

insert into paperdb.KeywordTable values (31, "Protection")

insert into paperdb.KeywordTable values (32, "Protection")

insert into paperdb.KeywordTable values (33, "Personalized")

insert into paperdb.KeywordTable values (34, "SIGIR")

insert into paperdb.KeywordTable values (35, "ICDT")


drop table paperdb.NgramsTable

create table paperdb.NgramsTable (
Prefix varchar(255),
Ngram varchar(10),
PRIMARY KEY (Prefix, Ngram)
)

create table paperdb.InvertedIndexTable (
KeywordID int,
RecordID int,
PRIMARY KEY (KeywordID, RecordID)
)

drop table paperdb.InvertedIndexTable

create table paperdb.PrefixTable (
Prefix varchar(255),
LowerKID int,
UpperKID int,
PRIMARY KEY (Prefix, LowerKID, UpperKID)
)

create table paperdb.NeighborhoodDeletionTable (
Prefix varchar(255),
iDeletedString varchar(255),
iDeletion int,
PRIMARY KEY (Prefix, iDeletedString, iDeletion)
)
