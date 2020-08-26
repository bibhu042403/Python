lower = 900
upper = 1200

print("Prime numbers between", lower, "and", upper, "are:")
print("hello")
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)