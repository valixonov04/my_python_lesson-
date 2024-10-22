# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:03:20 2024
@author: Valixonov Ilyosbek 
"""
#1. #UZ Shaxsiy ma'lumotlar tizimi: Foydalanuvchidan ismi, yoshi, manzili va telefon raqamini kiriting. Agar foydalanuvchi 18 yoshdan kichik bo'lsa, 
# #unga bu tizimdan foydalanish  cheklanganligi haqida xabar bering. Agar foydalanuvchi kiritgan ma'lumotlar to'liq bo'lmasa (biror narsa kiritilmasa), 
#foydalanuvchiga "Ma'lumot to'liq emas!" xabarini qaytaring. To'liq va mos keladigan ma'lumotlar kiritilganda, ularni dictionaryda saqlang va foydalanuvchi uchun profil yarating.

#1. #ENG Personal Information System: Ask the user to enter their name, age, address and phone number. If the user is under 18 years of age,
#inform him that the use of this system is restricted. If the information entered by the user is incomplete (something is not entered),
#to the user "The data is incomplete!" return the message. When complete and matching information is entered, store it in a dictionary and create a profile for the user.

print("Please add yourself all information ")
check = input("Are you at least 18 years old? Please Check Yes/Not/n >>  ")
if check.upper() == "YES":
    print("You are in the system 😊")
    name=input("What is your name ? ")
    age = input("how old are you ? ")
    location = input("Wher are you live ? ")
    phon_namer = input("You are phon namer ?")
    information = {}
    if all([name,age,location,phon_namer]):
       information["name"] = name
       information["age"] = age
       information["location"] = location
       information["phon_namer"] = phon_namer
    else:
        print("your infarmation do not full ! 😒 ")  
else :
    print("Sory You are litte ! bro ")

#2. #UZ Tartiblangan ism va yoshlar ro'yxati: Foydalanuvchidan 5 ta odamning ismi va yoshi kiritilishini so'rang. Bu ma'lumotlarni dictionaryda saqlang va yoshi bo'yicha tartiblangan holda chop eting
    
    #ENG Sorted list of names and ages: Ask the user to enter the names and ages of 5 people. Store these data in a dictionary and print them sorted by age

information = {}
print("Hi , Enter information about 5 of your friends !  ")
for i in range(5):
    name=input(f"{i+1} - Person , What is your name ? ")
    age =int(input(f"{i+1} - Person , How old are your ? "))
    information[name]=age
sorted_ages = sorted(information.values())  
print(information)
print(sorted_ages)   


#3. #UZ Fibonacci sonlari: Foydalanuvchidan raqam kiriting va shu raqamgacha bo'lgan Fibonacci ketma-ketligining sonlarini chop eting. Fibonacci sonlarini hisoblashda while tsiklidan foydalaning.
    
    #ENG 1. Fibonacci numbers: Ask the user to enter a number and print the numbers of the Fibonacci sequence up to that number. Use a while loop to calculate Fibonacci numbers.
a,b =0,1
n =int(input("Please  enter number ! "))
i=0
while i<n:
    print(a)
    start =a+b
    a=b
    b=start
    i+=1
#4 #UZ Elektron pochta tasdiqlash: Foydalanuvchidan elektron pochta manzilini so'rang. Agar pochta manzili "@gmail.com", "@yahoo.com", yoki "@outlook.com" bilan tugasa, foydalanuvchi 
# provayderini aniqlang va tegishli xabar chop eting. Agar pochta manzili kiritishda "@" belgisi bo'lmasa yoki noto'g'ri formatda kiritilgan bo'lsa, "Noto'g'ri elektron pochta manzili" degan xabar chiqaring.
 
 #ENG  Email Verification: Ask the user for their email address. If the email address ends with "@gmail.com", "@yahoo.com", or "@outlook.com", identify the user's provider and print the appropriate message. 
 # If the email address is entered without an ``@'' sign or is entered in an incorrect format, issue a message saying 'Invalid email address'.   
email = input(" Please enter your email address ! ")
#check_icon = ["@"]
check_words = ["@gmail.com", "@yahoo.com", "@outlook.com"]
if "@" in email :
    if any( words.lower()  in  email.lower() for  words in check_words):
        print("You are in sistem ! 😊")
    else:
        print("You are not full information ! 😒") 
else:
    print("Not right information !")

#5 #UZ 1.	Mahsulotlar va narxlar: Foydalanuvchidan mahsulotlarning nomi va narxini kiriting, bularni dictionaryda saqlang. Keyin foydalanuvchiga jami narxni hisoblang va chop eting. 
#Agar mahsulot narxi 100 mingdan yuqori bo'lsa, ularga chegirma qo'llang (masalan, 10%).
  
   #ENG 1. Products and prices: Ask the user to enter the name and price of the products, store them in a dictionary. Then calculate and print the total cost to the user. 
# If the price of the product is higher than 100 thousand, apply a discount to them (for example, 10%).

number =int(input("Please enter product number !  "))
product_price = {}
for i in range(number):
    product = input(f" {i+1} - Please enter product name ! ")
    price = int(input(f"{i+1} - Please enter price  !"))
    product_price[product] = price
all_price =[]    
for price_all in product_price.values():
    all_price.append(price_all)
sum_all= sum(all_price) 
if sum_all > 100_000 :
    sale = sum_all-((sum_all/100)*10)
    print(f"Your product {product_price.keys()}")
    print(f"Your purchase {sum_all}. Your sale {(sum_all/100)*10}% . You will pay  to be all {sale}")
else:
    print(f"Your product {product_price.keys()}")
    print(f"Your purchase {sum_all}.")
#6 #UZ  Takrorlanmas raqamlar ro'yxati: Foydalanuvchidan 10 ta raqam kiriting, bu raqamlar orasida takrorlanishlar bo'lishi mumkin. Ushbu raqamlar ichida faqat takrorlanmas
   # raqamlarni toping va alohida chop eting. Buning uchun set va listlardan foydalaning   
   
   #ENG List of non-repeating numbers: Enter 10 numbers from the user, there may be repetitions among these numbers. Find only unique numbers among these numbers and print 
   # them separately. Use sets and lists for this
list1 =[]
set_list ={}
print("You will enter at 10 number in here !")
for i in range(10):
    number = int(input(f"{i+1} - enter your namber ! ")) 
    list1.append(number)
set_list=set(list1)
print(list1) 
print(set_list) 
#7 #UZ Xarajatlar rejasi: Foydalanuvchidan har oyda qilinadigan 5 ta asosiy xarajatni va har birining narxini so'rang. Ushbu ma'lumotlarni list va dictionaryda saqlang.
   #  Xarajatlarning jami narxini hisoblang va agar foydalanuvchi kiritgan jami narx 1 milliondan oshsa, ularga byudjetdan chiqayotganliklarini ko'rsating va byudjetni qayta ko'rib chiqish taklifini bering.
  
   #ENG  List of non-repeating numbers: Enter 10 numbers from the user, there may be repetitions among these numbers. Find only unique numbers among these numbers and print them separately. Use sets and lists for this
information = {}
dictionary_name = []
dictionary_price = []
print("Hi , Enter information about to important  at 5 production ! ") 
for i in range(5):
    name=input(f"{i+1} - Enter praduct  ! ")
    price =int(input(f"{i+1} - Enter product price ! "))
    information[name]=price
    dictionary_name.append(name) 
    dictionary_price.append(price)
information[name]=price
sum_all = sum(dictionary_price)
if sum_all > 1_000_000:
    print("Your cost is large in limit ! ")
    print(sum_all) 
    print(dictionary_name)
    print(dictionary_price)
    print(information)
else:      
    print(sum_all) 
    print(dictionary_name)
    print(dictionary_price)
    print(information)
#8 #UZ Talabalar bahosi: 5 ta talabalar va ularning baholarini kiriting. Har bir talabani bahosiga qarab quyidagi izohlar bilan 
# chop eting:
#         1.	90 dan yuqori – "A'lo baho"
#         2.	80 dan yuqori – "Yaxshi baho"
#         3.	70 dan yuqori – "Qoniqarli"
#         4.	70 dan past – "Yomon baho".  
   #ENG #8 #UZ Student grade: Enter 5 students and their grades. With the following comments depending on the grade of each student
# print:
          # 1. Above 90 – "Excellent"
          # 2. Above 80 – "Good Grade"
          # 3. Above 70 – "Satisfactory"
          # 4. Below 70 – "Bad Grade".
student = {}
for i in range(5):
    name = input(f"Enter at {i+1}  student name ! ")
    grade = int(input(f"{name} grade ! "))
    student[name]=grade
for grades in student.values():
    if grades > 90:
        print("Very good ")  
    elif grades >80 :
        print("well")
    elif grade > 70 :
        print("not bad ")
    else:
        print("bad")
print(student)  

#9 #UZ 1.	Raqamlar filtri: Foydalanuvchidan 10 ta raqam kiriting. Ushbu raqamlar orasidan faqat juft va toq sonlarni alohida chop eting.
   #Agar raqam manfiy bo'lsa, ularni e'tiborsiz qoldiring. Bularni for tsikli yordamida filtrlab ko'rsating.

   #ENG 1. Number filter: Enter 10 numbers from the user. Among these numbers, print only the even and odd numbers separately. 
   #If the number is negative, ignore them. Filter these using a for loop.
for i in range(10): 
    number = int(input("Please enter at 10 number ! "))
    if number%2==0 :
        print(f"{number} is  couple ")
    
    elif number <=0:
         print(f"{number} is negative ! ")

    elif number%2 != 0:
        print(f"{number} is not couple !")

#10 #UZ Takrorlanmalarni aniqlash: Foydalanuvchidan bir nechta so'zlarni kiriting (kamida 10 ta). Ushbu so'zlardan takrorlanganlarini
# toping va faqat takrorlangan so'zlarni chop eting. Buning uchun set va listlardan foydalaning.

    #ENG Duplicate detection: Enter multiple words from the user (at least 10). These words are repeated
#Find  and print only repeated words. Use sets and lists for this
set_list ={}
list1 = []
for i in range(10):
    number = int(input(f"{i+1} - enter number ! "))
    list1.append(number)
set_list=set(list1)
print(set_list)
print(list1)

#11 #UZ Til bilimi: Foydalanuvchidan qaysi dasturlash tillarini bilishini so'rang va ularni dictionaryda saqlang. 
# Foydalanuvchi qaysi tillarni bilishini kiritgandan keyin, agar foydalanuvchi "Python" tilini bilsa, "Siz Python bo'yicha dasturchisiz" deb xabar bering. 
# Agar "JavaScript"ni bilsa, "Veb dasturchi" ekanini ayting. Aks holda, "Siz dasturchi emassiz" degan xabar chop eting.

    #ENG Language Knowledge: Ask the user what programming languages ​​they know and store them in a dictionary.
# After entering what languages ​​the user knows, report "You are a Python programmer" if the user knows "Python".
# Say "Web Developer" if knows "JavaScript". Otherwise, print the message "You are not a developer".

dictionary_name = {}
name = input("What is your name  ? ")
know =input("Which do you know a programming lenguange  ? ")
dictionary_name[name]=know
if know.lower() =="PYTHON".lower():
    print("You are programming in python ! ")
elif know.lower()=="JAVASCRIPT".lower() :
    print("You know Web programming ")  
else:
    print("You do not progam")   
print(dictionary_name)

#12 #uz 	Xaridlar ro'yxati: Mahsulotlar va ularning narxlarini lug'at shaklida kiritib, jami narxni hisoblang. Keyin foydalanuvchiga jami narx bo'yicha chegirma imkoniyatini ko'rsating:
#	  500 mingdan oshsa 5% chegirma.
#	  1 milliondan oshsa 10% chegirma.
#	  Chegirmadan keyin jami narxni chop eting

#ENG Shopping list: Enter the products and their prices in a dictionary and calculate the total price. Then show the user the possibility of a discount on the total price:
#    5% discount if it exceeds 500 thousand.
#    10% discount for more than 1 million.
#    Print total price after discount
information = {}
list1 =[]
print("Hi , Enter information about to important  at 5 production ! ") 
for i in range(5):
    name=input(f"{i+1} - Enter praduct  ! ")
    price =int(input(f"{i+1} - Enter product price ! "))
    information[name]=price
list1=list(information.values())
sum_all = sum(list1)
if sum_all > 5_000_00 :
    print(f"You will pay total suma {(sum_all/100)*5}  becouse You have 5% sale . ")
elif sum_all > 1000000 :
     print(f"You will pay total suma {(sum_all/100)*10}  becouse You have 10% sale . ")
else:
    print(f"You will pay {sum_all}")  


#13 #UZ  Takrorlanuvchi raqamlar: Foydalanuvchidan 10 ta raqam kiriting va ulardan takrorlanganlarini topib, chop eting. 
#Takrorlanmagan raqamlarni alohida ko'rsating. Buning uchun for tsikli va listdan foydalaning.
#ENG  Duplicate numbers: Enter 10 numbers from the user and find the duplicates and print them. Show non-repeated numbers separately. To do this, use a for loop and a list.

unique_nums = []
repeated_nums = []
nums = []
for i in range(10):
    nums.append(int(input("Raqam kiriting: ")))
for num in nums:
    if nums.count(num) > 1 and num not in repeated_nums:
        repeated_nums.append(num)
    elif nums.count(num) == 1:
        unique_nums.append(num)

print("Takrorlanuvchi raqamlar:", repeated_nums)
print("Takrorlanmagan raqamlar:", unique_nums)

#14 #UZ 1.	Fibonacci sonlarining uzunligi: Foydalanuvchidan Fibonacci ketma-ketligidagi nechta sonni ko'rsatish kerakligini so'rang va ushbu sonlarni ro'yxat shaklida chop eting.
#  Ketma-ketlikni yaratishda while tsiklidan foydalaning
    #ENG 1. Fibonacci numbers: Ask the user to enter a number and print the numbers of the Fibonacci sequence up to that number. Use a while loop to calculate Fibonacci numbers.
a,b =0,1
n =int(input("Please  enter number ! "))
i=0
while i<n:
    print(a)
    start =a+b
    a=b
    b=start
    i+=1
#15 #UZ  Juft va toq sonlar ajratish: Foydalanuvchidan 10 ta son kiriting va bu sonlarni juft va toq sonlar ro'yxatiga ajrating. Har bir ro'yxatni alohida chop eting.
    #ENG  Split even and odd numbers: Enter 10 numbers from the user and split these numbers into a list of even and odd numbers. Print each list separately.
even_numbers = []
odd_numbers = []

for i in range(10):
    number = int(input("Raqam kiriting: "))
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Juft raqamlar:", even_numbers)
print("Toq raqamlar:", odd_numbers)
