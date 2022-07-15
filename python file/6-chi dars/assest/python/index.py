a = 20 
b = -30 # minus bo'lishi mumkin
c = a + b
print(c)
#Butun sonlarni ham o'zgaruvchida saqlash, ularning ustida qo'shish (+), ayirish (-), ko'paytirish(*), bo'lish (/) kabi 
#arifmetik amallar bajarsa bo'ladi

# Kvadratning yuzini hisoblaymiz
kvdrt_tmni = 20 # Kavdratning tomoni 20 ga teng
kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
print(kvdrt_yuzi)

PI = 3.14159 # o'nlik son (float) Agar o'zaruvchi katta harfda yozilgan bolsa KONSTANTA bo'ladi uni ichidagi ma'lumotlar o'zgartirish mumkin emas
radius = 10  # butun son (integer)
diametr = 2*radius
print("Aylana uzunligi ", PI*diametr, " ga teng.")
#Natija: Aylana uzunligi 4.712384999999999 ga teng.

#ikki butun sonni bo'lish (/) natijasida o'nlik son hosil bo'ladi (natija butun bo'lsa ham).
a = -20
b = 40
c = b/a
print(c) # natija o'nlik son bo'ladi
#Natija: -2.0

#butun va o'nlik sonlar o'rtasidagi har qanday arifmetik amallarning natijasi ham o'nlik son bo'ladi.
a = 2
b = 3.0
# Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
print(a+b) 
print(a*b)
print(a**b)
print(2*(a+b))
#Natijalar: 2.0 , 5.0 , 6.0 , 8.0 , 10.0

#Uzun sonlarni kiritishda, qulaylik uchun, raqamlarni pastki chiziq (_) yordamida
#guruhlash mumkin. Python - son tarkibidagi pastki chiziqlarni (_) inobatga olmasdan, uzun sonligicha qabul qiladi.
aholi_soni = 7_594_000_000 # o'qishga qulay bo'lishi uchun shinday yoziladi
print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")
#Natija: Yer kurrasida 7594000000 ga yaqin odam yashaydi

#O'ZGARUVCHI TURINI ALMASHTIRISH
#str()— int yoki float turidagi sonlarni matnga o'zgartiradi.
#int()— matn yoki float ko'rinishidagi qiymatlarni butun songa o'zgartiradi. Bunda matn butun son ko'rinishida bo'lishi kerak.
#float()— matn yoki int ko'rinishidagi qiymatlarni o'nlik songa o'zgartiradi.

ism = 'Jobir'
yosh = 36
xabar = ism + ' ' + str(yosh) + ' yoshda' #yoshni qiymat int edi str matn ga aylantiryapdi
print(xabar)
#Natija: Jobir 36 yoshda

#O'ZGARUVCHI TURINI TEKSHIRISH

ism = 'Jobir'
yosh = 36
print(type(ism))  # ism degan o'zgaruvchining turini konsolga chiqaramiz
print(type(yosh)) # ismyosh degan o'zgaruvchining turini konsolga chiqaramiz
#Natija: <class 'str'> , <class 'int'>

#1 foydalanuvchining tug'ilgan yilini so'raydi va qiymatni int ga aylantiradi
t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#2 foydalanuvchi yoshini xisoblaydi
yosh = 2022 - t_yil # 
#3 foydalanuvchi yoshini konsolga chiqaradi
print("Siz " + str(yosh) + " yoshda ekansiz")
#Natija: 
#Tug'ilgan yilingizni kiriting: 2006 
#Siz 16 yoshda ekansiz