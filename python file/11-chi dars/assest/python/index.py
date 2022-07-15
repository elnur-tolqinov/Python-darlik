yosh = int(input('Yoshingiz nechida? '))
if yosh<=4: # yosh bolalarga bepul
    narx = 0
elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm  elif if va else qoshilgani degan manoda 
    narx = 5000
elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
    narx = 10000
else: # qariyalarga esa 8000 so'm
    narx = 8000
print(f"Sizga kirish {narx} so'm")
#Natija Yoshingiz nechida? so'raganda 12 yoshdan kichik yoki teng bolsa elif operatori Sizga kirish 5000 so'm degan so'zni chiqaradi

#or operatori
kun = input("Bugun nima kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')
#natija: Bugun nima kun?>>> deb so'raganda shanba yoki yakshanba yozilsa Bugun dam olish kuni. deb chiqaradi 
# or opretori yoki degan manoni bildiradi
# Bugun nima kun?>>> deb so'raganda shanba yoki yakshanba dan boshqa kun yozilsa Bugun ish kuni. deb chiqaradi

#and operatori
kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
    print("Cho'milgani ketdik!")
elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
    print("Uyda dam olamiz!")
#Natija: Bugun nima kun? so'raganda kuni yozganimizdan keyin Havo harorati qanday? deb so'raydi 40 bo'lsa
#bunda kuni shanba yoki yakshanba bolsa harorat 30 dan katta bolsa Cho'milgani ketdik! degan so'z chiqadi
#natija dushanba bolsa harorat 30dan kichik bolsa Uyda dam olamiz! degan so'z chiqadi

#Boolean malumot turi
#shartlarni ketma ketligini tekshirish
narh = 15000 # mijoz 15 so'mga ovqat oldi
choy = True #true mijoz oldi degan manoni beradi
salat = False#false mijoz olmadi degan manoni beradi
non = True
kompot = True
assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy:   # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:    # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot: # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti: # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000
    
print(f"Jami {narh} so'm")
#natija: 
#Mijoz choy oldi
#Mijoz non oldi 
#Mijoz kompor oldi
#Jami 25000 so'm

#in operatori
#in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini tekshirishiradi.
menu = ['osh','qazonkabob','shashlik','norin','somsa']
'manti' in menu # menu da manti bormi?
#Natija: False  yani ro'yhatda manti yoq

menu = ['osh','qazonkabob','shashlik','norin','somsa']
'osh' in menu # menu da osh bormi?
#Natija: True yani ro'yhatda osh bor

menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi.')
else:
    print('Afsuski bizda bunday ovqat yo\'q')
#Natija: Nima ovqat yeysiz?>>> soraganda somsa yozsak Buyurtma qabul qilindi. deb chiqadi
#Natija: Nima ovqat yeysiz?>>> soraganda sho'rva yozsak Afsuski bizda bunday ovqat yo'q deb chiqadi

#not in operatori
#not in operatori yordamida esa biror element ro'yxatda yo'qligini tekshiradi
menu = ['osh','qazonkabob','shashlik','norin','somsa']
'osh' not in menu # menu da osh yo'qmi?
#Natija: False chiqadi ro'yhatda chunki osh bor

menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() not in menu:
    print('Afsuski bizda bunday ovqat yo\'q')
else:
    print('Buyurtma qabul qilindi.')
#Nima ovqat yeysiz?>>> soraganda somsa yozsak Buyurtma qabul qilindi. deb chiqadi

#2 ta ro'yhatni tekshirish
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")
#natija: buyurtmalar ro'yhatni menu bilan solish tiradi agar menu bolsa
# Menuda soma bor kabi so'z chiqadi agar menu yoq bolsa Kechirasiz, menuda manti yo'q kabi so;z chiqadi