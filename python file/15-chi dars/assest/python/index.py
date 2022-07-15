#.items() Metodi
#bu metod yordamida lug'at ichidagi barcha kalit va qiymatlarni ko'rsatadi. 
talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

print(talaba_0.items())
#Natija: dict_items([('ism', 'alijon'), ('familiya', 'shamshiyev'), ('yosh', 22), ('fakultet', 'matematika'), ('kurs', 4)])

for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")
#Natija: 
# Kalit: ism
# Qiymat: alijon kabi hamma kalit va qiymatlar shu ko'rinishda chiqadi

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")
#Natija: Alining telefoni iphone x  
#tepadagi kabi hamma kalit va qiymatlar shu ko'rinishda chiqadi


#.keys() Metodi
#.keys() ro'yhatdagi faqatgina kalit so'zlarni chiqarib beradi
mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(mahsulotlar.keys())
#Natija: dict_keys(['olma', 'anor', 'uzum', 'anjir', 'shaftoli'])

print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())
#Natija: 
#Do'kondagi mahsulotlar:
#Olma 
#Anor 
#kabi hamma ro'yhatdagi narsalrni shu kabi chiqarib beradi

bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#Natija: Anor 20000 so'm 
#Uzum 40000 so'm 
#bozorlik digan royhatdagi narsala mahsulotlar ichida bo'lsa uning narx bilan chiqaradi

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")
#bozorlik digan ro'yhatdagi narsala mahsulotlar ichida bolmasa Iltimos, do'koningizga non ham olib keling kabi so'z chiqadi


#.values() Metodi
#.values() Metodi lug'atdagi hamma kalitni ichidagi qiymatni chiqaradi
print(telefonlar.values())
#Natija: dict_values(['iphone x', 'galaxy s9', 'mi 10 pro', 'nokia 3310']

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
#Natija:
#Foydalanuvchilar quyidagi telefonlarni ishlatishadi:
#ipone x kabi hamma kalitni ichidagi qiymatni chiqaradi


telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):#set() funktsiyasi ro'yhatda 1ta gap 2 yoki 3 marta kelsa faqt bittasi olib qolib qolganin ko'rsatmidi
    print(tel)
#Foydalanuvchilar quyidagi telefonlarni ishlatishadi:
#ipone x kabi hamma kalitni ichidagi qiymatni chiqaradi
