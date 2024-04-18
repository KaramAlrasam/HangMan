def lower(string):
  #create dictionary has alphabet
  alphabet_dict = {
      'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g',
      'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n',
      'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u',
      'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'
  }
#create variable kind of sting but it's empty and its name word
  word=""
  #make for loop on the string fro thr user
  for letter in string:
    # make sure from the letter is existed in alphabet_dict
    if letter in alphabet_dict: 
      #concatenate letter from alphabet_dict with word to get the final result
      word+=alphabet_dict[letter]
    # if the letter is not exist in the alphabet_dict. concate nate letter with word dirctly
    else:
      word+=letter
  return word # return the final result
print(lower("KARAM ALRASAM A1"))
    