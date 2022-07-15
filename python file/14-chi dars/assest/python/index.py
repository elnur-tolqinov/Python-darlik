#Lug'atlar bilan ishlash

car_0 = {'model':'ferrari','rang':'qizil'}
print(car_0['model'])
print(car_0['rang'])
#Natija: 
# ferrari
# qizil
#bunda car_0 o'zgaruvchi unichida model kalit bilan malumotni : yani 2ta nuqata da boglab turadi

talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(f"{talaba_0['ism'].title()},\
 {talaba_0['t_yil']}-yilda tu'gilgan,\
 {talaba_0['yosh']} yoshda")
 #Natija: Murod Olimov, 2000-yilda tu'gilgan, 20 yoshda 
 # bu kodda \ silish bilan uzun kodlarni qatorlarga bo'lib yozsa bo'ladi


#Yangi kalit qo'shish
talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika' 
#Natija: {'ism': 'abdulloh', 'yosh': 20, 't_yil': 2000, 'kurs': 4, 'fakultet': 'informatika'}


#Bo'sh lug'atga kalit va qiymatlar yuklash
talaba_1 = {}
talaba_1['ism'] = 'qobil rasulov' #ism digan kalit ochib qobil rasulov uning monosi qiymati deb beribdi
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
#Natija: 
#{'ism': 'qobil rasulov', 'kurs': 3, 'yosh': 20}
#Talaba Qobil Rasulov 3-kurs

#ro'yhatdagi kalit qiymatlarini o'zgartirish
talaba_1['kurs'] = 4 # 'kurs' ni 4 ga o'zgartirildi
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
#Natija: Talaba Qobil Rasulov 4-kurs


#KALIT va SO'Z-QIYMAT O'CHIRISH
talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(talaba_0)
del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
print(talaba_0)
#Natija:
#{'ism': 'murod olimov', 'yosh': 20, 't_yil': 2000} 
#{'ism': 'murod olimov', 't_yil': 2000}


#LUG'ATNI QATORLARGA BO'LIB YOZISH
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
#qatorga bo'lib yozishda , vergul bilan ajratib yozib ketiloradi


#get() METODI
phone = telefonlar['ali']
print(f"Alining telefoni {phone}")
#Natija: Alining telefoni iphone x

phone = telefonlar.get('hasan','Bunday ism mavjud emas')
#royhatda hasan digan so'z bo'lmasa .get  Bunday ism mavjud emas dugan so'zni chiqaradi

phone = telefonlar.get('hasan')
print(phone)
#Natija: None .get ga hech qanday gap yozilmasa None digan so'z chiqara none diga yoq digan manoni beradi
