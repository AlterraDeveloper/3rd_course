use UNIVER;

--ALTER TABLE Employees ADD department int;

--update Employees set department = 1 where codeid%2 = 0; --��������� 
--update Employees set department = 2 where codeid%2 != 0; --���������
--TODO �������� ����� ����������� � ����� 3 � �������� ��� ������� � ������ ������

--��������� � ����� 1 ���� ����������� 3-��� ������, ���������� ����� ������� �� ��������� 300
update Employees set department = 1
where department = 3 and salary <=300;


--� ����� 2 ���������  ���� ����������� 3-��� ������, ���������� ����� ������� ��������� 300
update Employees set department = 2
where department = 3 and salary >= 300;
