# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:33:11 2024

@author: user
"""

#Funksiya - bir necha qator kodlarning yig'ilmasi . 
#def - funksiyani e'lon qilish uchun command 


#bu funksiya orqali oz yoshingizni bilib olishiz mumkin !
# def yosh_hisobla(tugilgan_yil):
#     """Bu funksiya sizning yoshingizni hisoblab beradi, 
#     buning uchun tug'ilgan yilingizni kiriting"""
#     yosh = 2024 - tugilgan_yil
#     print(f"Sizning yoshingiz {yosh} yoshda.")
#salom beruvchi funksiya 
# def salom_beruvchi():
#     """bu funksiya salom beruvchi funksiya """
#     print("Assalomu alaykum !")
 

   
# #bu funksiya endi qiymat ham qabul qladi 
# def salom_ber(ism):
#     """bu funksiya ismingiz orqal salom beradi !"""
#     print(f"Assalomu alaykum {ism.title()}")
# salom_ber("Ali") 



# #Docstringni konsolga chiqarish uchun print(funksiya_nomi.__doc__) deb ham yozishimiz mumkin:
# #    print(type.__doc__) #<--- bu codan biz faqat consol oynasida foydalana olamiz
   



# # bazi funksiyalarda birnechta argumenlar(parametirlar) tallab etilishi mumkin !  
    
# #Ism va familyani jambal beruvchi funksiya 
# def ism_familya(ism,familya):
#     """ Bu funksiya ism va familyani jamlab beradi """
#     print(f"Sizning ismingiz: {ism.title()} \n " ,
#           f"Sizning familyangiz : {familya.title()} ")        
    
# ism_familya("ali", "Muhtorov")



#Ammalyot
# def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = input("Tug'ilgan yilingizni kiriting: ")
# yosh = int(tyil)
# yosh_hisobla(yosh)    



# #Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def kvadrat_kub(son):
#     """Bu funksiya orqali siz sonlarni kubi hamda kvadratini bilishiz mumkin """
#     son = int(son) #buyerda faqatgina son qabul qiladi
#     print(f"{son} ning kvadrati  {son**2} ga teng \n"
#           f"{son} ning kubi {son**3} ga teng ")
# # son = input("Son kiriting --> \n ")
# # kvadrat_kub(son)
# #kvadrat_kub(5)

# #Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def juft_toq (son):
#     """Soni juft yoki toq ekanligini aniqlovchi funksiya """
#     if son%2 != 0:
#         valu = f"{son} soni toq son "
#     else:
#         valu = f"{son} soni juft son "
#     print(f"Siz kiritgan {valu} ")

# #Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
# #Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

# def taqoslash (x,y):
#     """Bu funksiya sonlarni eng kata qiymatini consolga chiqaradi """
#     if x > y:
#        print(f"{x} kata  {y} dan ")
#     elif x < y :
#         print(f" {x} kichkina  {y} dan ")
#     else:
#         print(f"{x} va {y}  ikkisi teng ")
# taqoslash(6,6)

# #Foydalanuvchidan x va y sonlarini olib, yig'indini konsolga chiqaruvchi funksiya yozing.
# def yigindi_hisoblash(x,y):
#     """Bu funksiya orqali siz yigindini aniqlashiz mumkin """
#     yigindi = x+y 
#     print(f"Bu ikki soni qoshganda {yigindi} qiymatga teng ")

# yigindi_hisoblash(5, 9)


# #Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz
# #bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
# def soni_tekshirish(x):
#     """bu funksiya sonlarni 2 dan 10 gacha bolgan  sonlarnga bo'linishini tekshiradi """
#     for sonlar in range(2,11):
#         if sonlar%2 :
#             print(f"{x} ni {sonlar} ga bolsek qoldiq {x%sonlar} ga teng ")
#         else:
#             print(f"{x} ni {sonlar} ga bo'lganda qoldiq qolmaydi ")

# soni_tekshirish(203456578764)


#Lesson 2
#Yuqoridagi funksiyamizga ahamiyat bersangiz, uning badanida endi print() funksiyasi yo'q. 
#Buning o'rniga, funksiyamiz return operatori yordamida toliq_ism degan o'zgaruvchining 
#qiymatini qaytaradi.
# def toliq_ism_yasa(ism, familiya):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz
# student = toliq_ism_yasa("Ali","Qaxxorov")
# print(student)




# #range() dan farqli ravishda, funksiyamiz 2 son oralig'idagi sonlarni ro'yxat ko'rinishida 
# #qaytarsin.
# def oraliq(min, max, qadam=1):
#     sonlar = []  # bo'sh ro'yxat
#     while min < max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar
# # Misollar:
# print(oraliq(0, 40))       # Default qadam = 1
# print(oraliq(0, 40, 2))    # Qadam = 2
# print(oraliq(10, 50, 5))   # Qadam = 5
   
    


# #Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va 
# #telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. 
# #Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy 
# #qiling (masalan, tel.raqam, el.manzil)
# def info_user(name, lastname, born_year, address, email="" , tell_number="" ):
#     """ Bu userni malumotlarini royhat ko'rinishida qilib beradi """
#     lugat = {"name":name,
#              "lastname":lastname,
#              "born_year":born_year,
#              "address":address,
#              "email":email,
#              "tell_number":tell_number}
#     return lugat
# # information = info_user("Ali", "Valixonov", 2004, "Andijon viloyati", tell_number="+998882324077")
# # print(information)    
# #Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan 
# #ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
# users =[]
# while True:
#     name = input("What is your name ? \n ")
#     lastname = input("What is your last name ? \n")
#     born = input("how old are you ? \n ")
#     address =input("where are you from ? \n ")
#     email = input("what is your email ? \n ")
#     tell_number = input("what is your tell number ? \n ")
    
#     users.append(info_user(name, lastname, born, address,email,tell_number))
    
#     sorov = input("Yana malumot kiritasmi ?  yes/no \n")
#     if sorov == "no":
#         break

# print("Users: ")
# for user in users:
#     print(f"Name: {user['name'].title()} \n ",
#           f"LastName : {user['lastname'].title()} \n ",
#           f"Old : {user['born_year']} \n ",
#           f"Address :{user['address'].title()} \n ",
#           f"Email: {user['email']} \n ",
#           f"Tell: {user['tell_number']} \n ")
    
  
    
  
#Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

def max_value(x,y,z):
    """Uchta qiymatdan eng katasini chiqarib beruvchi funksiya """
    max = x 
    if y>= max:
        max =y
    if z>= max:
        max = z
    return max

print(max_value(50, 60, 80) ) 

#Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, 
#perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
#perimetir formula -> 2pR
#diyametir -> 2*R
#yuza -> pr**2


    
        





#Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar 
#ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning 
#yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish 
#had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...




#Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini 
#katta harfga o'zgatiruvchi funksiya yozing.

def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()   

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)






