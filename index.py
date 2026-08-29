# exponent
# a=4
# print(a*a)

# # flooer division 
# x=9
# y=2
# print(x//y)

# # relational operator

# a=20
# b=20
# print(a==b)

# a=12
# b=12
# print(a!=b)

# a=12
# b=11
# print(a<b)

# age=18
# print(age>=18)

# a=20
# a=a+5
# a+=5
# print(a)



# a="haadi"
# print(type(a))

# a=10
# print(type(a))

# b=10.6
# print(type(b))

# c=True
# print(type(c))

# lt=['ayat','khan','ayaan','haadi',12,89]
# lt[1]='ayaan'
# lt.append('zarah')
# lt.insert(1,'sarah')
# lt.remove(12)
# lt.pop(5)
# print(lt)

# tp=('ayat','khan','haadi',120,90)
# tp[3]='ubaid'
# print(tp)


# dt={
#     "name":"haadi",
#      "roll-no":2,
#      "address":"sgr",
#      "naaw":"hadu"
# }
# dt['name']='hadiya'
# dt['email']='h@gmail.com'
# dt.pop('naaw')
# del dt['email']
# print(dt)


# lt=[['wasiq','true',20],['haadi','false',89],['hanan','khan',15]]
# lt[0][0]='ayar'
# lt.append('saboor')
# lt[0].insert(2,'umar')
# lt[0].pop(3)
# del lt[2][2]
# print(lt)


# lt=[[['haadi','true',20],['huda',25,'false']],[['wasiq',90,120],['naira','khan','23']]
#     ,[['zara','sara',35],['ayat',89,70]]]

# lt[1][0][2]='saniya'
# lt[0][0].insert(1,'ubaid')
# lt[0][1].append('sadiya')
# del lt[0][1][0]
# print(lt)

# dt={
#     "name":{"firstname":"haadi","lastname":"bhat"},
#     "address":{"state":"kashmir","pincode":190001},
#     "subject":{"major":"social work","minor":"education"}
# }

# dt["name"]["firstname"]='zarah'
# dt['occupation']={"designation":"jr assnt","employ-code":9292}
# del dt["occupation"]
# print(dt)

# dt={
#     "1":{"name":{"firstname":"haadi","lastname":"bhat"},"address":{"state":"sringar","pincode":190001}},
#     "2":{"name":{"firstname":"zain","lastname":"khan"},"address":{"state":"gbl","pincode":190021}},
#     "3": {"name":{"firstname":"khan","lastname":"toiba"},"address":{"state":"kupwara","pincode":190022}}
# }

# dt["1"]["name"]["firstname"]='ayat'
# del dt["1"]["address"]
# print(dt)


# grade=input("enter your grade:-")
# if grade=='a':
#     print("topper")
# else:
#     print("fail") 


# grade=input("enter your grade:-")
# if grade =='a':
#     print("topper")
# elif grade=='b':
#     print("good")
# elif grade =='c':
#     print("average")
# else:
#     print("fail")


# age=int(input("enter your age:-"))
# if age >=18:
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
# elif x==0:
#     print("you entered zero")
# else:
#     print("negative number")


# username=input("enter your name:-")
# password=input("enter your password:-")
# if username=='haadi':
#     if password=='123456':
#         print("login sucessfull")
#     else:
#         print("invalid password")
# else:
#     print("incorrect username")


# girl=int(input("girl's age:-"))
# boy=int(input("boy's age:-"))

# if girl>=18 and boy>=18:
#     print("allowed")
# else:
#     print("not allowed")

# girl=int(input("girl's age:-"))
# boy=int(input("boy's age:-"))

# if girl>=18 or boy>=18:
#     print("allowed")
# else:
#     print("not allowed")


# a=12
# b=20
# c=30
# if a>=b and a>=c:
#     print(a, "is greater")
# elif b>=a and b>=c:
#     print(b,"is greater")
# else:
#     print(c,"is greater")


