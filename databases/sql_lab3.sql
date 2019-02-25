use UNIVER;

ALTER TABLE Employees ADD department int;

update Employees set department = 1 where codeid%2 = 0;  
update Employees set department = 2 where codeid%2 != 0; 
--TODO �������� ����� ����������� � ����� 3 � �������� ��� ������� � ������ ������

--I.	  ��������� DML

--1.	��������� � ����� 1 ���� ����������� 3-��� ������, ���������� ����� ������� �� ��������� 300 �.�.,
update Employees set department = 1
where department = 3 and salary <=30000;
--� � ����� 2 ���������  ���� ����������� 3-��� ������, ���������� ����� ������� ��������� 300 �.�;
update Employees set department = 2
where department = 3 and salary >= 300;

--2.	��������� �� 100 �.�. ���������� ����� ����������� 1-��� ������, ���������� � 1985�. 
update Employees set salary = salary + 100 
where department = 1 and year(date_of_bitrh) = 1985;

--3.	������� ��� ������, ��������������� ����������� 2-��� ������ � ���������� ������, ����������� 450 �.�.
delete from Employees where department = 2 and salary > 45000;

--4.	������� ��� ������ �� ������� ����������,  ��������� �������� TRUNCATE.
truncate table Employees;


--II.	��������  � �������� ��������
 
--1.	������� ������ �� ����� [����� ������] � [��� ����������] � ����. ����������
create index dep_no_and_fio_emp ON Employees (department,fio_employee);
--2.	������� ������ �� ������������ [������������ ������] � ����. ������.
create UNIQUE index unique_country ON Countries(country_name);
--3.	������� ������ �� ������������ ������ � �������� ����� ������.
create unique index unique_city_in_country ON Cities(city_name,country_id);
--4.	������� ������ �� ����� [����� ������] � [��� ����������]
drop index Employees.dep_no_and_fio_emp;



