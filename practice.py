
# list = ["apple ","banana","cherry","apple"]
# list = list + ["grapes"]
# # print(list.remove("apple"))
# # print(len(list))
# # print(type(list))
# # text = "mustafa"
# # text_list = list(text)
# # print(text_list)
# print(list)
# list[0] = "red cherry"
# print(list)
# print(list[-3]) # indexing to start from last



# print(list[2:5])
# print(list[:5]) #it will print from index 0 to 4
# print(list[2:]) # it will print index 2 to last
# print(list[-4:-1])

# print("apple" in list)




# list[1:3] = ["dear","sand"] #changing list item from specific range 
# print(list)


# list.remove("banana")
# print(list)
#for remove the specify index we use pop()
#in pop() method if we do not specify index it remove the last item by default
# list.pop(2)

# list.pop() #last item removed from the list.
#we can also use del keyword to remove item from list.
# list = ["apple","banana","grapes","kiwi","orange","mango","cherry","papaya"]
# print(list)
# del list

# print(list)
# del list[4] 
#del also can delete full list.
#clear function is use to clear all entities in list it empties the list.

# list.clear() #empties the list

# print(list)


# for i in list:
#     print(i)
# for i in range(len(list)):
#     print(list[i])


# by using while loop
# list = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# while i<len(list):
#     print(list[i])
#     i = i+1
# by list compheresion
# list =[1,2,3,4,5,6,7,8,9,10]
# [print(x) for x in list] #this is comperehension


# listfruits = ["apple","banana","orange","kiwi","cherry","almonds"]
# newlist = [i for i in listfruits if "a" in i]
# # now same thing with list comperesion

# # for i in listfruits:
# #     if "a" in i:
# #        newlist.append(i)


# print(newlist)


# listfruits = ["apple","banana","orange","kiwi","cherry","almonds"]
# for i in listfruits:
# for i in range(len(listfruits)): #printing through index

#     print(listfruits[i])
#     [print(i) for i in listfruits] #by  Comprehension method


# newlist = [i for i in listfruits if "a" in i]


# print(newlist)

# newlist = [i for i in listfruits if i!="apple"]
# print(newlist)


# newlist = [i for i in range(0,10)]
# print(newlist)

# newlist = [i for i in range(0,10) if i <5 ]
# print(newlist)


# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# list = ["apple","banana","kiwi","cherry","mango"]
# list.sort()
# print(list)


# l = [23,45,67,89,10,20,30]
# l.sort()
# print(l)

# # to sort descending, use the keyword argument reverse = True:
# l.sort(reverse = True)
# print(l)
# using key word and this type of of func below can give the result how close the no. is to 50
# def myfunc(n):
#     return abs(n-50)
# thislist = [100,82,65,23,50]
# thislist.sort(key = myfunc)
# print(thislist)


# lists = ["Apple","Banana","orange","kiwi"] #by default it sort capital letter first like it arrange first the capital letter word first 

# lists.sort()
# print(lists)
# lists.sort(key = str.lower) #by using this we can arrange list in a alphabatically order like previously
# print(lists)

# What if you want to reverse the order of a list, regardless of the alphabet?

# # The reverse() method reverses the current sorting order of the elements.

# lists.reverse() #it will reverse the list no matter the alpabatical order
# print(lists)



# thislist = ["apple","banana","mango"]
# mylist = thislist.copy() #using copy method we copy list
# print(mylist)
# print(id(mylist))
# print(id(thislist))
# print(thislist is mylist)

# l = thislist[:1]
# print(l)

# print(l is thislist)


# another method to copy list is list() function

# l = [1,2,3,4,5,6,7,8,9,10]
# mylist = list(l)
# print(mylist)
# print(l is mylist)
# print(id(l))
# print(id(mylist))




l = [1,2,3,4,5,6]
l2 = [11,12,13,14,15]
list = l +l2 
print(list)