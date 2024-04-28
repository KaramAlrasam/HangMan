#import string 
import string
#make function has string paramter
def isdigits(str1:str):
  #use for loop to iterate the chr on the condition
  for l in str1:
  #use tool in string to make conditon
    if l not in string.digits:
      return False
  return True
#make function to discover the input is alphabet and has 
#string paramter

def isalpha(str1:str):
  #use for loop to iterate the chr on the condition
  for l in str1:
  #make condition and using too in string
    if l not in string.ascii_letters:
      return False
  return True
def isalpha1(str1:str):
  for chr in str1:
    if not("A"<=chr<="Z" or "a"<=chr<="z"):
      return False
  return True
def isdigit1(str1:str):
  for chr in str1:
    if not "0"<=chr<="9":
      return False
  return True
  
paradime="0789765"
print(isdigit1(paradime))
print(paradime.isdigit())