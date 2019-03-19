use i315EA;

select
	'Год' = year(w.Датадвижения),
	'Месяц' = datename(month,w.Датадвижения)+' 1сб',
	format(w.Датадвижения,'d','de-de') as 'Дата',
	round(sum(w.Количество*w.Цена),0)[Объем]
from dbo.Склад[w] 
	join dbo.Сырье[s] on s.КодСырья =  w.КодСырья
	join dbo.Типы_сырья[ts] on s.КодТипаСырья = ts.КодТипаСырья
where 
	ts.НаимТипаСырья = 'Прочие'
	and datepart(weekday,w.Датадвижения) = 6
	and datepart(day,w.Датадвижения) <= 8
group by(w.Датадвижения)
;

select 
year(w.Датадвижения),
month(w.Датадвижения),
datename(month,w.Датадвижения) + '/' + 
case 
	when datepart(day,w.Датадвижения) between 1 and 10 then '1-st'
	when datepart(day,w.Датадвижения) between 11 and 20 then '2-nd'
	when datepart(day,w.Датадвижения) > 20 then '3-rd'
end
--round(sum(w.Количество*w.Цена),2)[Объем] 
from dbo.Склад[w] where year(w.Датадвижения) = 2002
group by(case 
	when datepart(day,w.Датадвижения) between 1 and 10 then '1-st'
	when datepart(day,w.Датадвижения) between 11 and 20 then '2-nd'
	when datepart(day,w.Датадвижения) > 20 then '3-rd'
end);

