CREATE DATABASE SchoolDB;

use SchoolDB;
CREATE TABLE Students(
StudentID int,
ID varchar(25),
PrimeiroNome varchar(25),
SegundoNome varchar(25)
);
CREATE TABLE Courses(
CoursesID int,
Nome varchar(30),
Unidade varchar(2)
);
INSERT INTO Students(StudentID,PrimeiroNome,SegundoNome)
VALUES
(1,"Pedro","Guimarães"),
(2,"Ronaldo","Fenomeno");
INSERT INTO Courses(CoursesID,Nome,Unidade)
VALUES
(1,"Data_Engineering","T1"),
(1,"Software_Engineering","T2");
select*from Students


 
