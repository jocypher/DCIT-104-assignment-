# A python program to find the average of the sum the number of prime numbers from 1 to 10 and 1 to 10000
prime_numbers = [2,3,5,7]
sum = prime_numbers[0] + prime_numbers[1] + prime_numbers[2]
prime = sum + prime_numbers[3] 
print(prime)
  
  # finding the average 
  
primes = len(prime_numbers )
aver = prime/ primes
print(aver)


# OR

sum = 1
avg =0
for i in range(10000):
  if (i % 2 == 1 and i % 3 != 0) or (i == 3) :
    sum += i
    avg += 1
    print(sum/ avg)
