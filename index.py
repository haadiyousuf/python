# exponents

# a=3
# print(a*a)


# flooer division

# x=9
# y=2
# print(x//y)


# # relational operator
# a=12
# b=12
# print(a==b)


# a=12
# b=12
# print(a!=b)


# a=12
# b=11
# print(a<b)


# age=18
# print(age>=12)


# age=12
# print(age<=12)


# a=12
# a=a+5
# a+=5
# print(a)


# data types tells which type of data  a particular variable holds

# int--it holds proper numerical value eg:12
# float--it holds point values eg:12.56
# string--it holds textual data eg:'wasiq'
# boolean--it holds tru/false values


# a="haadi"
# print(type(a))


# a=10
# print(type(a))


# a=10.6
# print(type(a))


# c="true"
# print(type(c))



# list stores multiple items in a single variable,it is hetrogenous,it is orderd,
# it is mutable (changeable)
# indexing is a numerical location of an items presented in list

# lt=['haadi','ayaan','khan',12,'true']
# lt[2]='raziya'
# lt.append('ayat')
# lt.insert(1,'heenu')
# lt.remove('true')
# lt.pop(4)
# print(lt)


# tuple stores multiple items in a single variable ,it is mutable (unchangeable),
# it is indexed ,it is ordered

# tp=('haadi','khan',21,89,'true')
# tp[1]='heenu'
# print(tp)



# set stores multiple items in a single variable,it is un-ordered,it is un-indexed,
# it does not allow duplicate

# st={'haadi',22,'true','khan',45,78,90}
# st.add('heenu')
# st.remove('true')
# print(st)


# dictionary stores multiple items in a single variable through the process of key-value pairs,
# it is orderd,it is key value pairs,it can have duplicates but not duplicate keys,it is mutable


# dt={
#     "name":"haadi",
#     "roll-no":21,
#     "address":"sgr"
    
    
# }

# dt['name']='hanan'
# dt['email']='haadi@gmail.com'
# dt.pop('email')
# del dt['roll-no']
# print(dt)


# lt=[['haadi','umar',21],['ubaid',12,89],['khan','false',70]]
# print(lt[0][1])
# print(lt[2][1])
# print(lt[1][0])
# print(lt[2][2])
# print(lt[1][2])

# lt[0][0]='ayat'
# lt.append('sahil')
# lt[0].insert(2,'heenu')
# lt[0].pop(3)
# del lt[1][1]
# print(lt)


# lt=[[['haadi','true',21],['wasiq',90,80]],[['sahil','false',77],['ayat','khan',12]],                     
# [['ayaan','zarah',15],['sarah','owais',88]]]

# print(lt[0][1][0])
# print(lt[2][1][0])
# print(lt[0][1][1])
# print(lt[2][0][1])
# print(lt[1][0][0])


# lt[1][0][0]='saniya'
# lt[0][0].insert(1,'ubaid')
# lt[0][1].append('saboor')
# del lt[0][1][0]
# print(lt)


# dt={
#     "name":{"firstname":"haadi","lastname":"yousuf"},
#     "address":{"state":"kashmir","pincode":190001},
#     "subject":{"major":"social work","minor":"education"}
# }

# dt["name"]["firstname"]='zarah'
# dt['occupation']={"designation":"jr assnt","employ_code":9797}
# del dt["address"]["pincode"]
# print(dt)


# dt={
#     "1":{"name":{"firstname":"haadi","lastname":"yousuf"},"address":{"state":"kashmir","pincode":19001}},
#     "2":{"name":{"firstname":"mir","lastnmae":"zain"},"address":{"state":"ang","pincode":190021}},
#      "3":{"name":{"firstname":"zarah","lastname":"jaan"},"address":{"state":"kupwara","pincode":192123}},
# }
# dt["1"]['name']['firstname']='ayat'
# del dt["1"]['address']['pincode']
# print(dt["1"])


# if -else
# indentation represents block of code= 1 indentation= 1 tab = 4 spaces


# grade = input("enter your grade:-")
# if grade =='a':
#     print("topper")

# else:
#     print("fail")


# grade=input("enter an grade:-")

# if grade =='a':
#     print("topper")

# elif grade=='b':
#     print("good")

# elif grade=='c':
#     print("average")

# else:
#     print("fail")


# input gives by default string value
# type casting means coverting one data type to another 


# age=int(input("enter your age:-"))

# if age>=18:
#     print("you can vote")

# else:
#     print("you cannot vote")



# x=int(input("enter an number:-"))

# if x%2==0:
#     print("even number")

# else:
#     print("odd number")



