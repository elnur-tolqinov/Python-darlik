#for operatori takrorlovchi 
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)
#Natija:
# Ali 
# Vali 
# Hasan 
# Husan 
# Olim     shu ko'rinishda chiqadi bunda for takrorlovchi mehmon digan o'zgaruvchini mehmonlar ichidagi 
#ismlarga tenglabdi bunda for operatori har bitta ismni alohida alohida chiqaradi.

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi")
#Natija: 
#Hurmatli Ali, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
#Hurmat bilan, Palonchiyevlar oilasi
#bunda har bitta ism uchun alohida matn chiqaradi 

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
print("Hurmat bilan, Palonchiyevlar oilasi\n")
#Natija:
#Hurmatli Ali, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
#Hurmatli Vali, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
#Hurmatli Hasan, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
#Hurmatli Husan, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
#Hurmatli Olim, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz
#Hurmat bilan, Palonchiyevlar oilasi                                kodimizda 4-qatorni o'ngga surmaganimiz uchun, Python 
# bu qatorni tsikl tashqarisida deb qabul qildi va faqatgina 1 marta, tsikl tugaganidan so'ng bajardi. 

#for yordamida sonli ro'yhatlar bilan ishlash

sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
#Natija: 
# 1 ning kvadrati 1 ga teng
# 2 ning kvadrati 4 ga teng
# 3 ning kvadrati 9 ga teng
#shunga o'xshab 1 dan 10 gacha sonnig kvadratini chiqaradi bu kod

sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
for son in sonlar:  # sonlar dagi har bir son uchun
    sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

print(sonlar)
print(sonlar_kvadrati)
#Natija
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] sonlar 
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100] tepadagi sonlarni kvadrati

dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)
#Natija:
#5 ta eng yaqin do'stingiz kim?
#1-do'stingizning ismini kiriting: Shahobddin #bunda input ismni yozishimizni so'rayapdi
#2-do'stingizning ismini kiriting: Javlon #bunda input ismni yozishimizni so'rayapdi
#3-do'stingizning ismini kiriting: Shaxzod #bunda input ismni yozishimizni so'rayapdi
#4-do'stingizning ismini kiriting: Shoxjahon #bunda input ismni yozishimizni so'rayapdi
#5-do'stingizning ismini kiriting: Mirjahon #bunda input ismni yozishimizni so'rayapdi
#['Shahobiddin', 'Javlon', 'Shaxzod', 'Shoxjahon', 'Mirjahon'] #ohirida shu korinishda chiqadi
