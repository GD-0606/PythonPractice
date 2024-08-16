"""
    why i need to move to the oop apprach instead pop ?
        1.no data secuirty.
"""



"""
To say a languge is Object Oriented , It has to sastisfy the following Principles.
			
			1. Classes
			2. Objects
			3. Data Encapsulation
			4. Data Abstraction
			5. Inheritance
			6. Polymorphism
			7. Message Passing(already discussed )

"""
"""
    class is used to develop the programmer defined dataType.
    It is a collection of variables (data members) and methods.
    memory space is created when we are creating the objects w.r.t className .
"""

"""
    Syntax for defining the class in python.
    class <class-name>:
	         Class Level Data Members
		 def InstanceMethodName(self,List of formal params if any):
		       ---------------------------------
		       Specify Instance Data Members---Perform Specific Operations
		       --------------------------------

		@classmethod
		def   classlevelmethodname(cls,list of Formal params if any)
		       --------------------------------------
		       Specify Class Level Data Members--Perform Common Operations
		       --------------------------------------
		@staticmethod
		def   staticmethodname(list of formal params if any):
		        --------------------------------------
			Performs Utility / Universal  Operations
			--------------------------------------

"""
class MyClass:
    x=10
# object creation
obj1=MyClass()

print(obj1.x,MyClass.x)


"""
    constructor is a special method initiated by the pvm do not leaving the object empty.
"""
# class Person:
#     #constructor
#     def __init__(self):
#         print("I am a default constructor")
#         self.a=10
#         self.b=20
#         print("Value of a is {}".format(self.a))
#         print("Value of b is {}".format(self.b))

# #object 
# per1=Person()
# per2=Person()
# print(per1.b,per2.a)

class Person:
    section="B"
    #constructor
    def __init__(self,id,name,age):
        print("I am a default constructor")
        self.name=name
        self.age=age
        self.id=id
        print("Person{} :  {} and section is {}".format(self.id,self.name,self.section))

#object 
per1=Person(1,"Gopi",22)
per2=Person(2,"Loka",30)

"""
    Data Members and Methods in class Structure 
"""
class Person:
    #class level member.
    section="B"
    #constructor
    def __init__(self,id,name,age):
        print("I am a default constructor")
        # instance level members
        self.name=name
        self.age=age
        self.id=id
        print("Person{} :  {} and section is {}".format(self.id,self.name,self.section))
    def get_age(self):
        print(f"Age is {self.age}")

    def get_info(self):
        self.get_age()
        print(f"sections is {self.name}")
    @classmethod
    def get_section(cls):
        print(f"Section is {cls.section}")
    @staticmethod
    def add(x,y):
        print( x+y)
#object 
per1=Person(1,"Gopi",22)
per2=Person(2,"Loka",30)
per2.get_info()