# x=int(input("enter an number:-"))

# if x>0:
#     print("positive number")

# if x==0:
#     print("you entered zero")

# else:
#     print("negative number")



# username = input("Enter your name:-")
# password = input("Enter your password:-")

# if username == 'haadi':
#       if password == '1234':
#             print("Login sucessfull")
#       else:
#             print("Invalid password")
# else:
#       print("Inncorect username")    




#And mean both condition should be true
#or means one of the conditions should be true
# girl = int(input("girl age:-"))
# boy = int(input("boy age:-"))

# if girl>=18 or boy>=18:
#       print("Allowed")
# else:
#       print("Not allowed")




# girl = int(input("girl age:-"))
# boy = int(input("boy age:-"))

# if girl>=18 and boy>=18:
#       print("Allowed")
# else:
#       print("Not allowed")

# a=40
# b = 21
# c=35
# if a>=b and a>=c:
#       print(a,"is greater")
# elif b>=a and b>=c:
#       print(b," is greater")
# else:
#       print(c,"is greater")


# Excetion handling means to simply identify an error and handle it gracefully
# try:
#       n1 = int(input("Enter ist number:-"))
#       op = input("+,-,x,/:-")
#       n2 = int(input("Enter 2nd number:-"))

#       if op =='+':
#             print(n1+n2)
#       elif op == '-':
#             print(n1-n2)
#       elif op =='x':
#             print(n1*n2)
#       elif op == '/':
#             print(n1/n2)
#       else:
#             print('Invalid operator')

# except ZeroDivisionError:
#       print("Cant divide by zero")


# loop is program that runs multiple time until the condition becomes true
  #i is an temporary variable which have default value of 0
  
# for i in range(10):
    #   print(i)


# tab = int(input("Enter an number:-"))
# for i in range(1,11):
#       res = tab * i
#       print(tab,'X',i,'=',res)


# for i in range(1,20,2):
#      print(i)


# lt=['wasiq','umer',12,89,'khan','true']

# for dt in lt:
#     print(dt)


# dt={
#   "Name":'Khan',
#   "Roll-no":21,
#   ' Adress':'Maisuma'
# }

# for key,value in dt.items():
#   print(key,':-',value)






# break stop current iteration
# for i in range(10):
    #  if i ==5:
      #  break
    #  print(i)

#continu skips current itteration
# for i in range(10):
  # if i ==5:
    # continue
  # print(i) 


# for i in range(100):
#   if i %2==0:
#     print(i,'is even')
#   else:
#        print(i,'is odd')




# x = int(input("Enter an number:-"))
# if x <=1:
#   print("Not prime")
# else:
#   for i in range(2,x):

#     if x % i ==0:
      
#       print("Not Prime number")
#       break
            
#   else:
#       print("Prime number")





# n = [12,25,90,21,46,101,31]

# flag = 0
# x = int(input("Enter an number:-"))
# for num in n :
#   if x == num:
#     flag =1
    
# if flag ==1:
#   print(x,'is in list')
# else:
#   print(x,"is not in list")
  

# word = input("Enter an number:-")
# rev = ''
# for ch in word:

#  rev = ch+rev
    
# if word == rev:
#     print(word,"is Palindrome")
# else:
#     print(word,"is not palindrome")



# lt = [12,25,90,21,46,101,31]
# print(lt[1:5])
# print(lt[:])
# print(lt[-2])
# print(lt[::3])
# print(lt[2:])
# print(lt[-1::])


# print(lt[4:])

# lt=[12,25,90,21,46,101,31]
# lt.sort()
# print(lt[-1])



# word = input("Enter an sentence:-")
# word.split() #split mean remove spaces
# print(len(word.split()))


# lt=[12,25,90,21,46,101,31]
# lt.sort(reverse=True)
# print(lt)


# i = 0
# while i <30:
#   i = int(input("Enter an number:-"))
#   print(i)





# while True:
#   x = int(input("Enter an number:-"))
#   if x % 2 == 0:
#     print(x,'is even')
#   else:
#     print(x,'is odd')
#   cht = input("Do you want to continue:-")
#   if cht =='no':
#     break



# while True:
#   n = int(input("Enter an number:-"))
#   if n <=1:
#     print("Not prime number")
#   else:
#     for i in range(2,n):
#       if n%i==0:
#         print("Not Prime ")
#         break
#     else:
#       print("Prime number")
#   cht = input("Enter yes to continue:-")
#   if cht !='yes':
#     break



# try:
#   x = 10/0
# except ZeroDivisionError:
#   print("Cant divide by zero")



