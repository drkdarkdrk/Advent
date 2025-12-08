file = open("day1.txt", "r")

contents = []

for line in file:
    temp = line.strip()
    if temp[0] == "L":
        contents.append(-1*int(temp[1:]))
    else:
        contents.append(int(temp[1:]))
file.close()

dial = 50
password = 0
check=[-950]

for entry in contents:
#for entry in check:
    start=dial
    dial += entry
##    print()
##    print(entry)
##    print("1-",dial)

    while dial<0:
            dial+=100    
            password+=1
##            print("4-",dial)
            if start==0:
                password-=1
                start=999
                
 
    while dial>100:
        dial-=100
        password+=1
##        print("5-",dial)


    if dial==0:
        password+=1
#        print("6-",dial)

    if dial==100:
        password+=1
        dial-=100
#        print("7-",dial)
        
#    print(password)
   
print(password)
