"""
This is a comment
written in
more than just one line
"""

# integer  literal
x=12
y=12.34
z="Gopi"
i=True
j=False
k=[1,2,3,4]
a=("mango","apple","kiwi")

# camelCase

myVariableName="Gopi"

#PascalCase

MyVariableName="Muppuri"

#Snake Case

my_variable_name="Gopi Muppuri"

# Many Values to Multiple Variables

fi,se,th=1,2,3
print(fi,se,th)


# One Value to Multiple Variables

fo=fi=si=6
print(fo,fi,si)

# Unpack a Collection

x,y,z=a


# global variables

def myfunc():
    global x
    x="name"
    print(x)

myfunc()
print(x,y,z)