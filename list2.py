list1 = [1,3,5,7]
list2 = list1[:] # by doing this slicing method we created the new list of same type if we update in it it will effect current list but not first from where we have copied.

print(list1[:])
list2[3] = 8
print(list2)
print(list1)


x = [1,2,3,4]
y = [1,2,3,4]
z = x

print(x ==z) #this is true bcz it is pointing towards list x

print(x is y) # here it is false bcz it is two different list of different address


list1 = [1,2,3,4,5]
list2 = [2,4,5,6,7]
list3 = list1 + list2
print(list3)


list4 = [1,3,5,7]
list5 = list4 #this create a fresh list but of two names means it is having two names list4 and list5

list4 = list4 + [9]
print(list5)
print(list4)
print(list4 is list5)




