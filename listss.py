courses = ['history','math','social science','PSD']
courses_2 = ['M1','M2','BEEE']
print(courses)
print(courses[0])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

# courses.append("art") # adds element in last
# courses.append(courses_2)  
# print(courses)

# courses.extend(courses_2)
# print(courses)

courses.insert(3,"chemistry")
print(courses)


nums = [1,5,6,7,8,9,2]
# nums.sort(reverse = True)
nums_sorted=sorted(nums)
print(nums_sorted)

popped = nums.pop() #pops the last element
print(popped)
print(nums)

nums.remove(5)
print(nums)
print(sum(nums))

print(nums)
print(nums.index(6)) #gives index of 6
print(10 in nums) #see whether elemnet is there or not gives answer in true or false

for i in nums:
    print(i)


for index,num in enumerate(nums,start = 1):
    print(index,num)
    
for index,num in enumerate(nums):
    print(index,num)
    
courses_str = '- '.join(courses)
print(courses_str)

new_list = courses_str.split(' - ')
print(new_list)
