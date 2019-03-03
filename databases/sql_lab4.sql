use UNIVER;

-- II.  Формирование запросов на выборку 

-- 1.	вывести данные (наименование и цену) 
--10 самых дорогих напитков, формируя заголовки полей запроса разными способами;
select top 10 
	s.НаимСырья as 'Наименование',
	s.ЦенаСырья as 'Цена' from Сырье[s] 
select top 10 
	s.НаимСырья[Наименование],
	s.ЦенаСырья[Цена] from Сырье[s] 
select top 10 
	'Наименование'=s.НаимСырья,
	'Цена'=s.ЦенаСырья from Сырье[s] 
where КодТипаСырья = 
	(select ts.КодТипаСырья from Типы_сырья[ts] 
		where ts.НаимТипаСырья = 'Напитки')
order by s.ЦенаСырья desc;

-- 2.	вывести данные (наименование, цену, код единицы измерения) всех наименований сырья, 
--	цена которых превышает цену    
--   а) любого 
--   б) хотя бы одного
--   сырья, измеряемого штуками;
select 
	s.НаимСырья[Наименование],
	s.ЦенаСырья[Цена],
	s.КодЕдИзм[ЕдИзм] from Сырье[s]
where s.ЦенаСырья > all --any
	(select ЦенаСырья from Сырье 
	 where КодЕдИзм = (select e.КодЕдИзм from Ед_изм[e]
						where e.НаимЕдИзм='Шт.')) 
order by s.ЦенаСырья desc;

-- 3.	вывести данные о количестве наименований напитков, измеряемых бутылками;
select 
	count(s.НаимСырья) as 'Количество напитков, измеряемых бутылками' 
from Сырье[s]
where s.КодЕдИзм = (select e.КодЕдИзм from Ед_изм[e] 
					where e.НаимЕдИзм = 'Бут.');   

-- 4.	вывести данные о максимальной и средней цене продуктов, измеряемых килограммами;
select 
	max(s.ЦенаСырья) as 'Максимальная цена продуктов изм-х в кг',
	round(avg(s.ЦенаСырья),1) as 'Средняя цена продуктов изм-х в кг' 
from Сырье[s]
where s.КодЕдИзм = (select e.КодЕдИзм from Ед_изм[e] 
					where e.НаимЕдИзм = 'Килограмм'); 
 
