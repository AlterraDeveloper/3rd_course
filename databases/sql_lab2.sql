--use UNIVER;

--CREATE TABLE Countries
--(codeid int PRIMARY KEY NOT NULL IDENTITY(1,1),
--country_name nvarchar(50) NOT NULL);

--CREATE TABLE Cities
--(
--	codeid int PRIMARY KEY NOT NULL IDENTITY(1,1),
--	city_name nvarchar(50) NOT NULL,
--	country_id int NOT NULL

--CONSTRAINT FK_Cities_to_Countries FOREIGN KEY (country_id) 
--REFERENCES Countries(codeid)
--);

--ALTER TABLE Cities  
--ADD CONSTRAINT UniqueCityInCountry 
--UNIQUE (city_name , country_id);

--CREATE TABLE Employees
--(
--codeid int PRIMARY KEY NOT NULL IDENTITY(1,1),
--fio_employee nvarchar(50) not null,
--date_of_bitrh date,
--salary int not null,
--city_id int not null,
--CONSTRAINT FK_Employees_to_Cities FOREIGN KEY (city_id) REFERENCES Cities(codeid),
--CONSTRAINT CheckSalary CHECK (salary >= 200)
--); 

--ALTER TABLE Employees ADD is_married bit not null default 0;

--ALTER TABLE Employees DROP CONSTRAINT IF EXISTS CheckSalary;
--ALTER TABLE Employees ADD CONSTRAINT CheckSalary CHECK (salary>=200 and salary<=50000);

--ALTER TABLE Employees ADD CONSTRAINT UnigueFIOandBirth UNIQUE(date_of_bitrh,fio_employee);

--ALTER TABLE Employees ADD CONSTRAINT LowBoundForBirth CHECK (YEAR(date_of_bitrh)>=1950);