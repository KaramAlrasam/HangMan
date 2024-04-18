
# first we need to make fuction has two paramters string and integer
def fill(str:str,width=None):
  #use split to divide it into multible lines
  list=str.split("\n")
#make list to colect the modifide lines
  m_list=[]
  #make width optional
  if width!=None:
#if the user input width make loop on the list which has lines of string
    for line in list:
#divide the number of width into two equils number   
      rinde=width//2
      linde=width-rinde
#append the modifide line with spaces in the beggning and the end
      m_list.append(" "*linde+line+" "*rinde)
#return the m_list by using join function
    
    return "\n".join(m_list) 
  else:
    return(str)
sample_text = '''
Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java.
'''
print(fill(sample_text,))
    
    
    
  