from random import randint
randm_no = randint(0,100)
print(randm_no)
print('\n')
# printing the random number between 1 and 1000.
r_no=randint(1,1000)
print(r_no)
print('\n')
nm=input("Enter some number")
print(nm)# this number will be string
print(type(nm))
print(float(nm))
print(int(nm))
print('conversion problem:')
celcius=[0,10,20,34,35.5]
farenheit= [((9/5)*temp + 32) for temp in celcius]
print(farenheit)
