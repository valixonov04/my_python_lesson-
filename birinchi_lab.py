#1 1. To`g`ri to`rtburchak peremetr va yuzini hisoblash uchun metodlarga ega classini yarating va 
# undan foydalanib 5 ta To`g`rito`rtburcha peremetri ya yuzini aniqlang.

class Peremetr_Yuza():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def peremetr(self):
        per =2*(self.a+self.b)
        return per 
    def yuza(self):
        yuz =self.a*self.b
        return yuz

birinchi =Peremetr_Yuza(10,4)
print(birinchi.peremetr)




#2 Uchburchak peremetr va yuzini hisoblash uchun metodlarga ega 
# classini yarating va undan foydalanib 5 ta uchburcha peremetri ya yuzini aniqlang
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
# 5 ta uchburchak uchun ma'lumotlar
triangles = [
    Triangle(3, 4, 5),
    Triangle(5, 12, 13),
    Triangle(7, 24, 25),
    Triangle(6, 8, 10),
    Triangle(9, 12, 15)]
# Har bir uchburchak uchun perimetr va yuzani hisoblash
for i, triangle in enumerate(triangles, 1):
    print(f"Uchburchak {i}: Perimetri = {triangle.perimeter()}, Yuzasi = {triangle.area():.2f}")





#3 Avtomabil(model, marka, ishlab chiqarilgan yil, bosib o`tgan masofa, texnik ko`rik sanasi) class yating
#  unda bosib o`tilgan masofaga masofa qo`shish, texnik ko`rikni yangilash metodlari yarating. 
# Ushbu klasdan foydalanib 3 ta mashina yarating va masofa, texnik ko`rik ma’lumotlarini yangilang.
class Avtomabil:
    def __init__(self, model, marka, yil, masofa, texnik_korik_sana):
        self.model = model
        self.marka = marka
        self.yil = yil
        self.masofa = masofa
        self.texnik_korik_sana = texnik_korik_sana
    
    def masofa_qoshish(self, km):
        self.masofa += km
        print(f"{self.model} uchun yangi masofa: {self.masofa} km")
    
    def texnik_korik_yangilash(self, yangi_sana):
        self.texnik_korik_sana = yangi_sana
        print(f"{self.model} uchun yangi texnik ko‘rik sanasi: {self.texnik_korik_sana}")

# 3 ta mashina yaratamiz
mashina1 = Avtomabil("Nexia", "Chevrolet", 2015, 120000, "2023-06-15")
mashina2 = Avtomabil("Malibu", "Chevrolet", 2018, 90000, "2023-04-10")
mashina3 = Avtomabil("Spark", "Chevrolet", 2020, 45000, "2023-01-20")

# Mashinalarning masofa va texnik ko‘rik sanasini yangilash
mashina1.masofa_qoshish(500)
mashina1.texnik_korik_yangilash("2024-06-15")

mashina2.masofa_qoshish(1200)
mashina2.texnik_korik_yangilash("2024-04-10")

mashina3.masofa_qoshish(800)
mashina3.texnik_korik_yangilash("2024-01-20")





#4  Shahar(nomi, maydon, aholi, aholi soni o`sishi metodi) class yarating va undan foydalanib 5 ta shahar yarating.
class Shahar:
    def __init__(self, nomi, maydon, aholi):
        self.nomi = nomi
        self.maydon = maydon  # kvadrat kilometrda
        self.aholi = aholi
    def aholi_oshirish(self, son):
        self.aholi += son
        print(f"{self.nomi} shahrining yangi aholisi: {self.aholi}")
# 5 ta shahar yaratamiz
shahar1 = Shahar("Toshkent", 334.8, 2700000)
shahar2 = Shahar("Samarqand", 120.0, 530000)
shahar3 = Shahar("Buxoro", 41.0, 280000)
shahar4 = Shahar("Andijon", 74.3, 420000)
shahar5 = Shahar("Navoiy", 47.0, 150000)
# Har bir shahar uchun aholi sonini oshirish
shahar1.aholi_oshirish(50000)
shahar2.aholi_oshirish(20000)
shahar3.aholi_oshirish(15000)
shahar4.aholi_oshirish(30000)
shahar5.aholi_oshirish(10000)




#5 Guruh(nomi, talabalar sonini qaytarish metodi, talabalar ro`yxati(list)) 
# class yarating va undan foydalanib 2 ta 4-5 nafat talabali guruh yarating.

class Guruh:
    def __init__(self, nomi, talabalar):
        self.nomi = nomi
        self.talabalar = talabalar  # talabalar ro‘yxati (list)
    
    def talabalar_soni(self):
        return len(self.talabalar)

# 2 ta guruh yaratamiz
guruh1 = Guruh("AI-101", ["Ali", "Vali", "Sanjar", "Shoxrux", "Nodir"])
guruh2 = Guruh("DS-102", ["Murod", "Sarvar", "Jasur", "Anvar"])
# Har bir guruh uchun talabalar sonini chiqaramiz
print(f"{guruh1.nomi} guruhidagi talabalar soni: {guruh1.talabalar_soni()}")
print(f"{guruh2.nomi} guruhidagi talabalar soni: {guruh2.talabalar_soni()}")





