class Student:

  c_name = "1학년 3반"

  def __init__(self, name, pos):
    self.name = name
    self.pos = pos

stu1 = Student("권민세", "반장")
stu2 = Student("박태인", "꺽다리")

Student.c_name = "2학년 1반"

print(stu1.name + stu1.pos + Student.c_name)
print(stu2.name + stu2.pos + Student.c_name)

# ----------------------------

class Account:
  interest_rate = 0.02

  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount

  def apply_interest(self):
    self.balance += self.balance * Account.interest_rate

acc = Account("권민세", 10000)
acc.deposit(5000)
acc.apply_interest()
print(f"{acc.owner}님의 최종 잔액: {acc.balance}원") 

#-------------------------------

class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("동물이 소리를 냅니다")

class Dog(Animal):

  def make_sound(self):
    print('강아지가 멍멍 하고 웁니다')

dog1 = Dog('개죽이')
dog1.make_sound()
print(dog1.name)