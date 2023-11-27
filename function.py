# def add(n,m):
#     sum = n+m
#     return sum


# num1 = int(input("enter the number1: "))
# num2 = int(input("enter the number2: "))

# print(add(num1,num2))
    


def power(x,n):
    ans = 1
    for i in range(0,n):
        ans = ans*x

    return ans



num = int(input("enter number:"))
pow = int(input("power:"))

print(power(pow,num))

