import csv
fields=['id','name','price','rotten']
li=[]
li1=[]
li2=[]
li3=[]
new=[]
new1=[]
new2=[]
new3=[]
with open("number.csv",'r') as op1:
	r1=csv.reader(op1)
	for r in r1:
		for k in r:
			dic={}
			dic['id']=k		
			li.append(dic)
with open("fruits.csv",'r') as op2:
	r2=csv.reader(op2)
	for r in r2:
		for k,d in zip(r,li):
			d['name']=k
			li1.append(d)
with open("price.csv",'r') as op3:
	r3=csv.reader(op3)
	for r in r3:
		for k,d in zip(r,li1):
			d['price']=k
			li2.append(d)
with open("rotten.csv",'r') as op4:
	r4=csv.reader(op4)
	for r in r4:
		for k,d in zip(r,li2):
			d['rotten']=k
			li3.append(d)
a=0
for d in li3:
	if(d['id']==''):
		if(a%2==0):
			a=a+1
		else:
			d['id']=int(a)
			a=a+1
			new.append(d)
	else:
		a=a+1
		new.append(d)
f=len(new)
a=0
for n in new:
	if(n['name']==''):		
		n['name']=new[(int(a)-10)%f]['name']	
		new1.append(n)
		a=a+1
	else:
		new1.append(n)
		a=a+1
for w in new1:
	if(w['price']==''):
		w['price']=float(0.00)
		new2.append(w)
	else:
		new2.append(w)
for k in new2:
	if(k['rotten']=="1"):
		k['rotten']="t"
		k['price']=float(0.00)
		new3.append(k)
	elif(k['rotten']=="0"):
		k['rotten']="f"
		new3.append(k)
	else:
		new3.append(k)
with open("data.csv",'w') as op6:
	w=csv.DictWriter(op6,fieldnames=fields)
	w.writeheader()
	w.writerows(new3)




