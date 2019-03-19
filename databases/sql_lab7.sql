use i315EA;

select
	'���' = year(w.������������),
	'�����' = datename(month,w.������������)+' 1��',
	format(w.������������,'d','de-de') as '����',
	round(sum(w.����������*w.����),0)[�����]
from dbo.�����[w] 
	join dbo.�����[s] on s.�������� =  w.��������
	join dbo.����_�����[ts] on s.������������ = ts.������������
where 
	ts.������������� = '������'
	and datepart(weekday,w.������������) = 6
	and datepart(day,w.������������) <= 8
group by(w.������������)
;

select 
year(w.������������),
month(w.������������),
datename(month,w.������������) + '/' + 
case 
	when datepart(day,w.������������) between 1 and 10 then '1-st'
	when datepart(day,w.������������) between 11 and 20 then '2-nd'
	when datepart(day,w.������������) > 20 then '3-rd'
end
--round(sum(w.����������*w.����),2)[�����] 
from dbo.�����[w] where year(w.������������) = 2002
group by(case 
	when datepart(day,w.������������) between 1 and 10 then '1-st'
	when datepart(day,w.������������) between 11 and 20 then '2-nd'
	when datepart(day,w.������������) > 20 then '3-rd'
end);

