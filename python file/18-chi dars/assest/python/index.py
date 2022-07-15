#WHILE YORDAMIDA RO'YXATNI TO'LDIRISH
ismlar = []

print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
n=1 # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-do'stingiz ismini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    if javob =='ha': #if Yana ism qo'shasizmi? (ha/yo'q) digan ha disa kodni davom etiradi yoq desa break qiladi yani kodni tugatadi
        n+=1
        continue
    else:
        break
#Natija: 
# Yaqin do'stlaringiz ro'yxatini tuzamiz.
# 1-do'stingiz ismini kiriting: olim
# Yana ism qo'shasizmi? (ha/yo'q)  #soraganda ha disa yana dostingizni ismini qo'shishini so'raydi yo'q disak kod to'xtaydi

print("Do'stlaringiz yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False # yana qo'shisizmi diganda yoq disak ishor false ga o'zgarib kod to'xtaydi

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")

#Natija: 
#Do'stlaringiz yoshini saqlaymiz.
#Do'stingiz ismini kiriting: Javlon
#Javlonning yoshini kiriting: 16
#Yana ma'lumot qo'shasizmi? (ha/yo'q) yo'q
#Javlon 16 yoshda 
#kod shunday ishlaydi

#RO'YXAT ELEMENTLARINI O'CHIRISH
cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
    cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
print(cars)
#Natija: ['lacetti', 'toyota', 'audi', 'malibu']
#Yuqoridagi tsikl toki cars degan ro'yxatda 'nexia' qiymati tugagunga qadar takrorlanaveradi.

#RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH
talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar: #bu kod talabalar ichidagi malulot tugaguncha ishlaydi 1chi ro'yhatdan olib o'zgartirib 2-chi ro'yhatga yuklaydi
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = baho
#Botirning bahosini kiriting:5 
#Botir baholandi

