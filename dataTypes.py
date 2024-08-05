# built-in Data types

"""

Python has the following data types built-in by default, in these categories:

        Text Type:	str
        Numeric Types:	int, float, complex
        Sequence Types:	list, tuple, range
        Mapping Type:	dict
        Set Types:	set, frozenset
        Boolean Type:	bool
        Binary Types:	bytes, bytearray, memoryview
        None Type:	NoneType
"""

# Python Number Types

"""

        1.int
        2.float
        3.complex

"""

#int
x=10
y=-10

z=3217674664736423648324912834328489438946893656457647569486892349836489683496132896481

bi=0b1110
print(x,type(x),y,type(y),z,bi)

# float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# type conversions

a=-10

print(float(a),complex(a))

# float

a=-10.234

print(int(a),complex(a))

# complex

a=12+2j

# str
s="my name is Gopi"
print(s[3 : -1 : -1])

# contact the string
s1="Hello"
s2="World"

print(s1+" " +s2)
print(f"{s1} {s2} \n testing")


