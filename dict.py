#key value pairs
#key is a unique identifier
#value is defination
#key can also be integer or any data type

student = {'name':'mustafa','age':25,'courses':['maths','compsci']}
print(student['name'])
print(student['courses'])
#print(student['phone']) #printing key does not access

#instead use get function
print(student.get('name'))
student['phone'] = '555-555'
# print(student.get('phone','not found'))
# use update function to update
student.update({'name':'ali'})
print(student)
print(student.values())
print(student.keys())
print(len(student))
print(student.items())

for key ,value in student.items():
    print(key,value)
    
