use UNIVER;

--ALTER TABLE Employees ADD department int;

--update Employees set department = 1 where codeid%2 = 0; --Выполнено 
--update Employees set department = 2 where codeid%2 != 0; --Выполнено
--TODO добавить новых сотрудников в отдел 3 и добавить еще записей в разные отделы

--Перевести в отдел 1 всех сотрудников 3-его отдела, заработная плата которых не превышает 300
update Employees set department = 1
where department = 3 and salary <=300;


--в отдел 2 перевести  всех сотрудников 3-его отдела, заработная плата которых превышает 300
update Employees set department = 2
where department = 3 and salary >= 300;
