import csv

data = []
intData = []
total=0

file = open("day2.txt","r")
for line in file:
    stripped = line.strip()
    split = stripped.split(",")

for entry in split:
    data.append(entry.split("-"))
    
for item in data:
    intData.append(list(map(int, item)))
    
for item in intData:
    for i in range(item[0],item[1]+1):
        errors = []
        factors = []
        for j in range(1,len(str(i))+1):
            if len(str(i))%j==0:
                factors.append(j)
        factors.pop()
        
        for factor in factors:
            similar=True
            for k in range(1,int(len(str(i))/factor)):
                if(str(i)[0:factor]!=str(i)[k*factor:(k+1)*factor]):
                    similar=False
            if similar==True:
                errors.append(i)
        for amount in list(set(errors)):
            total+=amount
##            print(amount)
        
print(total)
                    
