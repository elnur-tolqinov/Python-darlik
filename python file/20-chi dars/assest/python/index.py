#FUNKSIYADAN ODDIY QIYMAT QAYTARISH
def toliq_ism_yasa(ism, familiya):
    """Toliq isma qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism # qiymat qaytarish uchun return operatorini ishlatiladi

talaba1 = toliq_ism_yasa('olim','hakimov')
talaba2 = toliq_ism_yasa('hakim','olimov')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
#Natija:Darsga kelmagan talabalar: olim hakimov va hakim olimov


#IXTIYORIY ARGUMENTLAR
def toliq_ism_yasa(ism, familiya, otasining_ismi=''):#otsining ismi='' digan joy ixtiyoriy bosh joy
    """Toliq isma qaytaruvchi funksiya"""
    if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()

talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
#Natija: Darsga kelmagan talabalar: Olim Hakimov va Hakim Abrorovich Olimov


#FUNKSIYADAN LUG'AT QAYTARAMIZ
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
avtolar = [avto1, avto2]
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
#Onlayn bozordagi mavjud avtomashinalar:
# Qora Malibu. Narhi: Noma'lum
# Oq Gentra. Narhi: 15000

#FUNKSIYADAN RO'YXAT QAYTARAMIZ
def oraliq(min,max):
    sonlar = [] # bo'sh ro'yxat
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar

print(oraliq(0,10))
print(oraliq(10,21))
#Natija: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#shu ko'rinishda chiqadi

#FUNKSIYALARNI TSIKLDA ISHLATISH
print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break

# #Natija:
# Saytimizdagi avtolar ro'yxatini shakllantiramiz.

# Quyidagi ma'lumotlarni kiritingIshlab chiqaruvchi: gm  
# Modeli: gentra
# Rangi: qora
# Korobka: avto
# Ishlab chiqarilgan yili: 2022
# Narhi: 120000
# Yana avto qo'shasizmi? (yes/no): no

