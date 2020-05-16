class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#inheritance
class Student(Person):
  def __init__(self, fname, lname, age, gradyear):
    flname = fname + ' ' + lname
    super().__init__(flname, age)
    self.graduationyear = gradyear

p2 = Student('Mary', 'Jane', 23, 2019)
print('p2 name', p2.name)
print('p2 age', p2.age)    
print('p2 gradyear', p2.graduationyear)