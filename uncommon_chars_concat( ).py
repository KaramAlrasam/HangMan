#make function has two string paramters
def test(str1:str,str2:str):
  #use set function to get unique letters for each string
  set1=set(str1)
  set2=set(str2)
  #get the recemblnce items by  using &
  recemblnce= set1 & set2
  #make list comperhantion for two string and conctenate them and make condition
  # for not in recemblnce
  result=[i for i in str1 if i not in recemblnce]+[i for i in str2 if i not in recemblnce]
  return "".join(result)
s1="abcdpqr"
s2="xyzabcd"
print(test(s1,s2))