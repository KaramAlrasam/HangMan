def max(list:list):
  for index in range(len(list)):
    for index_a in range(index+1,len(list)):
      if list[index]<list[index_a]:
        list[index],list[index_a]=list[index_a],list[index]
    
  return list[0]
print(max([2,1,6,4,9,80,5,0,3,10]))