def sum_recursive(a):
   if a == 0:
      return 0
   else:
      return a + sum_recursive(a-1)
   
result=sum_recursive(10)
print("The sum of numbers from 0 to 10 is:" ,result)


