import random
import matplotlib.pyplot as plt

list1="./HealthyCells/"
list2="./CancerCell_Type1/"
list3="./CancerCell_Type2/"

directory = list1
cell_deaths=[]

for i in range(16):
	montecarlo_rand=random.sample(range(1,65),16)
	cell_death=0
	for j in montecarlo_rand:
		rows=[]
		with open(directory+"output"+str(j)) as fptr:
			rows = fptr.readlines()
		rows=[row.split(" ") for row in rows]
		#print(rows[len(rows)-1][5])
		if int(rows[len(rows)-1][5])>=50:
			cell_death+=1

	cell_deaths.append(cell_death)

fptr.close()

print(cell_deaths)

plt.figure(0)
plt.hist(cell_deaths, align='mid', bins=10)
plt.ylabel("Number of Groups")
plt.xlabel("Number of Cell Deaths")
plt.title("Cell Deaths in Healthy Cells")

directory = list2
cell_deaths=[]

for i in range(16):
	montecarlo_rand=random.sample(range(1,65),16)
	cell_death=0
	for j in montecarlo_rand:
		rows=[]
		with open(directory+"output"+str(j)) as fptr:
			rows = fptr.readlines()
		rows=[row.split(" ") for row in rows]
		#print(rows[len(rows)-1][5])
		if int(rows[len(rows)-1][5])>=50:
			cell_death+=1

	cell_deaths.append(cell_death)

fptr.close()

print(cell_deaths)

plt.figure(1)
plt.hist(cell_deaths, align='mid', bins=10)
plt.ylabel("Number of Groups")
plt.xlabel("Number of Cell Deaths")
plt.title("Cell Deaths in Type 1 Cancer Cells")

directory = list3
cell_deaths=[]

for i in range(16):
	montecarlo_rand=random.sample(range(1,65),16)
	cell_death=0
	for j in montecarlo_rand:
		rows=[]
		with open(directory+"output"+str(j)) as fptr:
			rows = fptr.readlines()
		rows=[row.split(" ") for row in rows]
		#print(rows[len(rows)-1][5])
		if int(rows[len(rows)-1][5])>=50:
			cell_death+=1

	cell_deaths.append(cell_death)

fptr.close()

print(cell_deaths)

plt.figure(2)
plt.hist(cell_deaths, align='mid', bins=10)
plt.ylabel("Number of Groups")
plt.xlabel("Number of Cell Deaths")
plt.title("Cell Deaths in Type 2 Cancer Cells")

plt.show()












			
