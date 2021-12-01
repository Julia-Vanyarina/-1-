# -PYTHON#№1
class First:
    color = "red"
    def out(self):
         print(self.color + "!")

obj1 = First()
obj2 = First()
print(obj1.color)
print(obj2.color)
obj1.out()
obj2.out()



#№2
class Second:
  color="red"
  form="circle"
  number=2

  def changecolor (self, newcolor):
    self.color = newcolor
  def changeform (self, newform):
    self.form = newform
  def changenumber (self, newnumber):
    self.number = newnumber
obj1 = Second()
obj2 = Second()
obj3 = Second()
print(obj1.color, obj1.form, obj1.number)
print(obj2.color, obj2.form, obj2.number)
print(obj3.color, obj3.form, obj3.number)
obj1.changecolor="green"
obj2.changecolor="blue"
obj2.changeform= "oval"
obj3.changecolor="pink"
obj3.changeform="square"
obj3.changenumber= 9
print(obj1.changecolor, obj1.form, obj1.number)
print(obj2.changecolor, obj2.changeform, obj2.number)
print(obj3.changecolor, obj3.changeform, obj3.changenumber)



#№3
class YesInit:
  def __init__(self,one,two):
    self.fname=one
    self.sname=two
obj1= YesInit("Peter", "Ok")
print(obj1.fname, obj1.sname)
class NoInit:
  def names(self,one,two):
    self.fname=one
    self.sname=two
obj1=NoInit()
obj1.names("Peter","Ok")
print(obj1.fname, obj1.sname)




#№4
class YesInit:
  def __init__(self,one="noname",two="nonametoo"):
    self.fname=one
    self.sname=two
obj1=YesInit("Sacha","Tu")
obj2=YesInit()
obj3=YesInit("Spartak")
obj4=YesInit(two="Harry")
print(obj1.fname, obj1.sname)
print(obj2.fname, obj2.sname)
print(obj3.fname, obj3.sname)
print(obj4.fname, obj4.sname)






#№5
class fruits:
  def __init__(self,w,n=0):
    self.what=w
    self.numbers=n

f1=fruits("apple",150)
f2=fruits("pineapple")

print(f1.what, f1.numbers)
print(f2.what, f2.numbers)

class banan(fruits):
  def __init__(self,w,c,n):
     super(). __init__(w)
     self.color = c
     self.numbers=n
    
f3=banan("banan","white", 150)  
print(f3.color, f3.numbers)



#№6
class Building:
  def __init__(self, w,c,n=0):
    self.what=w
    self.color=c
    self.numbers=n
    self.mwhere(n)
 
  def mwhere(self,n):
   if n<=0:
     self.where="отсутствуют"
   elif 0<n<100:
     self.where="малый склад"
   else:
     self.where="основной склад"
  def plus(self,p):
   self.numbers=self.numbers+p
   self.mwhere(self.numbers)
  def minus(self,m):
   self.numbers=self.numbers-m
   self.mwhere(self.numbers)
m1=Building("Доски","белые",50)
m2=Building("Доски","коричневые",300)
m3=Building("кирпичи","белые")
print(m1.what,m1.color,m1.where)
print(m2.what,m2.color,m2.where)
print(m3.what,m3.color,m3.where)
m1.plus(500)
print(m1.numbers,m1.where)



#2 задание
class Human:
  def __init__(self,name,surname):
    self.name = name
    self.surname = surname

  def height(self,heigh):
    self.heigh = heigh
    print(self.heigh)
  def weight(self):
    print(self.name,self.surname, "рост")

a = Human("Петя", "Иванов")
a.height(180)
a.weight()

b = Human("Саша", "Сергеев")
b.height(209)
b.weight()




#№7
class Things:
  def __init__(self,n,t):
    self.namething=n
    self.total=t
th1=Things("table",5)
th2=Things("computer",7)

print(th1.namething,th1.total)
print(th2.namething,th2.total)

th1.color="green"
th2.color="blue"

print(th1.color)
print(th2.color)




#№8
class Table:
  def __init__(self,l,w, h):
    self.long = l
    self.width = w
    self.height = h
  def outing(self):
    print(self.long, self.width, self.height)

class Kitchen(Table):
  def howplaces(self, n):
    if n < 2:
      print("It is not kitchen table")
    else:
      self.places = n
  def outplases(self):
    print(self.places)

class Worker(Table):
  def weight(self,we):
    self.we = we
    print(self.we)
  def name(self,name):
    self.name = name
    print(self.name)

t_room1 = Kitchen(2,1,0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplases()
t_2 = Table(1,3,0.7)
t_2.outing()
t_3 = Worker(6,9,11)
t_3.outing()
t_3.weight(80)
t_3.name("Julia")





#Практическое задание
class figure:
  def __init__(self,l, w, h, c = "white"):
    self.c = c
    self.l = l
    self.w = w
    self.h = h

  def changecolor(self, newcolor):
    self.color = newcolor

class oval(figure):
  def mina(self, name):
    self.name = name

class square(figure):
  def mina1(self,surname):
    self.surname = surname
h2 = oval(figure, 8, 10)
h1 = figure(15,6,3)
h2.changecolor = "green"
h1.name = "Oval"
h1.l = "10 см"
h1.w = "8 м"
h2.l = "4 см"
h2.w = "4 м"
h2.surname = "Square"
print(h1.name,",",h1.c,",",h1.l,"на", h1.w)
print(h2.surname,",",h2.changecolor,",", h2.l,"на",h2.w)
