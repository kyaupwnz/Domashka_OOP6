class Employee:
  __slots__ = ('first', 'last')
  def __init__(self, first, last):
    self.first = first
    self.last = last
  @property
  def fullname(self):
    return f'{self.first} {self.last}'

  @property
  def email(self):
      return self.first + "." + self.last + "@gmail.com"
  @fullname.setter
  def fullname(self, _fullname):
    self.first = _fullname.split()[0]
    self.last = _fullname.split()[1]
  
  @fullname.deleter
  def fullname(self):
     self.first = "None"
     self.last = "None"

emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# John
# John.Smith@email.com
# John Smith

emp_1.fullname = "Corey Schafer"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# Corey
# Corey.Schafer@email.com
# Corey Schafer

del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# None
# None.None@email.com
# None None
