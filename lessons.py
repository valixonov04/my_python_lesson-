# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:00:51 2024

@author: user
"""

#Dictionary
#1
'''
ism = {'Ayubhan':'AI','Shavkatjon':'backand'}
print(ism["Ayubhan"])
'''
'''
#2
talaba = {'ism':'Ilyosbek','familya':'Valixonov','kurs':4, 'yosh':20}
print(f"Talaba {talaba['ism']}  {talaba['familya']} .Uning yoshi {talaba['yosh']} da va {talaba['kurs']} da o'qiydi")
'''
'''
#3 
#del comandasi orqali biz dictionors dagi qiymatlarni o'chirisimiz mummkin . 
#masala  del talabalar['ism']
talabalar = {}
talabalar['ism'] = 'Ali'
talabalar['yosh'] = 20
talabalar['qayerdan'] = 'farg\'ona'
print(talabalar)
'''
'''
#4
#.get() METODI
#bu metod orqali agafrda lug'ata mavjud bo'lmagan key words bersak uning o'rniga boshqa umumiy narsa taklif etishi mumkin .
#car_0 = {'model':'ferrari','rang':'qizil'}
#print(car_0['samolyot'])

#buning o'rniga biz .get() metodidan foydalanamiz 

car_0 = {'model':'ferrari','rang':'qizil'}
moshina = car_0.get('samalyot',"bundey qiymat mavjudnnas")
print(moshina)                    
'''
'''
#5

#Ammalyot 
#number 1
otam = {'ism':'Dilshodbek','familya':'Qoxxorov', 'yil': 1967}
print(f"Mening otam {otam['familya']}  {otam['ism']} . {otam['yil']}-da tug'ilgan")

#number 2
mean = {'dadam':'osh', 'onam': 'shorva' , 'akam' : 'shashlik', 'kenayam':'mastava', 'ozim':'osh'}
print(f"Dadamning eng sevimli taomi {mean['dadam']}")
print(f"onamning eng sevimli taomi {mean['onam']}")
print(f"akamning eng sevimli taomi {mean['akam']}")
'''
'''
#number 3 
#Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. 
#Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

python_izoh = {'float': 'onli sonlar',
               'print':'chop etish',
               'int': 'butun sonlar',
               'for': 'uchun',
               'in': 'ichida'}

soz = input('iltimos kerakli sozni kiriting !').lower()

tarjima = python_izoh.get(soz)
if tarjima==None:
    print('bunday so\'z mavjud emas ! ')
else:
    print(f'{soz} ning manosi {tarjima} ')          
'''
'''
#Lug'at elementlari bilan ishlash 

#.items()- bu funksiya orqali biz lug'atdagi barcha key-value larni chiqarib beradi . 
talaba = {'ism':'anvar',
          'yosh':'20',
          'fakultet':'4',
          'kafedira':'EA'}
#print(talaba.items())
for key, value in talaba.items():
    print(f"Kalit: {key}")
    print(f"Qiymat: {value}")
'''
'''
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }   
    for k,q in telefonlar.items():
    print(f'{k.title()}ning telefoni {q}')
'''
#.key()- Agarda bizga lug'atdagi faqatgina key kerak bolsa bu metoddan foydalanishimiz
# mumkin.
'''
mahsulotlar = { #Do'kondagi mahsulotlar 
                'olma':2000,
                'anjir':3000,
                'o\'rik':4000,
                'shaftoli':5000}
#print(mahsulotlar.keys()) 
bozorlik = ['anor','uzum','non','olma','baliq']  
for mahsulot in mahsulotlar:
   if mahsulot in bozorlik:
       print(f'{mahsulot.title()}ning narxi: {mahsulotlar[mahsulot]} so\'m')

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f'Dokonizda {buyum} yo\'q ekan')
'''
'''
mahsulotlar = { #Do'kondagi mahsulotlar 
                'olma':2000,
                'anjir':3000,
                'o\'rik':4000,
                'shaftoli':5000}
print("Do'kondagi mahsulotlar :")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

'''
'''
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'shavkat':'iphone x',
    'olimjon':'mi 10 pro',
    }   
#print(telefonlar.values())
for telfon in set(telefonlar.values()):
    print(telfon.title())
'''
'''

#Amolyot
lugat = {#python izohli lug'ati
         'and':'va',
         'or':'yoki',
         'items':'kalit va qiymatlar barchasi chiqaradi ',
         'sorted':'A-Z gacha qilib tartiblash ',
         'values': 'fataq qiymatlar',
         'set':'gruhlsb beradi',
         'print':'consolga chiqatib beradi ',
         'for': 'uchun',
         'in':'ichida'}         
for english, uzbek in lugat.items():
    print(f'English: {english}')
    print(f'Uzbek: {uzbek}')
   
'''
'''
lugat = {
    'USA':'Vashinton',
    'Russin':'Maskov',
    'Ukrain':'Kiv',
    'Uzbekiston':'Toshkent',
    'Krgistan':'Bishkek',
    'Tajikistan':'Dushanbe'}
for davlat in sorted(lugat.keys()):
   print(f'Davlatlar: {davlat}')
for poytaht in sorted(lugat.values()):
    print(f'Poytahtlar: {poytaht}')
'''  
''' 
davlat = input('Biron davlatni kiriting !')
lugat = {
      'USA':'Vashinton',
      'Russin':'Maskov',
      'Ukrain':'Kiv',
      'Uzbekiston':'Toshkent',
      'Krgistan':'Bishkek',
      'Tajikistan':'Dushanbe'}
for poytaht in lugat.values():
    if davlat in poytaht:
        print("{davlat}ning poytahti {poytaht}")
'''  
'''
davlat = input('Biron davlatni kiriting! ')
lugat = {
      'USA': 'Washington',
      'Russia': 'Moscow',
      'Ukraine': 'Kyiv',
      'Uzbekistan': 'Tashkent',
      'Kyrgyzstan': 'Bishkek',
      'Tajikistan': 'Dushanbe'}

if davlat in lugat:
    poytaht = lugat[davlat]
    print(f"{davlat}ning poytahti {poytaht}")
else:
    print("Kiritilgan davlat ma'lumotlar bazasida mavjud emas.")

'''
menu = {#restaran menyusi
        'osh':2000,
        'shorva':3000,
        'kabab':4000,
        'somsa':5000,
        'dimlama':6000,
        'moshhorda':7000,
        'lagmon':8000,
        'monti':9000,
        'buhoro osh':10000,
        'makaron':400000}
print('Buurtma berishiz mumkin ')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f'{n+1} - taom: ').lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
       print(f"Sizning buyurtmangiz: {buyurtma} {menu[buyurtma]} som")
    else:
       print(f"kechiras {buyurtma} taom bizda mavjud emas ")
    




















