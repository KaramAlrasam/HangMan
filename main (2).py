#first we need to make function has two paramters item and list
def append(l:list,item):
  #second we need to know the lingth of the list 
  #beacauce we can conctenate list with list so we add the item dirctly between two list brackt and conctenate it with the stratch of our list
  l[len(l):]=[item]
#####################################
list=[]
print(list)
for num in range(7):
  append(list,num)
print(list)