#6   Hayvonlar(nomi, turi, oyoqlar soni, ozuqasi) clasini yarating va 5 ta hayvon yarating
class Hayvonlar:
    def __init__(self, nomi, turi, oyoqlar_soni, ozuqasi):
        self.nomi = nomi
        self.turi = turi
        self.oyoqlar_soni = oyoqlar_soni
        self.ozuqasi = ozuqasi

# 5 ta hayvon yaratamiz
hayvon1 = Hayvonlar("Sher", "Yirtqich", 4, "Go'sht")
hayvon2 = Hayvonlar("Fil", "O'txo'r", 4, "O't")
hayvon3 = Hayvonlar("Qush", "Parrandalar", 2, "Don")
hayvon4 = Hayvonlar("Ilon", "Suddalanuvchi", 0, "Go'sht")
hayvon5 = Hayvonlar("Ot", "Uy hayvoni", 4, "O't")

# Har bir hayvon haqida ma'lumotni chiqaramiz
for i, hayvon in enumerate([hayvon1, hayvon2, hayvon3, hayvon4, hayvon5], 1):
    print(f"Hayvon {i}: Nomi - {hayvon.nomi}, Turi - {hayvon.turi}, Oyoqlar soni - {hayvon.oyoqlar_soni}, Ozuqasi - {hayvon.ozuqasi}")




#7 Xonadon nomli class yarating va undan foydalanib ko`p qavatli turar
#  joy hisobi(ma’lumot beruvchi, komunal to`lovlar 1 yoki 2 ta )ni yuritish dasturini tuzing

class Xonadon:
    def __init__(self, nomi, qavat, komunal_tolovlar):
        self.nomi = nomi  # xonadon nomi yoki egasining nomi
        self.qavat = qavat  # qavat raqami
        self.komunal_tolovlar = komunal_tolovlar  # komunal to'lovlar ro'yxati

    def komunal_tolov_hisobi(self):
        umumiy_tolov = sum(self.komunal_tolovlar)
        return umumiy_tolov

    def malumot_berish(self):
        print(f"Xonadon: {self.nomi}")
        print(f"Qavat: {self.qavat}")
        print(f"Komunal to'lovlar: {self.komunal_tolovlar}")
        print(f"Umumiy komunal to'lov: {self.komunal_tolov_hisobi()} so'm")

# Bir nechta xonadon yaratamiz
xonadon1 = Xonadon("Ibrohimovlar", 2, [50000, 30000])  # 1-to'lov: elektr, 2-to'lov: suv
xonadon2 = Xonadon("Karimovlar", 4, [40000])  # faqat elektr to'lovi
xonadon3 = Xonadon("Niyozovlar", 3, [60000, 20000])  # elektr va suv to'lovlari

# Xonadonlar uchun ma'lumotlarni chiqarish
for xonadon in [xonadon1, xonadon2, xonadon3]:
    xonadon.malumot_berish()
    print("--------------------")



#8   . Fan va talaba klaslarini yarating va ular yordamida baholar
#  vedmosti va talaba reyting daftarchasi dasturlarini yarating

class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.baholar = []

    def baho_qoshish(self, baho):
        self.baholar.append(baho)

    def ortacha_baho(self):
        if self.baholar:
            return sum(self.baholar) / len(self.baholar)
        else:
            return 0

class Talaba:
    def __init__(self, ism, id):
        self.ism = ism
        self.id = id
        self.fanlar = {}

    def fan_qoshish(self, fan):
        self.fanlar[fan.nomi] = fan

    def reyting_daftarchasi(self):
        print(f"Talaba: {self.ism} (ID: {self.id})")
        for fan_nomi, fan in self.fanlar.items():
            ortacha = fan.ortacha_baho()
            print(f"{fan_nomi} fani: Baholar {fan.baholar} | O‘rtacha baho: {ortacha:.2f}")
        print(f"Umumiy reyting: {self.umumiy_reyting():.2f}")

    def umumiy_reyting(self):
        umumiy_baholar = [fan.ortacha_baho() for fan in self.fanlar.values()]
        if umumiy_baholar:
            return sum(umumiy_baholar) / len(umumiy_baholar)
        else:
            return 0

# Fanlarni yaratish
fan1 = Fan("Matematika")
fan2 = Fan("Fizika")
fan3 = Fan("Ingliz tili")

# Baholar qo‘shish
fan1.baho_qoshish(85)
fan1.baho_qoshish(90)
fan2.baho_qoshish(78)
fan2.baho_qoshish(82)
fan3.baho_qoshish(88)
fan3.baho_qoshish(92)

# Talaba yaratish va fanlarni qo‘shish
talaba = Talaba("Ali", 12345)
talaba.fan_qoshish(fan1)
talaba.fan_qoshish(fan2)
talaba.fan_qoshish(fan3)

# Talabaning reyting daftarchasini chiqarish
talaba.reyting_daftarchasi()
 






