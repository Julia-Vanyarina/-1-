#1
class Rectangle:
  def __init__(self, w = 0.5, h = 1):
    self.width = w
    self.height = h
  def square(self):
    return self.width * self.height

rec1 = Rectangle(5,2)
rec2 = Rectangle()
rec3 = Rectangle(3)
rec4 = Rectangle(h = 4)
print(rec1.square())
print(rec2.square())
print(rec3.square())
print(rec4.square())




#2
class Person:
  def __init__(self, n, s, q = 1):
    self.name = n
    self.surname = s
    self.skill = q
  def __del__(self):
    print("До свидания, мистер", self.name, self.surname)
  def into(self):
    return "{0} {1}, {2}".format(self.name, self.surname, self.skill)

worker = Person("И", "Котов", 3)
helper = Person("Д", "Мышев", 1)
maker = Person("О", "Рисов", 2)

print(worker.into())
print(helper.into())
print(maker.into())

del helper
print("Конец программы")
input()


#3
class Student:
  def __init__(self, surname, university, gender, grade, mail, phone,institute,faculty, group="АДЭУ-211"):
    self.surname = surname
    self.group = group
    self.university = university
    self.gender = gender
    self.grade = grade
    self.mail = mail
    self.phone = phone
    self.institute = institute
    self.faculty = faculty

  def __del__(self):
      print("Отчислен студент", self.surname, d[self.grade])
  def display(self):
      return "{0} {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}".format(self.surname, self.university, self.gender, self.group, d[self.grade],self.mail,self.phone, self.institute, self.faculty)


d = {2:"Задолжник", 4:"Ударник", 5:"Отличник"}
s1 = Student("Сидоров Иван Иванович", "МГУ","м", 5, "sidor@gmail.com", "899573788575", "ФилФак", "Английский язык")
print(s1.display())
s2 = Student("Петрова Мария Александровна", "МГТУ", "ж", 4, "petrmar@mail.ru", "898272838035", "МехМат", "Математика")
print(s2.display())
s3 = Student("Пупкин Михаил Владимирович", "МГПУ", "м", 3, "Pupmisha@gmail.com", "89398484595", "ИЦО", "Аналитика данных")
print(s3.display())

if s1.grade < s2.grade:
  del s1
elif s1.grade > s2.grade:
  del s2
else:
  print("МОЛОДЦЫ!")
  
  
  
  
  