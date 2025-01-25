#INFO2602-LAB1

x=10
x=23
y=5
z = ( x + y)/x + (78%3)

name="bobby"
age=12
height=6.5
hasDate=False
comp=7j

message = f'Hi my name is {name} I am {age} years old'
print (message)

intHeight=int(height)
strHeight=str(height)
floatHeight=float(intHeight)
ageType=type(age)

name=input("Enter name:")
print(name)

if 3 > 5:
  print("more")
else :
 print("less")


mark = input("Enter mark: ")
mark = int(mark)
if mark > 70 :
  print("A")
elif mark > 60:
  print("B")
elif mark > 50:
  print("C")
else :
  print("F") 

i = 1
while i < 10:
 print(i)
 i+=1
else:
 print("This is run when the loop condition is no longer met")


list = ["bob", "sally", "john"]
for j in list:
 print(j)

for i in range(0, 10, 2):
 print(i)

#use i+=value instead of i++

#FUNCTIONS 

def add(a,b):
  return a+b

def printPerson(name,age,height):
  print(name,age,height)

printPerson(age=12, name='bob',height=5)

def sayHello(fname, lname='Smith'):
  print('Hello '+fname+' '+lname)

sayHello('John')
sayHello('Bill', 'Young')

list = ['item1', 'item2', 'item3']
list2 = [12, 33, 45, 58, 23]

print(list)

print(list2[-1])

print(list2[2:4])

print(len(list2))

list.append('item4')

item4 = list.pop()

list3 = list2.copy()

num=[1,2,3,4]
doubled=[n*2 for n in num]
print(doubled)
odd=[n for n in num if n%2==1]
print(odd)

num = [ 1, 2, 3, 4]
[first, second, *rest] = num
print(first)
print(second)
print(rest)

num2 = [5, 6]
num3 = num + num2
print(num3) 

num4 = num2.copy()

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple); 
print(thistuple[0]); 

data = [ 20, 3, 20, 42, 2, 3, 10, 32, 2]

myset = {0, 1}

for num in data:
 myset.add(num)

print(myset)
num_unique = len(myset)

mydict = {
        "name":"bob",
        "age": 34
}

print(mydict)

print(mydict['age'])

mydict['height'] = 7

for key in mydict:
        print(key)

for key in mydict:
        print(mydict[key])

if 'weight' in mydict:
        print(mydict['weight'])
else:
        print('no weight property!')

class Person:

  def __init__(self, name, height, weight):
    self.name = name
    self.height = height
    self.weight = weight

  def sayHello(self):
    print("Hello! I'm a person, my name is", self.name)

class Student(Person):
    def __init__(self, stid, name, height, weight):
        super().__init__(name, height, weight)
        self.stid = stid
        
    def sayHello(self):
        print("Hello! I'm a student, my name is", self.name)


bob = Person('bob', 12, 34)
sally = Student(123, 'sally', 7, 34)

bob.sayHello();
sally.sayHello();

print(bob.name);