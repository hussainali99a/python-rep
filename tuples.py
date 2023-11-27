#tuples are immutable you can change it
tuple_1 = ('history','maths','social science')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'art' #cant change value

print(tuple_1)
print(tuple_2)

#for maodification we use list
#loop through and access than tuples