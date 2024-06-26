# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:29:49 2024

@author: user
"""

#while and input

# yigindi = 0
# while True:
#     son = int(input("Son kiriting (0 to'xtatish uchun): "))
#     if son == 0:
#         break
#     yigindi += son
# print("Yig'indi:", yigindi)

# salom = input('Ismiz nima ? ')
# print('salom ',salom)





# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingiz necha metr? ")
# height = float(height) # bo'yni o'nlik songa o'tkazamiz


# name = input("Ismingiz nima ? \n ").title()
# ask  = f" Salom {name} . Yoshingiz nechida ?  "
# old = input(ask)
# old = int(old)
# ask2 = f'{name} Bo\'yingiz necha sm ? '
# heigh = input(ask2)
# heigh = float(heigh)




#Wile - bu tohtamaydigon tsikl toki fols qiymat bolmaguncha 
# son = 1
# while son <= 5:
#     print(son)
#     son+=1
    



# print("Bu dastur sonlarni yig'indisini chiqarib beradi. (qachonki 0 kiritsengiz dastur yig'indini chiqaradi )  ")
# yigindi = 0 
# son = 1 




# while True:
#     son = int(input("Son kiriting ! \n "))
#     if son == 0:
#        break 
#     yigindi+=son  
# print(f"Jami sonlar yig'indisi {yigindi} ga teng")    




#Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi
# stop so'zini yozishi bilan dasturni to'xtating
# savol = 'Sizga qaysi kitob yoqadi ? \n'
# savol+= 'Agar dasturni to\'tatishni hohlasez stop buyrug\'ini yozing '
# kitob = ''
# while kitob != 'stop':
#       kitob = input(savol)
      
# print('Siz STOP buyrug\'ini yubordiz')





#Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
#7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while 
#tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. 
#Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

# savol = "Yoshingiz nechida "
# ishora = True
# while  ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         ishora = False
#     else:    
#         yosh = int(qiymat)
#         if yosh < 7 :
#           price = 2000
#         elif yosh >= 7 and yosh <= 18:
#           price = 3000
#         elif yosh > 18 and yosh < 65:
#           price = 10000
#         else:
#           price=0
#     if price== 0:
#         print('siz uchun chipta bepul')
#     else:
#         print(f'Siz uchun narh {price} so\'m')
# print('siz dasturni tohtatingiz')
    



# savol = "Yoshingiz nechida "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#     if yosh < 7:
#         price = 2000
#     elif yosh >= 7 and yosh <= 18:
#         price = 3000
#     elif yosh > 18 and yosh < 65:
#         price = 10000
#     else:
#         price = 0
#     print(f'Siz uchun narh {price} so\'m')



# savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     try:
#         son = float(qiymat)
#         if son < 0:
#             print("Iltimos, musbat son kiriting.")
#             continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#         else:
#             ildiz = son ** 0.5
#             print(f"{son} ning ildizi {ildiz} ga teng")
#     except ValueError:
#         print("Iltimos, son kiriting.")
























     
                
                