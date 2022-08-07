# A python code to find the average of the sum all even numbers between 1 and 10000
sum = 1
avg = 0
for i in range(10000):
   if i % 2 == 0:
      sum += i
      avg += 1
      print(sum/avg)
   
  
