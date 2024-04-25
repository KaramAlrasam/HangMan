import time
n_list=[1,2,3,4,5,6,7,8,9]
start=time.time()
#make function has list paramter
def sortSaprated(l:list):
  
  #make for loop for the list
  for num in range(len(l)):
    #make condition for the num if it was even number let it stay in its place
    #and if it was odd number make it swich with another one
    #so you need two for loop
    for num1 in range(num+1,len(l)):
      if l[num]%2!=0 and l[num1]%2==0:
        l[num],l[num1]=l[num1],l[num]
  return l

print(sortSaprated(n_list))
print(time.time()-start)
print("-"*30)
###########################
start=time.time()
def sortSaprated2(l:list):
  for i in range(len(l)-1):
    if l[i]%2!=0 and l[i+1]%2==0:
      l[i],l[i+1]=l[i+1],l[i]
  return l
print(n_list)
print(time.time()-start)