#make function has string paramter
def test(str1:str):
  #make list comprehantion to the string
  #when you split items by split function convert item into int and then return it
  #string even to delete zeros from the items
  result=".".join([ str(int(i)) for i in str1.split(".")])
  return result
print(test("127.0.0.01 "))
print(test("255.024.01.01"))