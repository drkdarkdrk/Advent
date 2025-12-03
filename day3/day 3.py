with open("day3.txt","r") as day3_file:
      data=[]
      for line in day3_file:
            data.append(line.strip())

      total=0

      for entry in data:
            max=0
            for i in range(len(entry)):
                  for j in range(i+1,len(entry)):
                        temp = int(str(entry)[i]+str(entry)[j])
                        if (temp)>max:
                              max=temp
            total+=max
      print(total)