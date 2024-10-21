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