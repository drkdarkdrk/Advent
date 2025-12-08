#Creid to Oscar Kats, Bredan Head

def combine(inputRanges):
      sumRanges=[]
      current=inputRanges[0]

      for start,end in inputRanges[1:]:
            if current[1]>=start:
                  current=[current[0],max(end,current[1])]
            else:
                  sumRanges.append(current)
                  current = [start,end] 
      sumRanges.append(current)
      return sumRanges


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

      ranges = sorted(ranges,key=lambda l:l[0], reverse=False)

      ranges = combine(ranges)
      
      print(ranges)

      for item in ranges:
            total+=item[1]-item[0]+1
      
      print(total)

      

      


