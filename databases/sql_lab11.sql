USE UNIVER;
GO
--1.1	Cоздать функцию, определяющую для заданного месяца заданного года 
--максимальный объем поставки одним внешним поставщиком;

DROP FUNCTION IF EXISTS ufn_MaxVolumeOfExternalProvider;
GO
CREATE FUNCTION ufn_MaxVolumeOfExternalProvider(@month int,@year int)
RETURNS real
AS
BEGIN
DECLARE @maxVolume real;
SET @maxVolume =
(
SELECT TOP 1 
		'Объем' = SUM(skl.Количество*skl.Цена)
FROM dbo.Склад AS skl 
JOIN dbo.Поставщики AS p ON skl.КодПоставщика = p.КодПоставщика
WHERE 
	skl.ПризнакДвижения = 'Поступление'
	AND  skl.КодПоставщика != 21
	AND skl.КодПоставщика IS NOT NULL
	AND YEAR(skl.Датадвижения) = @year
	AND MONTH(skl.Датадвижения) = @month
GROUP BY p.НаимПоставщика
ORDER BY Объем desc
)
RETURN (@maxVolume) 
END
GO

--1.2 Cоздать функцию, определяющую для заданного месяца заданного года 
--наименование самого эффективного внешнего поставщика (см. предыдущий пункт);

DROP FUNCTION IF EXISTS ufn_NameOfMostEfficientProvider;
GO
CREATE FUNCTION ufn_NameOfMostEfficientProvider(@month int,@year int)
RETURNS nvarchar(50)
AS
BEGIN
DECLARE @providerName nvarchar(50);
SET @providerName =
(
SELECT TOP 1 
		p.НаимПоставщика
FROM dbo.Склад AS skl 
JOIN dbo.Поставщики AS p ON skl.КодПоставщика = p.КодПоставщика
WHERE 
	skl.ПризнакДвижения = 'Поступление'
	AND  skl.КодПоставщика != 21
	AND skl.КодПоставщика IS NOT NULL
	AND YEAR(skl.Датадвижения) = @year
	AND MONTH(skl.Датадвижения) = @month
GROUP BY p.НаимПоставщика
ORDER BY SUM(skl.Количество*skl.Цена) desc
)

RETURN (@providerName) 
END
GO

--1.3	Cоздать функцию, определяющую для заданного месяца заданного года состав поставщиков, 
--обеспечивших поставку сырья заданного типа с объемом в денежном выражении не меньше заданного. 
--Выводимая информация должна содержать данные о коде поставщика, его наименовании  и объеме поставки.

DROP FUNCTION IF EXISTS ufn_Providers;
GO
CREATE FUNCTION ufn_Providers(@month int,@year int,@type nvarchar(50),@amount real)
RETURNS TABLE
AS
RETURN (
SELECT 
	skl.КодПоставщика,
	p.НаимПоставщика,
	'Объем' = SUM(skl.Цена*skl.Количество)
FROM dbo.Склад AS skl 
JOIN dbo.Поставщики AS p ON skl.КодПоставщика = p.КодПоставщика
JOIN dbo.Сырье AS s ON skl.КодСырья = s.КодСырья
JOIN dbo.Типы_сырья AS ts ON s.КодТипаСырья = ts.КодТипаСырья
WHERE
	skl.ПризнакДвижения = 'Поступление'
	AND skl.КодПоставщика IS NOT NULL
	AND YEAR(skl.Датадвижения) = @year
	AND MONTH(skl.Датадвижения) = @month
	AND ts.НаимТипаСырья = @type
GROUP BY skl.КодПоставщика,p.НаимПоставщика
HAVING SUM(skl.Цена*skl.Количество) >= @amount
)
GO

--2.1 Создать пакет для определения максимального объема поставки одним внешним поставщиком в июле 2002 года;
SELECT dbo.ufn_MaxVolumeOfExternalProvider(7,2002);
--2.2 Создать пакет для определения наименования самого эффективного внешнего поставщика в июле 2002 года;
SELECT dbo.ufn_NameOfMostEfficientProvider(7,2002);
--2.3 Создать пакет для определения состава поставщиков, обеспечивших поставку напитков
--в июле 2002 года объемом не менее. Выводимая информация должна быть сортирована по наименованиям поставщиков.
SELECT * FROM dbo.ufn_Providers(7,2002,'Напитки',5000) ORDER BY НаимПоставщика;
GO


