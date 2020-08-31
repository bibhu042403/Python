x=0
while x<5:
    print(f'The current value of x is {x}')
    x +=1
else:
    print('X is not less than 5!')
print('\n')
y=5
while y<10:
    if y==8:
        break
    print(y)
    y +=1
print("\n")

z=10
for i in range(0,z):
    if i==8:
        continue
    print(i)