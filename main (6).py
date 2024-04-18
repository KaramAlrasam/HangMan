#create center function eccept three argument one degult and the rest string
def center(string:str,num:int,sp=None):
  #make condition if the number less or equil to the lingth return the string
  if num<=len(string):
    return string
  #make two variables each one has number
  l_sp=num//2
  r_sp=num-l_sp
  if num%2==1:
    r_sp+=1
  if sp!=None:
    return (sp*l_sp)+string+(sp*r_sp)
  return (" "*l_sp)+string+(" "*r_sp)
print(center(" karam alrasam ",17,"*"))
    