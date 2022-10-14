class Person:
  def __init__(self, name, age, city):
    self.name = name
    self.age = age
    self.city = city

p1 = Person("John", 36, 'hyd')

print(p1.name)
print(p1.age)

#Inheritance
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019