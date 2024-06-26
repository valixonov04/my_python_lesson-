# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:42:35 2024

@author: user
"""
'''
#Nesting 
#bu lug'atlarni ichida royhatlar yoki aksincha royhatlarni ichida lug'atlarni qolash imkoni beradi

car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }

#car = car1
#print(f"{car['model']}" ,\
#      f"{car['rang']} rang "\
#      f"{car['yil']}$")
      
cars = [car0,car1,car2]
for car in cars:
    print(f"Modelei : {car['model']} "\
          f"  rangi {car['rang']}  "\
          f" narhi {car['narh']} $")

'''
'''
malibus = []
for n in range(10):
     new_car = {#har bita mashina uchun lug'at 
                'model':'malibu',
                'rang':None,
                'narh':None,
                'kilametir':0,
                'karobka':'avfto'}
     malibus.append(new_car)
                             



for malibu in malibus[:3]:
    malibu['rang']='qora'
for malibu in malibus[3:6]:
    malibu['rang']='qizil'   
    
    
for malibu in malibus[:5]:
    malibu['kilometir']= 10 
    
for malibu in malibus:
    if malibu['rang']=='qora':
        malibu['karobka'] = 'avftamat'
        
    
    
    
for malibu in malibus:
    if malibu['karobka'] == 'avfto':
        malibu['narh']=300000
    else:
        malibu['narh'] = 25000
    
    
    
for model,narh,rang,kilametir,karobka in malibus.items():
    print(f"Model: {model}")
    print(f"Rang: {rang}")
    print(f"Narhi: {narh}")
    print(f"Kilametiri: {kilametir}")
    print(f"Karobka: {karobka}")
    
    
    
    
#print(malibus)

'''
'''
malibus = []
for n in range(10):
    new_car = {  # har bir mashina uchun lug'at
        'model': 'malibu',
        'rang': None,
        'narh': None,
        'kilometir': 0,
        'karobka': 'avto'
    }
    malibus.append(new_car)

for malibu in malibus[:3]:
    malibu['rang'] = 'qora'
for malibu in malibus[3:6]:
    malibu['rang'] = 'qizil'

for malibu in malibus[:5]:
    malibu['kilometir'] = 10

for malibu in malibus:
    if malibu['rang'] == 'qora':
        malibu['karobka'] = 'avtomat'
    else:
        malibu['karobka'] = 'mehanika'
    

for malibu in malibus:
    if malibu['karobka'] == 'avtomat':
        malibu['narh'] = 30000
    else:
        malibu['narh'] = 25000

for malibu in malibus:
    print(f"Model: {malibu['model']}")
    print(f"Rang: {malibu['rang']}")
    print(f"Narhi: {malibu['narh']}")
    print(f"Kilometiri: {malibu['kilometir']}")
    print(f"Karobka: {malibu['karobka']}")
    print("\n")

#print(malibus)

'''
'''
dasturchilar = {
                'ali':['java','python','django'],
                'shox':['html','css','boots'],
                'ayubhan':['ai','c++','c#'],
                'hasan':['javascrib','python',]}
for ism,tili in dasturchilar.items():
     print(f'\n {ism} quydagi dasturlash tiliarini biladi :')
     for till in tili:
            print(till.upper(), end='')
'''

'''

adabiyot = {
    'ism':'Alisher Navoiy',
    'tugilgan_yili': 1441,
    'asarlari': ['hamsa','chor devon'],
    'vafoti yili': 1501
    }
matemati = {
    'ism': 'Alin Tuning',
    'tugilgan_yili':1880,
    'asarlari':"tuning testi",
    'vafoti yili':1969
    }
 
shaxslar = [adabiyot,matemati]
for shaxs in shaxslar:
    print(f"ism: {shaxs['ism']}")
    print(f"Tug'ilgan yili': {shaxs['tugilgan_yili']}")
    print(f"Asarlari : {shaxs['asarlari']}")
    print(f"Vafoti: {shaxs['vafoti yili']}")
    
'''
'''
kinolar = {
    'ali':['Sherli homis','shovshindan qochis','karib dengiz qaroqchiar'],
    'vali': ['interselerlar','kapitan amerika '],
    'shox': ['qasoskorlar','temir odam','terminator'],
    'husan': ['betmen','archi','shavq']
    }
for ism,kino in kinolar.items() :
        print(f'\n{ism} ga yoqadigon kinolar:')
        for kino1 in kino :
            print(kino1.title())
'''          
davlatlar = {
    'uzbekistan': {
        'poytahti': 'toshkent',
        'yermaydoni': 448900,
        'aholisi':3600240000,
        },
    'russin': {
        'poytahti': 'maskov',
        'yermaydoni': 10000448900,
        'aholisi':36000000,
        },
    'kazaqistan': {
        'poytahti': 'toshkent',
        'yermaydoni': 12131448900,
        'aholisi':700000000,
        },
    'china': {
        'poytahti': 'toshkent',
        'yermaydoni': 448.900,
        'aholisi':3433443000000,
        }
    }          
    
for davlat,info in davlatlar.items():
    print(f"\n {davlat} ning poytahti {info['poytahti']}  "\
          f"yer maydoni {info['yermaydoni']} ga teng "\
          f"aholi soni {info['aholisi']}"
          )
        
             








