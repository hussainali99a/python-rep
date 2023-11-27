#print list of n factosrs:-
n = int(input("enter the number"))

flist = []
for i in range(1,n+1):
    if n%i==0:
        flist = flist + [i]
print(flist) 

# n = int(input("enter the number: "))

# flist = []
# i =1
# while i<=n:
#     if n%i==0:
#         flist = flist + [i]
#         i = i+1

# print(flist) 

