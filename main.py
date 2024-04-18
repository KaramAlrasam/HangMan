#make function accept one integer argument
def zfill(str:str,num:int,sp="0"):
  #messure the lingth of the string
  lingth=len(str)
  #make condition to find out which one is greader
  if lingth>num:
    return str
  
  return sp*(num-lingth)+str
  ########################################
for num in range(5):
   print(zfill(str(num)*num,4,"*"))