def split(string:str, num=None,sap=None):
  #create empty list
  list=[]
  #create point start for slicing
  start=0
  #create for loop roun on the string
  for index in range(len(string)):#karam alrasam loves c++
    # create the list debands on the on the saprator of the user or defult one
    if string[index]==" " or string[index]==sap:
      list.append(string[start:index])
      #update the start point
      start=index+1
      # this condition maks sure from lingth of the list equil to the user num if succeded break the loop
      if num!=None and len(list)==num:
         break
  list.append(string[start:])
  return list
print(split("karam-alrasam-loves-c++",2,"-"))

  #discover the begining of each word and append it to the list