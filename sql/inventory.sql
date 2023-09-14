show databases;
use inventory;
show tables;
create table products(
ID int primary key auto_increment, P_NAME varchar(30) , QUANTITY int);
desc products;

create table locations(
ID int primary key auto_increment not null, NAME varchar(30));

create table transfers(
ID int primary key auto_increment not null, FROM_L varchar(30), TO_L varchar(30),PRODUCT varchar(30) , QUANTITY int);

desc transfers;