#value error

# try:
#   num = int(input("Enter an number:-"))
#   print(num)
# except ValueError:
#   print("Invalid value")



#type error


# try:
#   a ="21"+2
#   print(a)
# except TypeError:
#   print("Type mismatch error")



# #name error


# try:
#   print(a)
# except NameError:
#   print('a is not defined')



# try:
#   lt= [12,78,90]
#   print(lt[3])
  
# except IndexError:
#   print("This item doesnt belong in list")



#key error
# try:
#   dt={
#     "name":"Michall"
#   }
#   print(dt['age'])
# except KeyError:
#   print("This key doesnt belong to dict")
  


# try:
#   a =10
#   a.append(20)
# except AttributeError:
#   print("This thing doesnt belong to this ")


# from  index1 import add,sq
# a = int(input("Enter an number:-"))
# b= int(input("Enter an number:-"))
# add(a,b)

# sq(a)



# def add(a,b):
  # return a+b


# print(add(10,12))



# add = lambda x,y: x+y
# print(add(11,12))


# sq = lambda x : x*x

# print(sq(3))



# even_odd = lambda x : 'even' if x%2==0 else 'odd' 

# print(even_odd(12))


# lt =[2,3,4,5,6]
# sq = tuple(map(lambda x: x*x,lt))
# print(sq)


# num =['11','21','55','10','89']
# ap = list((map(int,num)))
# print(ap)



# num =[1,2,3,4,5,6,7,8,9,10]
# sq = list(filter(lambda x: x%2==0,num))
# print(sq)


# names = ['BOB','ALICE','KHAN','UMER']
# n = list(map(str.lower,names))
# print(n)

# a = 'wasiq'

# print(a.capitalize())



# a = 'wasiq'

# print(a.upper())

# lt =[-90,21,-11,56,-90,11]
# n = list(filter(lambda x: x<0,lt))
# print(n)


# fruits = ['Kiwi','apple','Mango','pinanapple','pomogrante']
# n = list(filter(lambda x: len(x)>4,fruits))
# print(n)



# names = ['bob','umer','wasiq']
# n = list(map(str.capitalize,names))
# print(n)


#File handling is the process of creating updating and deleting a particulat file
#r stands reading file
#w stand creating a file
#a stands updating a paricular file
#x deleting a particular file



# Here we create a file
# file = open('file.txt','w')
# file.write("Hello from world")
# file.close()

# #here we read a particular file
# f = open('file.txt','r')
# data = f.read()
# print(data)


# f = open('file.txt','w')
# f.write('Hello world')


# f = open('file.txt','a')
# f.write(' ,from wasiq')
# f.close()

# f = open('file.txt','r')
# d = f.read()
# print(d)


# f = open('file.txt','x')
# f.close()

# f = open('f1.txt','w+b')
# f.write(b"Hello sibtain")
# f.close()



# file=open(r'C:\Users\user\Desktop.txt','w')
# file.write("hello haadi")
# file.close()



# with  open('haadi.txt','w')as f:
#     f.write("hello from haadi")



#Object oriented programing language is programing concept that make our more cleaner  more reusble and more in format and provide clean code
#Encapsulation
#Abstraction
#inheritence
#polymorphism


#class is a blueprint for creating an object
#encapsulation means bundling of data
#abstraction means hiding the complexity of code
# class ils:
#   def greet(self):
#     print("Hello from ils")
    
#   def bye(self,a,b):
#     print(a+b)
#     print(self)
#     print('bye from ils')


# i = ils()   #object is a insatnce  of classs
# i.greet()
# i.bye(12,13)

# #polymorphism means same function diffrent beaviour
# class dog:
#   def speak(self):
#     print("bow bow")

# class cat:
#   def speak(self):
#     print("Meow Meow")
    
# d = dog()
# c = cat()
# d.speak()
# c.speak()
  
  
# class Animal:
#   def walk(self):
#     print("Animal is walkimg")



# class dog(Animal):
#   def bark(self):
#     print("Dog barks!")
    
    
# d = dog()
# d.bark()
# d.walk()



#acess specifier allows us to manage the visibilty and acessibilty of class  atributes
#in python there no true acess specifier like jave , c++ and c#
# class ils:
    
#   def __init__(self):
#     print("Hello i am from constructor!")

#     self.__bye()
#   def hello(self):
#     print("Hello from ils")
    
#   def _ok(self):
#     print("Hello from protected function")
    
#   def __bye(self):
#     print("This is private function!")
    

# i = ils()
# i.hello()
# i._ok()
# i.__bye()






























   
   



      
      


      
      