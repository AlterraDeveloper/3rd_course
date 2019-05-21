USE Boreas1;
GO
--1.1	Создать процедуру для вывода данных (Марка, Цена, НаСкладе) о товарах заданного типа. 
--Сортировать данные по марке товаров. Предусмотреть возможность задания типа товаров по умолчанию, 
--а также диагностики (с использованием оператора Return) ситуации, когда товаров заданного типа не существует;

DROP PROC IF EXISTS usp_GoodsOfType;
GO
CREATE PROC usp_GoodsOfType 
	@typeOfGood nvarchar(25) = 'Напитки'
AS
SET NOCOUNT ON; 
BEGIN
	DECLARE @error nvarchar(50);
	SET @error = ''; 
	IF (SELECT COUNT(*) FROM dbo.Типы WHERE Категория = @typeOfGood) = 0
		BEGIN
			SET @error = 'Товаров с типом "' + @typeOfGood + '" не существует';
			SELECT @error AS 'Текст ошибки';
		END
	ELSE
		BEGIN
		SELECT 
			t.Марка,
			t.Цена,
			t.НаСкладе
		FROM dbo.Товары AS t
		JOIN dbo.Типы AS tps ON t.КодТипа = tps.КодТипа
		WHERE tps.Категория = @typeOfGood
		ORDER BY t.Марка;
		END;
END;
GO

--1.2	Создать процедуру, которая реализует следующие функции:
---	создает копию (Заказы_1) таблицы Заказы;
---	увеличивает в таблице Заказы_1 на заданное количество процентов стоимость доставки с 
--	заданным именем для всех заказов, дата исполнения которых находится в заданном интервале времени;
---	выводит данные (КодЗаказа, СтоимостьДоставки (с двумя знаками после запятой), ДатаИсполнения 
--	(в немецком формате)) всех измененных записей таблицы Заказы_1;
---	определяет количество измененных записей в таблице Заказы_1 (как параметр типа output)

DROP PROCEDURE IF EXISTS usp_IncreaseCostOfDelivery;
GO
CREATE PROCEDURE usp_IncreaseCostOfDelivery
	@percent int, 
	@deliveryName nvarchar(40),
	@startTime smalldatetime,
	@endTime smalldatetime,
	@modifiedRowsCount int OUTPUT
AS
SET NOCOUNT ON;
BEGIN
	DROP TABLE IF EXISTS dbo.Заказы_копия; 
	SELECT * INTO dbo.Заказы_копия FROM dbo.Заказы;
	UPDATE dbo.Заказы_копия SET СтоимостьДоставки = ( 100 + CONVERT(REAL,@percent) ) / 100 * СтоимостьДоставки
		WHERE  Доставка = 
			(SELECT КодДоставки FROM dbo.Доставка WHERE Название = @deliveryName)
			AND ДатаИсполнения BETWEEN @startTime AND @endTime;
	SET @modifiedRowsCount = @@ROWCOUNT;
	SELECT 
		zc.КодЗаказа,
		ROUND(zc.СтоимостьДоставки,2) AS Стоимость_Доставки,
		FORMAT(zc.ДатаИсполнения,'d','de-de') AS Дата_Исполнения 
	FROM dbo.Заказы_копия as zc
	WHERE  Доставка = 
			(SELECT КодДоставки FROM dbo.Доставка WHERE Название = @deliveryName)
			AND ДатаИсполнения BETWEEN @startTime AND @endTime
	ORDER BY КодЗаказа;
	 
END;
GO

--1.3	Создать процедуру, которая реализует следующие функции:
---	выводит информацию (КодЗаказа, ДатаИсполнения, Марка, Стоимость товара с учетом скидки) 
--	о заказах клиента с заданным кодом (строковый тип данных) за заданный интервал времени. 
--	В выводимой информации должны содержаться данные о стоимости каждого заказа (с учетом скидки);
---	определяет суммарную стоимость всех заказов заданного клиента за заданный интервал времени 
--	(как параметр типа output)

DROP FUNCTION IF EXISTS ufn_GetClientGoodsInOrders;
GO
CREATE FUNCTION ufn_GetClientGoodsInOrders
(@clientCode nvarchar(10),@startTime smalldatetime,@endTime smalldatetime)
RETURNS TABLE
AS
RETURN
(
SELECT TOP (99.99999) PERCENT
		z.КодЗаказа,
		z.ДатаИсполнения,
		t.Марка, -- из за того что фигурирует это поле создал функцию ниже
		SUM((zn.Количество*zn.Цена)*(1-zn.Скидка)) AS 'Стоимость товара с учетом скидки'
	FROM dbo.Заказы AS z 
	JOIN dbo.Заказано AS zn ON z.КодЗаказа = zn.КодЗаказа
	JOIN dbo.Товары AS t ON zn.КодТовара = t.КодТовара
	WHERE z.Клиент_ID = CONVERT(INT,@clientCode)
		  AND z.ДатаИсполнения BETWEEN @startTime AND @endTime
	GROUP BY ROLLUP(z.КодЗаказа,z.ДатаИсполнения,t.Марка)
	ORDER BY z.КодЗаказа,z.ДатаИсполнения
);
GO
DROP PROCEDURE IF EXISTS usp_GetClientOrders;
GO
CREATE PROCEDURE usp_GetClientOrders
	@clientCode nvarchar(10),
	@startTime smalldatetime,
	@endTime smalldatetime,
	@total int OUTPUT
AS
SET NOCOUNT ON;
BEGIN
	SELECT * FROM ufn_GetClientGoodsInOrders(@clientCode,@startTime,@endTime);
	SELECT 
		fn.КодЗаказа,
		fn.ДатаИсполнения,
		SUM(fn.[Стоимость товара с учетом скидки]) AS 'Стоимость заказа с учетом скидки'
	FROM ufn_GetClientGoodsInOrders(@clientCode,@startTime,@endTime) AS fn
	GROUP BY fn.КодЗаказа,fn.ДатаИсполнения
	;
	SET @total = (SELECT SUM([Стоимость товара с учетом скидки]) FROM ufn_GetClientGoodsInOrders(@clientCode,@startTime,@endTime))
END;
GO

--2.1 Создать пакет для вызова процедуры п.1.1, предусмотрев возможность выдачи сообщения об отсутствии товаров заданного типа;
--2.2 Создать пакет для вызова процедуры п.1.2 и вывода информации о количестве измененных записей;
--2.3 Создать пакет для вызова процедуры п.1.3 и вывода информации о суммарной стоимости всех заказов заданного клиента за заданный интервал времени
SET DATEFORMAT dmy;
EXEC usp_GoodsOfType 'Хлебобулочные';
DECLARE @modifiedRowsCount int;
EXEC usp_IncreaseCostOfDelivery 100,'Почта','01-09-1994','30-11-1994',@modifiedRowsCount OUT;
PRINT 'Изменено ' + STR(@modifiedRowsCount,LEN(@modifiedRowsCount)) + ' строк';
DECLARE @total int;
EXEC usp_GetClientOrders '35','01-01-1993','31-12-1993',@total OUT;
PRINT 'Общая сумма заказов : ' + STR(@total,LEN(@total));
GO