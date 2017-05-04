import matplotlib.pyplot as plt

list1="./HealthyCells/"
list2="./CancerCell_Type1/"
list3="./CancerCell_Type2/"

directory = list1
vals=[]
for i in range(1,65):
	rows=[]
	#val=0
	with open(directory+"output"+str(i)) as fptr:
		rows=fptr.readlines()
	rows=[row.split(" ") for row in rows]
	val=0
	count=0
	for j in rows:
		#row=row.split()
		if int(rows[count][5])>=50:
			val=rows[count][0]
			vals.append(int(val)/10000000)
			#print(rows[count][0])
			break
		count+=1
	

fptr.close()

#print(vals)

plt.figure(0)
plt.hist(vals,normed=True)
plt.xlabel("Time of first cell death")
plt.ylabel("Probability")
plt.title("Probability distribution of time to death in Healthy Cells")

directory = list2
vals=[]
for i in range(1,65):
	rows=[]
	#val=0
	with open(directory+"output"+str(i)) as fptr:
		rows=fptr.readlines()
	rows=[row.split(" ") for row in rows]
	val=0
	count=0
	for j in rows:
		#row=row.split()
		if int(rows[count][5])>=50:
			val=rows[count][0]
			vals.append(int(val)/10000000)
			#print(rows[count][0])
			break
		count+=1

fptr.close()

#print(vals)

plt.figure(1)
#plt.hist(vals)
plt.hist(vals,normed=True)
plt.xlabel("Time of first cell death")
plt.ylabel("Probability")
plt.title("Probability distribution of time to death in Type 1 Cancer Cells")

directory = list1
vals=[]
for i in range(1,65):
	rows=[]
	#val=0
	with open(directory+"output"+str(i)) as fptr:
		rows=fptr.readlines()
	rows=[row.split(" ") for row in rows]
	val=0
	count=0
	for j in rows:
		#row=row.split()
		if int(rows[count][5])>=50:
			val=rows[count][0]
			vals.append(int(val)/10000000)
			#print(rows[count][0])
			break
		count+=1
	

fptr.close()

#print(vals)

plt.figure(2)
plt.hist(vals,normed=True)
plt.xlabel("Time of first cell death")
plt.ylabel("Probability")
plt.title("Probability distribution of time to death in Type 2 Cancer Cells")
plt.show()