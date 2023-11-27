#set are unordered and dont have duplicates
cs_courses = {'history','maths','physics','compsci'}
print(cs_courses)
#duplicate put ting in set
cs_courses = {'history','maths','physics','compsci','maths'}
print(cs_courses) #donot print maths as math is double here 


#intersection on two set:-
cs_courses = {'history','maths','physics','compsci'}
art_courses = {'history','physics','compsci','art'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

#empty list
empty_list = []
empty_list = list()
#empty tuple
empty_tuple = ()
empty_list = tuple()

empty_set = {} #cant do this to create set {} this create dictionary so use set() function to create set
empty_set = set()