# try:
#     n1=int(input("enter ist number:-"))
#     op=input("+,-,*,/:-")
#     n2=int(input("enter 2nd number:-"))

#     if op =='+':
#         print(n1+n2)
#     elif op =='-':
#         print(n1-n2)
#     elif op =='*':
#         print(n1*n2)
#     elif op =='/':
#         print(n1/n2)
#     else:
#         print('invalid operator')
# except ZeroDivisionError:
#     print("cannot divide by zero")


# for i in range(10):
#     print(i)


# tab=int(input("enter an number:-"))
# for i in range(1,11):
#     res=tab * i
#     print(tab,'x',i,'=',res)


# for i in range(1,20,2):
#     print(i)


# lt=['haadi','umer',12,80,'true',90]
# for dt in lt:
#     print(dt)



# dt={
#     "name":"haadi",
#     "roll-no":3,
#     "address":"sgr"
# }
# for key,value in dt.items():
#     print(key,':-',value)



# for i in range(10):
#     if i ==5:
#         break
#     print(i)


# for i in range(10):
#     if i==5:
#         continue
#     print(i)


# for i in range(100):
#     if i%2==0:
#         print(i,'is even')
#     else:
#         print(i,'is odd')


# x=int(input("enter an number:-"))
# if x<=1:
#     print("semi prime")
# else:
#     for i in range (2,x):
#         if x % i==0:
#             print("not prime number")
#             break
#     else:
#         print("prime number")


# n=[12,25,90,80,75,150,120,18]
# flag=0
# x=int(input("enter an number:-"))
# for num in n:
#     flag=1

# if flag ==1:
#     print(x,'is in list')
# else:
#     print(x,"is not in list")


# word=input("enter an number or word:-")
# rev=''
# for ch in word:

#     if word == 'rev':
#      print(word , "is palindrome")
# else:
#     print(word , "is not  pallindrome" )


# lt=[12,25,90,21,70,90,120,80]
# print(lt[1:5])
# print(lt[:])
# print(lt[-2])
# print(lt[::3])
# print(lt[2:])
# print(lt[-1:]


# lt.sort()
# print(lt[-1])


# word=input("enter an sentence:-")
# word.split()
# print(len(word.split()))


# lt=[12,30,5,10,9,8,60,109,150]
# lt.sort(reverse=True)
# print(lt)



# i=0
# while i <30:
#     i=int(input("enter an number:-"))
#     print(i)


# while True :
#     x=int(input("enter an number:-"))
#     if x % 2 == 0:
#         print(x,'is even')
#     else:
#         print(x,'is odd')
#         cht=input("do u want to continue:-")
#         if cht == 'no':
#             break


# while True:
#     n=int(input("enter an number:-"))
#     if n<=1:
#         print('semi prime')
#     else:
#         for i in range(2,n):
#             if n%2 ==0:
#                 print("not prime")
#                 break
#         else:
#             print("prime number")
#     cht= input("enter yes to continue:-")
#     if cht != 'yes':
#        break


# try:
#     x=10/0
# except ZeroDivisionError:
#     print("cannot divide by zero")


# # value error
# try:
#     num=int(input("enter an number:-"))
#     print(num)
# except ValueError:
#     print("invalid value")

# # type error
# try:
#     a="12"+2
#     print(a)
# except TypeError:
#     print("type mismatch ")

# NameError

# try:
#     print(a)
# except NameError:
#     print('a is not defined')


# try:
#     lt=[12,14,10]
#     print(lt[3])

# except IndexError:
#     print("this item doesn't belong in list")


# try:
#     dt={
#         "name":"haadi"
#     }
#     print(dt['age'])
# except KeyError:
#     print("this key doesn't belong to dt")

# try:
    # a=10
    # a.append(20)

# except AttributeError:
    # print("this thing doesn't belong to this")

    



# file=open(r'C:\Users\YOUSUF\Desktop/okay/haadi.txt','w')
# file.write("hello haadi")
# file.close()


# with open('haadi.txt','w')as f:
#     f.write("hello hadu")




















