CREATE DATABASE ofdb;
use ofdb;

create table Biblioteca(
  bookid int,
  Nome varchar(25),
  Autor varchar(25),
  Ano varchar(25),
  genero varchar(25)
);

insert into Biblioteca(bookid,Nome,Autor,Ano,genero) 
values 
(1,"Frankenstein","Victor","1867","Horror"),
(2,"Frankenstein","annne","1869","Horror");

select * from Biblioteca;