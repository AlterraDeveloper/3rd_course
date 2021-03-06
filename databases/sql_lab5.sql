use UNIVER;

-- Формирование запросов на выборку

-- 1.	Вывести  список имеющегося на складе сырья
select 
	s.НаимСырья[Список имеющегося на складе сырья ] 
from Сырье[s] 
where s.КодСырья in (select 
						w.КодСырья 
					from Склад[w] 
					--where w.КодСклада = 1
					);

-- 2.	Вывести  список отсутствующего  на складе сырья
select 
	s.НаимСырья[Список отсутствующего на складе сырья] 
from Сырье[s] 
where s.КодСырья not in (select 
						w.КодСырья 
					from Склад[w] 
					--where w.КодСклада = 1
					);

-- 3.	Вывести данные обо всех наименованиях сырья с указанием  
-- максимальной и средней цены сырья по типам и единицам измерения 
-- (сортировать данные по типам, единицам измерения и наименованиям сырья).
select 
	s.НаимСырья,
	s.КодТипаСырья,
	s.КодЕдИзм,
	round(avg(s.ЦенаСырья),2)[Сред.цена],
	max(s.ЦенаСырья)[Макс.цена]
from Сырье[s] 
group by rollup(s.КодТипаСырья,s.КодЕдИзм,s.НаимСырья)
order by s.КодТипаСырья,s.КодЕдИзм,s.НаимСырья;

-- 4.	Вывести данные обо всех кодах сырья 
-- с указанием  общего объема сырья, поступившего на основной склад  за 2002 год 
select 
	w.КодСырья,
	round(sum(w.Количество),2)[Объем] 
from Склад[w] 
	where w.КодСкладаДвиж = 1 and
	year(w.Датадвижения) = 2002 and
	w.ПризнакДвижения = 'Поступление'
	group by rollup( w.КодСырья)
	order by w.КодСырья;  