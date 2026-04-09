print("welcome to python")
print(5+4)
print(5-4)
print(5*4)
print(5/2)
#print("5/2")

# print() is a in-built python function
# this is a comment
# there are two types of comments in python
# 1. single line comment (#)
# 2. multi line comment(''' or """)

"""
print("python students: charan, nitish,sai ram, ahmed and naveen")
print("python students: charan, nitish,sai ram, ahmed and naveen")
print("python students: charan, nitish,sai ram, ahmed and naveen")
"""
# this is a comment
# syntax = grammer

print(10%3)
print(10//3)
print(3**2)
print(3**3)


# population density
# d=p/a
print(16000000/650)


# f=1.8*c+32 , c=35
print(1.8*35+32)
print(1.8*40+32)

# sum of first n natural numbers
# n*(n+1)/2
# n=4, 1,2,3,4=10
# n=10, 1,2,3...8,9,10=55
# n=15
print(10*(10+1)/2)
print(4*(4+1)/2)
print(15*(15+1)/2)

# variables
# let x=10
# a name to a value
a=10
b=20
print(a)
print(b)

c=35
f=1.8*c+32
print(f)

c=40
f=1.8*c+32
print(f)

# arithmetic operators
# +, -, *, /, //(floor division), **(exponentiation), %(modulus)

# Assignment operator
# =, +=, -=, *=, /=, //=, **=, %=

x=5
x+=3 # x=x+3
print(x)

x-=2 # x=x-2
print(x)

x*=4 # x=x*4
print(x)

x/=2 # x=x/2
print(x) # 12.0

x//=3 # x=x//3
print(x) # 4.0

x**=2 # x=x**2
print(x) # 16.0

x%=5 # x=x%5
print(x)

x+=3
print(x)

temp=35
age=20
age2=21
salary=20000
hyd_temp=40
mumbai_temp=35


# Data types
# 1. int - integer
# 2. float - decimal numbers
# 3. str - string
# 4. bool - boolean (True or False)

a=10
b=3.14

print(type(a))
print(type(b))
print(type(10))
print(type(10.5))

# literals
# 1. int literal - 10, 20, -5
# 2. float literal - 3.14, -0.5

c="hello"
print(type(c))
d=True
e=False
print(type(d))
print(type(e))

# Type conversion
# implicit type conversion - python automatically converts one data type to another
# explicit type conversion - we manually convert one data type to another using built-in functions like int(), float(), str(), bool()
a=10
b=float(a)
print(b)

a=10.5
b=int(a)
print(b)

# int() is mainly used when you want to convert a string to an integer
a="10"
b=int(a) # "10" -> 10
print(b)
print(b+5) 

a="10.5"
# b=int(a) # "10.5" -> error
b=float(a) # "10.5" -> 10.5
print(b+1)

print(int(10.5))
print(int(10))
print(int("10"))
# print(int("10.5")) # error

print(float(10))
print(float(10.5))
print(float("10"))
print(float("10.5"))

# str()
print(str(10)) # "10"
print(str(10.5)) # "10.5"
print(str(True)) # "True"
print(str(False)) # "False"
print(str(b)) # "10.5"
print(str("z")) # "z"
# print(str(z))

# bool()
print(bool(0)) # False
print(bool(0.0)) # False
print(bool("")) # False
print(bool(1)) # True
print(bool(-1)) # True
print(bool("hello")) # True


