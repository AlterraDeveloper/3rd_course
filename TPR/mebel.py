#quantity of items: chairs,tables,bookshelfs respectively
items_list = [[],[],[]]
#margin per month
max_margin_list = [-1,-1,-1]
#otpuska
otpusk_list = [0,0,0]

MAY,JUNE,JULY = 0,1,2
CHAIRS,TABLES,BOOKSHELFS = 0,1,2
step = 10
##print(MAY,JUNE,JULY)
##print(CHAIRS,TABLES,BOOKSHELFS)

#balances on warehouse on may,june,july
delta_list = [ [30,100,50], [0,0,0], [0,0,0]]

print("May statistic : ")
for x1 in range(2800-delta_list[MAY][CHAIRS],3000,step):
	for y1 in range(500-delta_list[MAY][TABLES],1000,step):
		for z1 in range(320-delta_list[MAY][BOOKSHELFS],580,step):
			e1 = (75-((20*x1+40*y1+15*z1)/(19200/2)))*2
			margin = x1*100+y1*350+z1*60-delta_list[MAY][CHAIRS]*150*0.02-delta_list[MAY][TABLES]*400*0.02-delta_list[MAY][BOOKSHELFS]*60*0.02
			if margin > max_margin_list[MAY]:
				max_margin_list[MAY] = margin
				items_list[MAY] = [x1,y1,z1]
				otpusk_list[MAY] = e1
print("Margin : "+str(max_margin_list[MAY]))
print("Otpusk : " + str(int(150-otpusk_list[MAY])))
print("Chairs {0}\ntables {1}\nbookself {2}\n".format(items_list[MAY][CHAIRS],items_list[MAY][TABLES],items_list[MAY][BOOKSHELFS]))
print()


delta_list[JUNE][CHAIRS] = items_list[MAY][CHAIRS] - (2800-delta_list[MAY][CHAIRS])
delta_list[JUNE][TABLES] = items_list[MAY][TABLES] - (500-delta_list[MAY][TABLES])
delta_list[JUNE][BOOKSHELFS] = items_list[MAY][BOOKSHELFS] - (320-delta_list[MAY][BOOKSHELFS])
print("June statistic : ")
for x1 in range(2300-delta_list[JUNE][CHAIRS],3000,step):
	for y1 in range(800-delta_list[JUNE][TABLES],1000,step):
		for z1 in range(300-delta_list[JUNE][BOOKSHELFS],580,step):
			e1 = (75-((20*x1+40*y1+15*z1)/(19200/2)))*2
			margin = x1*100+y1*350+z1*60-delta_list[JUNE][CHAIRS]*150*0.02-delta_list[JUNE][TABLES]*400*0.02-delta_list[JUNE][BOOKSHELFS]*60*0.02
			if margin > max_margin_list[JUNE]:
				max_margin_list[JUNE] = margin
				items_list[JUNE] = [x1,y1,z1]
				otpusk_list[JUNE] = e1
print("Margin : "+str(max_margin_list[JUNE]))
print("Otpusk : " + str(int(150-otpusk_list[JUNE])))
print("chairs {0}\ntables {1}\nbookself {2}\n".format(items_list[JUNE][CHAIRS],items_list[JUNE][TABLES],items_list[JUNE][BOOKSHELFS]))
print()


delta_list[JULY][CHAIRS] = items_list[JUNE][CHAIRS] - 2300 - delta_list[JUNE][CHAIRS]
delta_list[JULY][TABLES] = abs(items_list[JUNE][TABLES] - 800-delta_list[JUNE][TABLES])
delta_list[JULY][BOOKSHELFS] = abs(items_list[JUNE][BOOKSHELFS] - 300-delta_list[JUNE][BOOKSHELFS])
print("July statistic : ")
for x1 in range(3350-delta_list[JULY][CHAIRS],3000,step):
	for y1 in range(1400-delta_list[JULY][TABLES],1000,step):
		for z1 in range(600-delta_list[JULY][BOOKSHELFS],580,step):
			e1 = (75-((20*x1+40*y1+15*z1)/(19200/2)))*2
			margin = x1*100+y1*350+z1*60-delta_list[JULY][CHAIRS]*150*0.02-delta_list[JULY][TABLES]*400*0.02-delta_list[JULY][BOOKSHELFS]*60*0.02
			if margin > max_margin_list[JULY]:
				max_margin_list[JULY] = margin
				items_list[JULY] = [x1,y1,z1]
				otpusk_list[JULY] = e1
print("Margin : "+str(max_margin_list[JULY]))
print("Otpusk : " + str(int(150-otpusk_list[JULY])))
print("chairs {0}\ntables {1}\nbookself {2}\n".format(items_list[JULY][CHAIRS],items_list[JULY][TABLES],items_list[JULY][BOOKSHELFS]))
print()

print(items_list)
print(max_margin_list)
print(otpusk_list)
print(delta_list)
