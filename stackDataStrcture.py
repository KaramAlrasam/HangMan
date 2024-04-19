class stack:
  #make initalise for the list
  def __init__(self):
    self.stack=[]
  #make function push is charge in to add item to the list
  def push(self,item):
    """function push is charge in to add item to the list"""
    self.stack[len(self.stack):]+=[item]
  #make function peek is in charge  to show last item in the list
  def peek(self):
    """make function peek is in charge  to show last item in the list"""
    #make condition for the list to make sure is empty or not
    if not self.is_empty(self.stack):
      return self.stack[-1]
    return None
  #make function is_empty is in charge to make sure from the list is empty or not
  def is_empty(self,item):
    """function is_empty is in charge to make sure from the list is empty or not"""
    #the answer will be True or False
    return len(item)==0
  #make function pop is in charge to delete the last item in the list
  def pop(self):
    """function pop is in charge to delete the last item in the list"""
    #make condition for the list to make sure from the list is empty or not
    if not self.is_empty(self.stack):
      #find the index of the item in the list
      
      del self.stack[-1]
  #make function size is in charge in to messure the list
  def size(self):
    """function size is in charge in to messure the list"""
    return len(self.stack)
#make instance for the class stack
my_stack=stack()
#add three items for the list
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
#peek the list
print("The last item about the list: ",my_stack.peek())#output 3
my_stack.pop()
my_stack.pop()
print("the answer about the list: ",my_stack.is_empty(my_stack.stack))
print("the size of the list: ",my_stack.size())