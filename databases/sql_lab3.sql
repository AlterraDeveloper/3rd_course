use UNIVER;

ALTER TABLE Employees ADD department int;

update Employees set department = 1 where codeid%2 = 0;  
update Employees set department = 2 where codeid%2 != 0; 
--TODO добавить новых сотрудников в отдел 3 и добавить еще записей в разные отделы

--I.	  Операторы DML

--1.	Перевести в отдел 1 всех сотрудников 3-его отдела, заработная плата которых не превышает 300 у.е.,
update Employees set department = 1
where department = 3 and salary <=30000;
--а в отдел 2 перевести  всех сотрудников 3-его отдела, заработная плата которых превышает 300 у.е;
update Employees set department = 2
where department = 3 and salary >= 300;

--2.	Увеличить на 100 у.е. заработную плату сотрудников 1-ого отдела, родившихся в 1985г. 
update Employees set salary = salary + 100 
where department = 1 and year(date_of_bitrh) = 1985;

--3.	Удалить все записи, соответствующие сотрудникам 2-ого отдела с заработной платой, превышающей 450 у.е.
delete from Employees where department = 2 and salary > 45000;

--4.	Удалить все строки из таблицы Сотрудники,  используя оператор TRUNCATE.
truncate table Employees;


--II.	Создание  и удаление индексов
 
--1.	Создать индекс по полям [Номер отдела] и [ФИО сотрудника] в табл. Сотрудники
create index dep_no_and_fio_emp ON Employees (department,fio_employee);
--2.	Создать индекс на уникальность [Наименование страны] в табл. Страны.
create UNIQUE index unique_country ON Countries(country_name);
--3.	Создать индекс на уникальность города в пределах одной страны.
create unique index unique_city_in_country ON Cities(city_name,country_id);
--4.	Удалить индекс по полям [Номер отдела] и [ФИО сотрудника]
drop index Employees.dep_no_and_fio_emp;



