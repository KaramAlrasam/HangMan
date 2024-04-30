#make function has two string paramters
def test(str1:str,str2:str):
  m,n=len(str1),len(str2)
  multiList=[[0 for _ in range(m+1)]for _ in range(n+1)]
  length=0
  loction=0
  for i in range(1,m+1):
    for j in range(1,n+1):
      if str1[i-1]==str2[j-1]:
        multiList[i][j]=multiList[i-1][j-1]+1
        if multiList[i][j]>length:
          length=multiList[i][j]
          loction=i-1
      else:
        multiList[i][j]=0
  return str1[loction-length+1:loction+1]
print(test("ddcgggggggg","abcggjjjjjj"))