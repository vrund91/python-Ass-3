import random

list1 = [1,2,3,4,5,6,7,8,9,0]
set1 =  {1,2,3,4,5,6,7,8,9,0} 

print("Random element from the list:",random.choice(list1))
print("Random element from the set:",random.choice(list(set1)))