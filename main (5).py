#make function has two paramters one of them string and another integer
def encrypted_word(str:str,num:int):
#make list has letters from a to z
  l_list=[chr(i)for i in range(ord("a"),ord("z")+1)]
  print(l_list)
#make variable has empty value string
  encrypted_word=""
#make for loop on the users word and copersone with l_letter
  for l in str:
    if l.lower()in l_list:
      index=l_list.index(l)
      encrypted_word+=(l_list[(index+num)%len(l_list)])
    else:
      encrypted_word+=l
  return encrypted_word
print("encrypted word is ",encrypted_word("abc",3))     
