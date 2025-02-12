show databases;

use vit;

show tables from vit;

select * from cse;
insert into cse values (1002,'Isha',78);
insert into cse values (1011,'Sid',85,'UK');

desc cse;

ALTER TABLE cse DROP COLUMN s_contact;
ALTER TABLE cse ADD(
    s_country varchar(25) DEFAULT 'India'
);
use vit;
ALTER TABLE cse RENAME column 
    s_country TO s_state;
desc cse;

select * from cse;

delete from cse where s_id=1002;

insert into cse values (1002,'Varun',75,'India'),(1003,'Neeraj',85,'India');

UPDATE cse SET s_name='Rohan' WHERE s_id=1002;

UPDATE cse SET s_mark = s_mark+1; 
use vit;
select s_id,S_name from cse where s_id=1002;
use org123;
CREATE TABLE Employees (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Age int
);
desc Employees;

ALTER TABLE Employees
MODIFY Age int NOT NULL;

CREATE TABLE Staff (
    ID int primary key,
    LastName varchar(255) NOT NULL unique,
    FirstName varchar(255) NOT NULL unique,
    Age int
);
desc Staff;

use org123;

create table inventory(
c_id int primary key,
c_name varchar(25) not null unique,
c_decrp varchar(250) not null
);

insert into inventory values (102, 'furnitures', 'it stores all set of wooden items');
select * from inventory;
desc inventory;

use org123;
CREATE TABLE Items (
    P_ID int primary key,
    p_Name varchar(250) NOT NULL,
    c_id int ,
    CONSTRAINT c_id FOREIGN KEY (c_id)
    REFERENCES inventory(c_id)
);
show tables from org123;
desc Items;

drop table Items;

insert into Items values (904, 'Wooden table', null);
select * from Items;


select * from inventory;

delete from inventory where c_id=101;

drop table inventory;




CREATE TABLE Course (
    cno INT PRIMARY KEY,
    cname VARCHAR(20)
);
select * from Course;
INSERT INTO Course(cno, cname) 
 VALUES(101,'c'),
       (102,'c++'),
       (103,'DBMS');

CREATE TABLE Enrollment (
    sno INT,
    cno INT,
    jdate date,
    PRIMARY KEY(sno),
    FOREIGN KEY(cno) 
        REFERENCES Course(cno)
        ON DELETE CASCADE
);
INSERT INTO Enrollment(sno,cno,jdate) 
 VALUES(2, 105, "2021/05/05");
select * from Enrollment;
desc Enrollment;

create database saturday;
use saturday;

create table inventory(
c_id int primary key,
c_name varchar(25) not null unique,
c_decrp varchar(250) not null
);

insert into inventory values (101, 'electronics', 'it stores all set of electronics items');
select * from inventory;
desc inventory;

CREATE TABLE Items (
    P_ID int primary key,
    p_Name varchar(250) NOT NULL,
    c_id int ,
    CONSTRAINT c_id FOREIGN KEY (c_id)
    REFERENCES inventory(c_id) on delete cascade
);

insert into Items values (904, 'INTEL I5 Processor', 101);
select * from Items;
delete from inventory where c_id=101;
select * from inventory;


CREATE TABLE Employees (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (salary>=200000 and salary <=400000)
);


ALTER TABLE Employees	
ADD CHECK (Age>=18);

CREATE TABLE Staff (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255) DEFAULT 'Coimbatore'
);
desc Staff;

use org123;
show tables from org123;

select * from worker;

SELECT * FROM worker WHERE salary LIKE '8%';
use org123;
create view admin_more_salary as 
select * from worker 
where department='Admin' and salary > 100000 order by salary desc;

select * from admin_more_salary;

select department, count(department) from worker 
where department in ('admin','account') group by department;

SELECT department, COUNT(department) as highest_head_count
FROM worker
GROUP BY department
HAVING COUNT(department) >= 3;

create table vitBhopal (id int primary key, name varchar(20) not null,
department varchar(25) not null);
insert into vitbhopal values (104,'Karthik','cs'),(103,'Arun','cs');

create table vit (id int primary key, name varchar(20) not null,
college varchar(25) not null);
insert into vit values (104,'Karthik','chennai'),(103,'Arun','bhopal');
select * from vit;

select * from vitbhopal;

select name as WinnerOfTheYear from vitbhopal
where id = (select id from vit where college='bhopal');

use org123;
drop table student;
create table student(
s_id int primary key,
s_name varchar(25) not null,
s_department varchar(25) not null
);

insert into student values (1001,"Akhil","ECE"),(1002,"Madhav","CSE"),(1003,"Kunal","Mech"),(1006,'Rajiv','Aero'),(1007,"Manish","Civil");

select * from student;
drop table vit;
create table VIT(
s_id int primary key,
s_cgpa varchar(5) not null
);
insert into vit values (1001,'7.2'),(1002,'8.6'),(1007,'9.25');
select * from vit;
use org123;

select * from student cross join vit;

SELECT * from student INNER JOIN vit where student.s_id = vit.s_id;

SELECT * FROM student full outer JOIN vit ON (student.s_id = vit.s_id);
