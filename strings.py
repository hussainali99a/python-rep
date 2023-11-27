# greet = "hello"
# print(greet[1])
# print(greet[-1]) #for backward indexing start from -1 and from infront start with 0
# # we can concancate string or we can say add it 
# s ="mustafa"
# d = " qasim ali"
# print(s+d)

# print(len(s))
# slicing means to seperate a part of strings means in hello
#we slice it from e to last second l
#s[1:4] like this
#in slice if we give 2:4 so it means it will give 2 and 3 one less like range.
# print(s[1:7])

# print(s[1:4])

s = "hello"
# print(s[1:4])
# print(s[:3])
# print(s[2:])
# print(s[0:7])
#cannot modify strin by place or by indexing
#slice give  sub sequence of a string
# s[3] = "p"

s = s[0:3] + "p!" 
#we can modify string by slicing and then concancate it.like above example
#string is immutable
print(s)




 