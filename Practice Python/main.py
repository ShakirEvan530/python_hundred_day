#string


# first_name = "Bro"
# food = "Pizza"
# email = 'ausshakirahmed@gmail.com'
# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f"Your email is  {email}")

# ! integer 

# age = 25;
# quantity = 3;
# print(f"You are {age} years old")
# print(f"You are buying {quantity} items")


# !boolean type 
# is_Student = True
# if is_Student:
#     print("you are a student")
# else:
#     print("You are not a student")


# is_Student2 = False
# if is_Student2:
#     print("you are a student")
# else:
#     print("You are not a student")

#?typescript 
# name= "Bro Code"
# age = 25
# gpa = 3.2
# is_Student = True
# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_Student))
# print(name)

# name = input("What is your name?:")
# age = int(input("How old are you?:"))
# age = age+1;
# print(f"Hello {name}!")
# print("Happy birthday")
# print(f"you are {age} years old now")

# item = input("What item would you like to buy?:")
# price = float(input("What is the price of the item?:"))
# quantity = int(input("How many would you like to buy?:"))
# total = price * quantity
# print(f"You have bought {quantity}  {item}")
# print(f"Your total is: ${total}")

# !word games 
# adjective1 = input("Enter an adjective (description):")
# noun1 = input("Enter a noun(person , place , thing)")
# adjective2 = input("Enter an adjective(description):")
# verb1 = input("Enter a verb ending with 'ing")
# adjective3 = input("Enter an adjective(description):")
# print(f"Today i went to a {adjective1} zoo.")
# print(f"In an exhibition, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")

# import math 
# x = 4 
# y=9
# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# print(result)
# result1 = math.ceil(x)
# result2 = math.floor(y)
# print(result1)
# print(result2)

# radious = float(input("Enter the radious of a circle:"))
# circumference = 2*math.pi*radious
# print(f"The circumference is:{round(circumference,2)}")

# age = int(input("Enter your age:"))

# if age >= 18:
#     print("you are now an adult and you can vote now")
# elif age <0:
#     print("You haven't been born yet")

# elif age==0:
#     print("Your age is zero and you are a baby")
# elif age>=100:
#     print("You are very old to give your vote")
# else:
#     print("You must be 18+ to sign na and give your vote")
# *hello world

# !Python calculator
# operator = input("Enter the operator (+,-,*,/):")
# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the second number:"))

# if operator =="+":
#     result = num1 + num2
#     print("The result is :",result)
# elif operator =="-":
#     result = num1 - num2
#     print("The result is :",result)
# elif operator =="*":
#     result = num1 * num2
#     print("The result is :",result)
# elif operator =="/":
#     result = num1 / num2
#     print("The result is :",result)
# else: 
#     print(f"{operator} is not valid operator")


# ! kg to pound convettor 
# weight = float(input("Enter your weight:"))
# unit = input("kilogram or pounds?(kg/lb):")

# if unit =="kg":
#     weight = weight * 2.205;
#     print(f"Your weight in pound is {weight} lb")
#     unit = "lb"
# elif unit == "lb":
#     weight = weight / 2.205;
#     print (f"Your weight in kilogram is {weight} kg")
#     unit = "kg"
# else :
#     print(f"{unit} is not a valid unit") 

# print(f"Your new weight is {round(weight)} {unit}")


# ? kg to pound convertor
# !weight to pound or pound to weight convertor
# * kg to pound convertor calculator
# weight = float(input("Enter your weight:"))
# unit = input("Kilogram or pound?(kg/lb):")

# if unit=="kg":
#     weight = weight * 2.205;
#     print(f"Your weight in pound is {weight} lb")
#     unit ="lb"

# elif unit=="lb":
#     weight = weight /2.205;
#     print(f"Your weight in kilogram is {weight} kg")
#     unit = "kg"

# else:
#     print(f"{unit} is not a valid unit")

# print(f"your new weight is {round(weight)} {unit}")

# list1 = ["apple","banana","Mango"]
# list2 = [1,2,3,4,5]
# list3 = [True,False,True]
# print(type(list1))
# print(type(list2))
# print(type(list3))

# thislist = list(("apple","Banana","cherry"))
# print(thislist)
# thislist2 = list(("apple","Banana","Mango"))
# mainitems =(thislist2)
# print(mainitems[1])

# thislist3 = ["apple","banana","cherry","orange","kiwi","WaterMelon","mango"]
# print(thislist3)
# print(thislist3[2:5])
# print(thislist3[:4])
# print(thislist3[2:])

# print(thislist3[-4:-1])
# if "apple" in thislist3:
#     print("Yes apple is present in the list")

# thislist =["apple","banana","Cherry","Orange","kiwi","mango"]
# print(thislist)
# thislist[1:3]=["blackcurrant","watermelon"]
# print(thislist)


# thislist =["apple","banana","Cherry"]
# print(thislist)
# thislist.insert(2,"watermelon")
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.append("orange")
# print(thislist)
# thislist = ["apple","banana","cherry"]
# thislist.insert(1,"orange")
# print(thislist)

# tropical = ["mango","pineapple","papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thistuple =("kiwi","orange","evan")
# thislist.extend(thistuple)
# print(thislist)
# thislist.append(thistuple)
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.pop(1)
# print(thislist)
# del thislist[0]
# print(thislist)
# del thislist

# thislist = ["apple","banana","cherry"]
# thislist.clear()
# print(thislist)
# for x in thislist:
#     print(x)
# for x in range(len(thislist)):
#     print(x)
#     print(thislist[x])


# thislist =["apple","banana","cherry"]
# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i=i+1

# a = float(input())
# if a<=400.00:
#     a1 =a+a*0.15
#     b1=a1-a
#     print(f"Novo salario: {a1:.2f}")
#     print(f"Reajuste ganho: {b1:.2f}")
#     print(f"Em percentual: {(b1/a)*100:.0f} %")
# elif a>=400.01 and a<=800:
#     a2=a+a*0.12
#     b2=a2-a
#     print(f"Novo salario: {a2:.2f}")
#     print(f"Reajuste ganho: {b2:.2f}")
#     print(f"Em percentual: {(b2/a)*100:.0f} %")
# elif a>=800.01 and a<=1200:
#     a3=a+a*0.10
#     b3=a3-a
#     print(f"Novo salario: {a3:.2f}")
#     print(f"Reajuste ganho: {b3:.2f}")
#     print(f"Em percentual: {(b3/a)*100:.0f} %")
# elif a>=1200.01 and a<=2000:
#     a4=a+a*0.07
#     b4=a4-a
#     print(f"Novo salario: {a4:.2f}")
#     print(f"Reajuste ganho: {b4:.2f}")
#     print(f"Em percentual: {(b4/a)*100:.0f} %")
# else:
#     a5=a+a*0.04
#     b5=a5-a
#     print(f"Novo salario: {a5:.2f}")
#     print(f"Reajuste ganho: {b5:.2f}")
#     print(f"Em percentual: {(b5/a)*100:.0f} %")

# fruits = ["apple","Banana","cherry","kiwi","mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)

# fruits = ["apple","banana","cherry","kiwi","mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)
# newlist = [x.upper() for x in fruits]
# newlist.upper(fruits)
# print(newlist)

# thislist = ["orange","mango","kiwi","pineapple","banana"]
# thislist.sort()
# print(thislist)

# def myfunc(n):
#     return abs(n-50)
# thislist =[100,50,65,82,23]
# thislist.sort(key=myfunc)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)






















