 # f = open("exercise.txt","r")
# x = f.read()
# # print(x)
# y = x.split(";")
# # z = y.replace("\n"," ")

# li = [i.replace("\n"," ") for i in y]
# li = list(filter(None,li))
# # print(li)


# li = ["m","o","m"]
# y = list(reversed(li))
# print(y)
# if li == y:
#     print("palindrome")
# else:
#     print("not a palindrome")


# li = list((500,100,1,85,1000,91))
# li.sort(reverse=True)
# print(li[0:3])


# li_1 = ["5","6","8","11","15","25"]
# li_2 = ["10","9","2","1","5","6"]
# for i in li_1:
#     for x in li_2:
#         # y = i % x
#         pass
#     print(i,x,end="\n")
#     # print(y)


# def swap_num(user,a,b):
#     name = user
#     print("user {} befor swapping {} {}".format(name,a,b))
#     x = a
#     a = b
#     b = x
   
#     print("user {} after swapping {} {}".format(name,a,b))


# swap_num("sindhu",10,5)



# convert below two list into dictionary and converted dictionary should be inside list
# 'elemnt' implimenting list comprehension
# x = ["carname","model","year","color"]
# y = [("ford dodge","svrt","2018",["red","blue","black","yellow"]),("suzuki","alpha","2020",
#                                                     ["gray","blue","black","white"])]
# elemnt = [dict(zip(x,i)) for i in y]
# print(elemnt)


# update below key 'colour' to 'color' and then map below two tuples and convert to dictionary
# x = ("carname","model","year","colour")
# y = ("ford dodge","svrt","2018",["red","blue","black","yellow"])

# z = list(x)
# z[3] = "color"
# print(z)
# d = dict(zip(z,y))
# print(d)


# write a python script to
# to find the area of a rectangle
# circumference of a circle
# creat seperate function for above problems where function should be callable and usable
# # in another script as a module
# def rectangular_area(length,width):
#     x = (1/2)*length*width
#     print(x)

# def circumference_circle(radius):
#     pi = 3.14
#     c = 2*pi*radius
#     print(c)

# l1 = ['a','e','i','o','u']
# l2 = ['apple','bench','orange','elephant']

# for i in l2:
#     for j in l1:
        
#             print(j+i)
#         else:
#             print(j)



# #tringal
# r = int(input("enter the number : "))
# for i in range(0,r):
#     for j in range(0,i+1):
#         print("*",end = " ")
#     print()



# #calendar problem
# import calendar
# s = calendar.prcal(2024)
# print(s) 




# python script to convert celsius to fahrenheite
# c = int(input("enter the temperature in degree celsius : "))
# f = (9/5)*c + 32
# print(f"the tempreture is {f} degree Fahrenheit")


#script to check poditive number or negative number
# n = int(input("enter the number : "))
# if n > 0:
#     print("the given number",{n},"is positive")
# else:
#     print("the given number",{n},"is negative")


#script to fine leap year or not
# y = int(input("enter the year : "))
# if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#     print(f"{y} is a leap year")
# else:
#     print("not a leap year")



#script to calculate fibonacci series
# x = 0
# y =1
# for i in range(0,10):
#     temp = x + y
#     print(temp)
#     x = y
#     y = temp


#script to find factorial of a number
# x = int(input("enter the number"))
# fact=1
# for i in range(1,x+1):
#     fact = fact *i
# print("The factorial of {} is {}".format(x,fact))


#write a python script where create a class student and pass arguments as student_name,marks of
#5 subjects and use class method to calculate average marks of student
# class Student:
#     def display(self,name,sub1,sub2,sub3,sub4,sub5):
#         self.name = name
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3
#         self.sub4 = sub4
#         self.sub5 = sub5

#     def marks(name,sub1,sub2,sub3,sub4,sub5):
#         print(name)
#         print("subject 1 marks are {}".format(sub1))
#         print("subject 2 marks are {}".format(sub2))
#         print("subject 3 marks are {}".format(sub3))
#         print("subject 4 marks are {}".format(sub4))
#         print("subject 5 marks are {}".format(sub5))
#         print((sub1+sub2+sub3+sub4+sub5)/5)
    
# o = Student
# o.marks("sindhu",56,63,98,98,56)



#write a python script to solve below mentioned problems
# get count of None objects from the list
# remove all none elements from below list-
# list_1 = ['Mahesh',None,'Sindhu','Aniketh',None,'Shwetha',None,None,None,'Pushpa','Rakesh','Senthil',None] 
# list_1 = ['Mahesh',None,'Sindhu','Aniketh',None,'Shwetha',None,None,None,'Pushpa','Rakesh','Senthil',None] 
# c = list_1 .count(None)
# print("Count of None objects in the given list : ", c)
# x = list(filter(None,list_1))
# print(x)


#write a python script to create class employee and with the help of get attribute display employe 
# details with the help od set attribute allow 
#feature to modify employee salary
#>convert the emp details passed as arguments inside class to dictionary using dict 
# constructor/instance method
#> also solve the object Ambiguty problem
#example
#-ouput
#before using set attribute,
#emp name : Sindhu
#emp salary : 50000
#after using set attribute.
#{'name':'sindhu','salary': 50000}
#{'name':'sindhu','salary': 75000}
# class Employee:
#     def __init__(self,emp_name,emp_salary):
#         self.emp_name=emp_name
#         self.emp_salary=emp_salary

# a = Employee('sindhu',50000)
# print(getattr(a,'emp_name'),getattr(a,'emp_salary'))
# u = int(input("enter the employee salary : "))
# setattr(a,'emp_salary',u)
# print(getattr(a,'emp_name'),getattr(a,'emp_salary'))
# print(a.__dict__) 

# data from file
# f = open("emp.txt","r")
# li=[]
# for i in f:
#     li.append(i.strip())
    

    # a = Employee()
    # print(getattr(a,'emp_name'),getattr(a,'emp_salary'))

 















#write a python script to solve below mentioned problems
# > sort the list in Descending order
# >find mean value,median value,middle element from the list print the out put with its respected position also
# >highest frequency of the element from below list
# li = [500,759,1,10,9,200,76,900,55,65,1000,355555,55,9,1,9]
# example
#  - output
#  sorted list in descending order
#  []
#  mean value - pos[element], element
#  median value - pos[element], element
#  middle value - pos[element], elemetnt  
#  Higest frequency - pos[element], element, frequency
li = [500,759,1,10,9,200,76,900,55,65,1000,355555,55,9,1,9]
li.sort(reverse = True)
print(li)
a = len(li)
m = round(a/2)
print('pos[{}]'.format(m),li[m])

# print(a)
# s=0
# for i in li:
#     s+=i
#     print(s)
#     mean = s/a
#     print(f"mean value is {mean}")
# median = 
# print(f"\nMedian Value is {median}")



 