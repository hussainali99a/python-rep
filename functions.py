
# def hello():
#     print("hello world")


# hello()

# hello()

# hello()



# def hello(name):
#     print("hello "+  name)



# myname = input("enter your name:")
# hello(myname)



#parameters are values accepted by the function inside the function definition.
#arguments pass through the function when we call it
# you can also pass default value in function like below


# def hello(name = "my friend"):
#     print("hello " + name)

# hello() # here i havent pass the value but bcz  i have given the
#value in parameters so it is said to be default value.

# hello("mustafa")

# multiple parameters

# def hello(name , age):
#     print("hello "+ name + (", you are " + str(age)) + " years old ")


# hello("mustafa",20)


# def hello(name):
#     print("hello "+ name +"!")
#     return name

# myname = input("enter your name:")
# hello(myname)


# variable scope:-
# if variable is decleared before  the function than it can be use inside and utside the function.
# it is called global variables.


# age = 8
# def test():
#     print(age)

# print(age)
# test()

# now if we declare varibale inside the function so it is local variable
# it cant be print outside


# def test():
#     age = 8
#     print(age)
#     # print(age) cant use variable outside the function if it is declare inside the function

# test()

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk("my name is mustaf qasim ali")
