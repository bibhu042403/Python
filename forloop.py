#1st for loop
my_loop=[1,2,3,4]
for i in my_loop:
    print(i)
print("end of this for loop\n")
my_list=[2,4,5,6,7,8]
#2nd for loop
for num in my_list:
    if num%2==0:
        print(f'Even number: {num}')
    else:
        print(f"odd Number: {num}")
print("End of my_list Loop\n")
#3rd for loop
list_sum=0
for num in my_list:
    list_sum +=num
    print(list_sum)
print("\n")
print(list_sum)
#4th loop
mystring="Hello World"
for letter in mystring:
    print(letter)
print('\n')
for let in 'Hello Bibhu':
    print(let)

mlist = [(1,2),(3,4),(5,6),(7,8)]
len(mlist)
for item in mlist:
    print(item)
for (a,b) in mlist:
    print(a)
    print(b)

d={'k1':1,'k2':2,'k3':3}
for item in d.items():
    print(item)
for key,values in d.items():
    print(values)
print('\n')

name='bibhu'
for item in name:
    if item=='i':
        continue
    print(item)
print('\n')

for item in name:
    if item=='i':
        break
    print(item)

