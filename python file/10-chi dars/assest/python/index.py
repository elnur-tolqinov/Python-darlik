#if operatori
avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
    else: # aks holda ... 
        print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.
#bunda if avto digan ro'yhat bmw ga teng bolsa hamma harfni katta qilib yoz debdi
#bunda else avto digan ro'yhat bmw ga teng bolmasa matnlarni birinchi harfni katta qilib yoz debdi
#Natija:
#Audi
#BMW
#Volvo 
#Kia 
#Hyundai
#natija shu ko'rinishada chiqadi

#Tepadagi misolni tekshirish uchun == operatoridan foydalandik. Bu operatorni oddiy tilga tarjima qilsak 
#"tengmi?" degan ma'noni beradi.
# Agar shartning ikki tarafidagi qiymatlar teng bo'lsa ifoda TRUE qiymatini qaytaradi TRUE-to'g'ridigan manomi beradi
#teng bo'lmasa FALSE qaytaradi FALSE-noto'gri degan manoni beradi

ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
else:
    print("Salom, Ali")
#Natija ism soriydi ismga vali yozsam aliga teng bo'lmasa Uzr, Vali biz Alini kutayapmiz. degan so'z chiqadi
#ism ali ga teng bolsa Salom Ali degan so'z chiqadi

yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
    print('Xush kelibsiz!')
else: # ask holda
    print('Kirish mumkin emas!')
#natija Yoshingiz nechida?>>> so'raganda 15 deb yozilsa Kirish mumkin emas! degan so'z chiqadi
#natija Yoshingiz nechida?>>> so'raganda 18 yoki undan katta son yozilsa Xush kelibsiz! degan so'z chiqadi

login = input("Yangi login tanlang:")
if len(login)<=5: # login uzunligini tekshiramiz
    print("Login 5 harfdan ko'proq bo'lishi shart!")
#natija Yangi login tanlang: so'ragn payti 5 tadan kam yoki 5ta so'z yozsak Login 5 harfdan ko'proq bo'lishi shart! degan so'z chiqadi

yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2022-yil<18: # foydalanuvchining yoshini hisoblaymiz
    print(f"Yoshingiz {2020-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")
#Natija: Tug'ilgan yilingizni kiriting: soraganda yil yozamiz va u yilni 2022 yildan ayirib natijani 18 ga tenglab 
# koradi 18 dan katta bo'sa yoki teng bolsa Yoshingiz 18 da ekan. Xush kelibsiz! degan so'z chiqadi
# agar yosh 18dan kichkina chiqsan yoshingiz yozib Kirish mumkin emas! degan soz chiqadi

yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>65: print("Siz COVID-19 risk guruhida ekansiz") 
#natija yoshhingiz 65 dan katta bolsa Siz COVID-19 risk guruhida ekansiz shu so'zni chiqaradi bu Bir qatorli if/else deb ataladi
#yoki yana bitta misol
x, y = 25, 50 # x=25 va y=50
print("x>y") if x>y else print("x<y")
#Natija: x<y
