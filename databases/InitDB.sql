CREATE DATABASE SPORT_ADMIN;

USE SPORT_ADMIN;

CREATE TABLE Services(
	ServiceId INT PRIMARY KEY CLUSTERED IDENTITY(1,1),
	ServiceName NVARCHAR(50) NOT NULL,
	ServiceStartTime TIME NOT NULL,
	ServiceEndTime TIME NOT NULL,
	IsOnMonday BIT NOT NULL,
	IsOnTuesday BIT NOT NULL,
	IsOnWednesday BIT NOT NULL,
	IsOnThursday BIT NOT NULL,
	IsOnFriday BIT NOT NULL,
	IsOnSaturday BIT NOT NULL,
	Price INT NOT NULL,
	Quantity TINYINT NOT NULL
);

CREATE TABLE Clients(
	ClientId INT PRIMARY KEY CLUSTERED IDENTITY(1,1),
	LastName NVARCHAR(50) NOT NULL,
	FirstName NVARCHAR(50) NOT NULL,
	MiddleName NVARCHAR(50),
	Sex BIT NOT NULL,
	MobilePhone NVARCHAR(50)
);

CREATE TABLE Abonements(
	AbonementId INT PRIMARY KEY CLUSTERED IDENTITY(1,1),
	ClientId INT NOT NULL REFERENCES Clients(ClientId),
	ServiceId INT NOT NULL REFERENCES Services(ServiceId),
	AbonementStartDate DATE NOT NULL,
	AbonementEndDate DATE NOT NULL,
	TrainingsRemain TINYINT NOT NULL,
	IsActive BIT NOT NULL
);

CREATE TABLE Payments(
	PaymentId INT PRIMARY KEY CLUSTERED IDENTITY(1,1),
	Amount INT NOT NULL,
	AbonementId INT NOT NULL REFERENCES Abonements(AbonementId),
	DateOfPayment DATETIME NOT NULL
);

GO
CREATE PROCEDURE GymMargin @start_date date, @end_date date
AS
SELECT 
	s.ServiceName,
	sum(p.Amount)
from Payments[p] 
	inner join Abonements[a] ON a.AbonementId = p.AbonementId
	inner join dbo.Services[s] ON s.ServiceId = a.ServiceId
	where convert(date,p.DateOfPayment) >= @start_date and convert(date,p.DateOfPayment) <= @end_date 
	group by s.ServiceName	
GO

CREATE PROCEDURE GetClientServices @client_id int,@start_date date, @end_date date
AS
SELECT 
	c.LastName,
	c.FirstName,
	s.ServiceName,
	count(a.AbonementId)
FROM Abonements[a]
inner join Services[s] ON a.ServiceId = s.ServiceId
inner join Clients[c] ON c.ClientId = a.ClientId
where a.ClientId = @client_id and convert(date,a.AbonementStartDate) >= @start_date and convert(date,a.AbonementStartDate) <= @end_date
group by c.LastName,c.FirstName,s.ServiceName;
GO

CREATE PROCEDURE GetActiveAbonemets @start_date date, @end_date date
AS
SELECT 
	c.LastName,
	c.FirstName,
	a.AbonementStartDate,
	a.AbonementEndDate,
	s.ServiceName
FROM Abonements[a]
	inner join Services[s] ON a.ServiceId = s.ServiceId
	inner join Clients[c] ON c.ClientId = a.ClientId
where convert(date,a.AbonementStartDate) >= @start_date and convert(date,a.AbonementStartDate) <= @end_date and a.IsActive = 1
group by c.LastName,c.FirstName,s.ServiceName;
GO
