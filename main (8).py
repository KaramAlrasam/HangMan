#make function named test and has one paramter sort of string
def remove_l(str:str,num:int):
  #make condition measur the lingth of the sring
  if len(str)>3  and 0<=num<=len(str):
    #make the start point and end point and conctenate them
      start=str[:num]
      end=str[num+1:]
      return start+end
  return str
print(remove_l("python",6))