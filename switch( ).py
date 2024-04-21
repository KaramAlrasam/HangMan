#make function has three string paramters
def switch(l:list, str1, str2):
  #make condition to make sure the two words are existing
  if str1 and str2 in l:
    #find the index for both words
    word1_i=l.index(str1)
    word2_i=l.index(str2)
    l[word1_i],l[word2_i]=l[word2_i],l[word1_i]
    return l
  else:
    raise NameError ("The items are not existed")
print(switch([1,2,3,4,5,6,7,8,9],"v","t"))