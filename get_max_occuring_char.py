#make function has one string paramter
def get_max_occuring_char(str:str):
  #create list its long similar to the list ASCII_chr 
  #which is length 256 and its elemients wil be zero 
  #even later we can update those elemients
  ASCII_chr=[0]*256
  #make for loop to the str 
  #and use ord() function to find the index for letter in the list of ASCII_chr
  #and then update zero
  for l in str:
    ASCII_chr[ord(l)]+=1
  #make variable its value -1 and then it will be updated
  max= -1
  #we choose -1 beacouse it comes befor zero dirctly
  ######
  #make variable its value empty string we will updated later
  #it will be as result later
  ch=""
  #make for loop to the string and update the value for max and for ch
  for l in str:
  # that's true max has -1 in begnning 
    if max<ASCII_chr[ord(l)]:
      #but we will update it by take advantige of circle for loop 
      max=ASCII_chr[ord(l)]
      ch=l
  return ch
print(get_max_occuring_char("abcdefghijkb"))
print(get_max_occuring_char("Python: Get file creation and modification date/times"))