#list is a sequence of values.
# it is not of perfect order means it can have int ,str in it
#indexing and slicing can be done in lists.
#length of list is given byfunc len
#s ="hello"
#in str s[0] will give h and s[0:1] will also give h
#l =[1,2,3,4,5]
#but in list l[1]=1,but l[0:1] =[1] it will give sub lists
#list can contain another list inside it .
nested = [[2,[67]],4,["hello"]]
print(nested[0])
print(nested[0][1])
print(nested[2][0][1:2])
#list can be updated in place 
#list are mutable
nested[1]= 7
print(nested)
nested[0][1][0]=19
print(nested)

