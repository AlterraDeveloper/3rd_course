use Boreas1;

--1.0	Создать копию таблицы Клиенты с именем Клиенты_1
DROP TABLE IF EXISTS dbo.Клиенты_копия;
SELECT * INTO dbo.Клиенты_копия FROM dbo.Клиенты;
GO

----------Тестова проверка работы триггера----------------------------
--ALTER TABLE dbo.Клиенты_копия ADD isDelete bit NOT NULL default 0 ;
--DROP TRIGGER IF EXISTS trg_del_test ;
--GO
--CREATE TRIGGER trg_del_test ON dbo.Клиенты_копия
--INSTEAD OF DELETE
--AS
--	SET NOCOUNT ON;
--	UPDATE dbo.Клиенты_копия SET isDelete = 1
--	WHERE Клиент_Id in (SELECT Клиент_Id FROM deleted);
--GO
---------------------------------------------------------------------------

--1.1	Создать триггер на обработку вставки записи в таблицу Клиенты_1. 
--Условие успешной вставки – уникальность аббревиатуры клиента (поле КодКлиента).

DROP TRIGGER IF EXISTS trg_Insert_Client;
GO
CREATE TRIGGER trg_Insert_Client ON Клиенты_копия
INSTEAD OF INSERT
AS
SET NOCOUNT ON;
IF EXISTS (SELECT 1 FROM dbo.Клиенты_копия[c] WHERE c.КодКлиента in (SELECT i.КодКлиента FROM inserted[i]))
	RAISERROR('Аббревиатура должна быть уникальной!!!',10,1);
ELSE INSERT INTO dbo.Клиенты_копия
	(Адрес,
	Город,
	Должность,
	Индекс,
	КодКлиента,
	Название,
	Область,
	ОбращатьсяК,
	Страна,
	Телефон,
	Факс) 
SELECT 
	i.Адрес,
	i.Город,
	i.Должность,
	i.Индекс,
	i.КодКлиента,
	i.Название,
	i.Область,
	i.ОбращатьсяК,
	i.Страна,
	i.Телефон,
	i.Факс
FROM inserted[i]; 
GO

--1.2	Создать триггер на обработку удаления записей из таблицы Клиенты_1. 
--Условием запрета на удаление является принадлежность клиента стране Италия.

DROP TRIGGER IF EXISTS trg_Delete_Client;
GO
CREATE TRIGGER trg_Delete_Client ON Клиенты_копия
INSTEAD OF DELETE
AS
SET NOCOUNT ON;
DELETE FROM Клиенты_копия WHERE Клиент_Id not in (SELECT Клиент_Id FROM deleted WHERE Страна = 'Италия');
GO

--1.3	Создать триггер на обработку изменения записей в таблице Клиенты_1. 
--Запретить изменение любых данных, касающихся главных менеджеров.

--Триггер запрещает изменение и главных менеджеров и других должностей 
DROP TRIGGER IF EXISTS trg_Update_Client;
GO
CREATE TRIGGER trg_Update_Client ON Клиенты_копия
INSTEAD OF UPDATE
AS
SET NOCOUNT ON;
			--DECLARE @КодКлиента nvarchar(5)
			--DECLARE @Название nvarchar(40);
			--DECLARE @ОбращатьсяК nvarchar(30);
			--DECLARE @Должность nvarchar(30);
			--DECLARE @Адрес nvarchar(60);
			--DECLARE @Город nvarchar(15);
			--DECLARE @Область nvarchar(15);
			--DECLARE @Индекс nvarchar(10);
			--DECLARE @Страна nvarchar(15);
			--DECLARE @Телефон nvarchar(24);
			--DECLARE @Факс nvarchar(24);

			--IF UPDATE(КодКлиента) SET @КодКлиента = (SELECT КодКлиента FROM inserted);
			--ELSE SET @КодКлиента = (SELECT КодКлиента FROM deleted);

			--IF UPDATE(Название) SET @Название = (SELECT Название FROM inserted);
			--ELSE SET @Название = (SELECT Название FROM deleted);

			--IF UPDATE(ОбращатьсяК) SET @ОбращатьсяК = (SELECT ОбращатьсяК FROM inserted);
			--ELSE SET @ОбращатьсяК = (SELECT ОбращатьсяК FROM deleted);

			--IF UPDATE(Должность) SET @Должность = (SELECT Должность FROM inserted);
			--ELSE SET @Должность = (SELECT Должность FROM deleted);

			--IF UPDATE(Адрес) SET @Адрес = (SELECT Адрес FROM inserted);
			--ELSE SET @Адрес = (SELECT Адрес FROM deleted);

			--IF UPDATE(Город) SET @Город = (SELECT Город FROM inserted);
			--ELSE SET @Город = (SELECT Город FROM deleted);

			--IF UPDATE(Область) SET @Область = (SELECT Область FROM inserted);
			--ELSE SET @Область = (SELECT Область FROM deleted);

			--IF UPDATE(Индекс) SET @Индекс = (SELECT Индекс FROM inserted);
			--ELSE SET @Индекс = (SELECT Индекс FROM deleted);

			--IF UPDATE(Страна) SET @Страна = (SELECT Страна FROM inserted);
			--ELSE SET @Страна = (SELECT Страна FROM deleted);

			--IF UPDATE(Телефон) SET @Телефон = (SELECT Телефон FROM inserted);
			--ELSE SET @Телефон = (SELECT Телефон FROM deleted);

			--IF UPDATE(Факс) SET @Факс = (SELECT Факс FROM inserted);
			--ELSE SET @Факс = (SELECT Факс FROM deleted);

	IF EXISTS (SELECT 1 FROM inserted AS i WHERE i.Клиент_Id in 
				(SELECT d.Клиент_Id FROM deleted AS d WHERE d.Должность = 'Главный менеджер'))
					BEGIN
						RAISERROR('НЕЛЬЗЯ!!! Он главный менеджер',10,1);
						RETURN;
					END;
	--ELSE
	--	UPDATE dbo.Клиенты_копия
	--	SET 
	--		КодКлиента= @КодКлиента,
	--		Название = @Название,
	--		ОбращатьсяК = @ОбращатьсяК,
	--		Должность = @Должность,
	--		Адрес = @Адрес,
	--		Город = @Город,
	--		Область = @Область,
	--		Индекс = @Индекс,
	--		Страна= @Страна,
	--		Телефон= @Телефон,
	--		Факс= @Факс
	--	FROM (SELECT * FROM inserted) AS i
	--	WHERE i.Клиент_Id not in (SELECT Клиент_Id FROM dbo.Клиенты_копия[c] WHERE c.Должность = 'Главный менеджер' );
GO

-- 3.1 Создать триггер  для запрета создания или изменения  любой таблицы  базы данных.

DROP TRIGGER IF EXISTS trg_CreateAlterTable;
GO
CREATE TRIGGER trg_CreateAlterTable
ON DATABASE
FOR CREATE_TABLE,ALTER_TABLE
AS
PRINT 'Триггер не позволяет добавить(изменить) таблицы!!!';
ROLLBACK TRANSACTION;
GO
ALTER TABLE dbo.Клиенты_копия ADD isDelete bit NOT NULL default 0;
GO
-- 3.2 Создать триггер для запрета удаления любого триггера базы данных.

DROP TRIGGER IF EXISTS trg_DropTrigger;
GO
CREATE TRIGGER trg_DropTrigger
ON DATABASE
FOR DROP_TRIGGER
AS
PRINT 'Триггер не позволяет удалять другие триггеры!!!';
ROLLBACK TRANSACTION;
GO

