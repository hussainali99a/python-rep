# function takes input and return output
# def hello_func():
# #    print('hello function')
#     return 'hello function'
# # print(hello_func) #gives address where function is in the memory

# # print(hello_func()) #print none becouse we have pass the value
# # if we simply write hello_func() it will print nothing beacuse our return is doing nothing or it is not been execute for certain values
# print(hello_func())
# # print(hello_func().upper())


# # def length(string):
# #     count = 0
# #     for i in string:
# #         count = count +1
# #     return count

# # str = input()
# # s = length(str)
# # print(s)

# def hello_func(greeting,name="you"):
#     return '{},{} function'.format(greeting,name)

# print(hello_func("hi",name = "mustafa"))

# def student_info(*args,**kwarges):
#     print(args)
#     print(kwarges)
# courses = ['maths','arts']
# info = {'name':'mustafa','age':22}
# student_info(*courses,**info)

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)

def days_in_month(year,month):
    if not 1<= month <=12:
        return 'invalid month'
    if month==2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2000))
print(days_in_month(2017,2))