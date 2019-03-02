#quantity of items: chairs,tables,bookshelfs
items_in_may = []
items_in_june = []
items_in_july = []

#otpuska
may_e = 0
june_e = 0
july_e = 0
 

max_margin_in_may = -1
max_margin_in_june = -1
max_margin_in_july = -1

step = 10

#balances on warehouse on may,june,july
delta_x = [30,0,0]
delta_y = [100,0,0]
delta_z = [50,0,0]

print("May statistic : ")
for x1 in range(2800-delta_x[0],3000,step):
	for y1 in range(500-delta_y[0],1000,step):
		for z1 in range(320-delta_z[0],580,step):
			e1 = (75-((20*x1+40*y1+15*z1)/(19200/2)))*2
			margin = x1*100+y1*350+z1*60-delta_x[0]*150*0.02-delta_y[0]*400*0.02-delta_z[0]*60*0.02
			if margin > max_margin_in_may:
				max_margin_in_may = margin
				items_in_may = [x1,y1,z1]
				may_e = e1
print("Margin : "+str(max_margin_in_may))
print("Otpusk : " + str(int(150-may_e)))
print("chairs {0}\n tables {1}\n polka {2}\n".format(items_in_may[0],items_in_may[1],items_in_may[2]))
print()


delta_x[1] = items_in_may[0] - (2800-delta_x[0])
delta_y[1] = items_in_may[1] - (500-delta_y[0])
delta_z[1] = items_in_may[2] - (320-delta_z[0])
print("June statistic : ")
for x1 in range(items_in_may[0]-delta_x[1],3000,step):
	for y1 in range(items_in_may[1]-delta_y[1],1000,step):
		for z1 in range(items_in_may[2]-delta_z[1],580,step):
			e1 = (75-((20*x1+40*y1+15*z1)/(19200/2)))*2
			margin = x1*100+y1*350+z1*60-delta_x[1]*150*0.02-delta_y[1]*400*0.02-delta_z[1]*60*0.02
			if margin > max_margin_in_june:
				max_margin_in_june = margin
				items_in_june = [x1,y1,z1]
				june_e = e1
print("Margin : "+str(max_margin_in_june))
print("Otpusk : " + str(int(150-june_e)))
print("chairs {0}\n tables {1}\n polka {2}\n".format(items_in_june[0],items_in_june[1],items_in_june[2]))
print()