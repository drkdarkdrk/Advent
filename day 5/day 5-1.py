with open("day 5.txt","r") as day5_file:
      data=[]
      ranges =[]
      split=False
      total=0

      for line in day5_file:
            if line=="\n":
                  split=True
            elif split==False:
                  stripped=line.strip()
                  splitted=stripped.split("-")
                  intSplitted=list(map(int, splitted))
                  ranges.append(intSplitted)
            elif split==True:
                  data.append(int(line.strip()))
            else:
                  print("fuck")

      # print(ranges,data)

      for entry in data:
            fresh=False
            for period in ranges:
                  if period[0]<=entry<=period[1]:
                        fresh=True
            if fresh==True:
                  total+=1
      
      print(total)