with open("day4.txt","r") as day4_file:
      data=[]
      for line in day4_file:
            item=[]
            lineStrip=line.strip()
            for entry in lineStrip:
                  temp=[]
                  temp.append(entry.strip())
                  item.append(temp)
            data.append(item)


      for line in data:
            line.insert(0,['.'])
            line.append(['.'])

      topBottomArray=[]
      for i in range(len(data)+2):
            topBottomArray.append(['.'])

      data.insert(0,topBottomArray)
      data.append(topBottomArray)



      total=0
      
      index=[]
      for i in range(len(data)):
            smallIndex=[]
            for j in range(len(data[i])):
                  smallIndex.append([0])
            index.append(smallIndex)

      kill=False
      while(kill==False):
            loopTotal=0

            for i in range(1,len(data)-1):
                  lineTotal=0
                  for j in range(1,len(data[i])-1):
                        count=0
                        if(data[i][j]==['@']):
                              for p in range(-1,2):
                                    if(data[i+p][j-1]==["@"]):
                                          count+=1
                                    if(data[i+p][j]==["@"]):
                                          if(p!=0):
                                                count+=1
                                    if(data[i+p][j+1]==["@"]):
                                          count+=1
                              if(count<4):
                                    index[i][j]=[1]
                                    lineTotal+=1
                  loopTotal+=lineTotal
            total+=loopTotal

            # print()
            # for i in range(len(data)):
            #       for j in range(len(data[i])):
            #             print(data[i][j] ,end='')
            #       print("")

            if(loopTotal>0):
                  for i in range(1,len(data)-1):
                        for j in range(1,len(data[i])-1):
                              if(index[i][j]==[1]):
                                    data[i][j]=['.']
            else:
                  kill=True
      print(total)
      

                  

            