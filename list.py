mylist=['one','two','three','four']
print(mylist[0])
print(mylist[1:])
anlist = ['five','six']
mylisy = mylist.append(anlist[1])
print(mylist)
print(mylist.pop())
print(mylist.pop(1))
print(mylist.sort())
print('\n')
list1=[23,56,21,43,76]
print(min(list1))
print(max(list1))

from random import shuffle
mylist12=[1,2,3,4,5,6,7,8,9]
shuffle(mylist12)
print(mylist12)
print('\n')

mlist='hello'
mlist1=[]
for letter in mlist:
    mlist1.append(letter)
print(mlist1)

# Another method to print same things
mlist2=[letter for letter in mlist]
print(mlist2)
mlist3=[x for x in 'Hello']
print(mlist3)
mlist4=[y for y in range(0,10)]
print(mlist4)
mlist5=[z**2 for z in range(1,10)]
print(mlist5)
mlist6=[n for n in range(0,10) if n%2==0]
print(mlist6)






