# ***************************************** Class, obj & self ***************************************** 
# class Dog:          # Class
#     attr1 = "mammal"
#     attr2 = "dog"
 
#     def fun(self):      # A default keyword refer to object.
#         print("I'm a", self.attr1)
#         print("I'm a", self.attr2)

# obj = Dog()         # Object
 

# print(obj.attr1)
# obj.fun()

# ***************************************** __init__ method ***************************************** 
# class Person:

#     def __init__(self, name):
#         self.name = name

#     def say_hi(self):
#         print('Hello, my name is', self.name)
   
# obj = Person('Mazhar')
# obj.say_hi()

# ***************************************** Class and Instance Variables ***************************************** 

# class Person:  
#     def __init__(self, name, fname):       
#         self.name = name
#         self.fname = fname
 
#     def fun(self):    
#         print("My name is : ", self.name,self.fname)

# obj = Person("Mazhar", "Nasser")        
# obj.fun()

# ***************************************** Destructors  ***************************************** 
# class Employee:
     
#     def __init__(self):
#         print('Employee created.')

#     def __del__(self):
#         print('Destructor called, Employee deleted.')

#     def salary(self):
#         pass
 
# obj = Employee()
# del obj
# # obj.salary        # through an error bcz obj deleted

# ***************************************** Inheritance  ***************************************** 

# class Person:  
#     def __init__(self, name, fname):       
#         self.name = name
#         self.fname = fname
 
#     def fun(self):    
#         print("My name is : ", self.name,self.fname)

# class Email(Person):
#     pass

# obj = Email("mazhar", "naseer")

# obj.fun()
# ***************************************** Encapsulation   ***************************************** 
# class Base:
#     def __init__(self):
        
#         self._a = 2         # Protected variable
#         self.__b = 5        # Private variable
 
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print(self._a)
#         #print(self.__b)      # through error because b is private variable

# obj = Derived()

# ***************************************** polymorphism ***************************************** 

# class Teacher():
#     def name(self):
#         print("Haroon Raheed")
  
#     def language(self):
#         print("Urdu")
  
#     def city(self):
#         print("lahore")
  
# class Student():
#     def name(self):
#         print("Ali Raza")
  
#     def language(self):
#         print("Punjabi")
  
#     def city(self):
#         print("Karachi")
 
# def func(obj):
#     obj.name()
#     obj.language()
#     obj.city()
  
# obj_tchr = Teacher()
# obj_stu = Student()
  
# func(obj_tchr)
# func(obj_stu)

# ***************************************** Class or Static Variables ***************************************** 
# class Employee:
#     compny = 'ABC Tech'                 
#     def __init__(self,name,id):
#         self.name = name            
#         self.id = id           

# a = Employee('HAbib', 1)
# b = Employee('FAisal', 2)
  
# print(a.compny) 
# print(b.compny)  
# print(a.name)    
# print(b.name)  
# print(a.id)   
# print(b.id)   

# ***************************************** Class or Static Variables ***************************************** 
# from datetime import date

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def fromBirthYear(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)

#     def display(self):
#         print(self.name + "'s age is: " + str(self.age))

#     @staticmethod
#     def address():
#         print("c Block, Phase 3, DHA Lahore")

# person = Person('Ali', 25)
# person.display()

# person1 = Person.fromBirthYear('Arslan',  1985)
# person1.display()

# person.address()