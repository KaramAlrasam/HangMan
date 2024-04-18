#make function has one integer paramter
def bimonachi(num:int):
  #make list has two items 
  bimo_nachi=[0,1]
  #make for loop the start fro 2 and the end from the user
  for i in range(2,num):
    #append the result in the list
    #                    1           +       0     =  1
    #                     1           +      1      = 2
    #                      2           +      1      =  3
    bimo_nachi.append(bimo_nachi[i-1]+bimo_nachi[i-2])
  return bimo_nachi
print(bimonachi(10))