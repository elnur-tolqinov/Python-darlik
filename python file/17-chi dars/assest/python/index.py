#while TSIKLI BILAN TANISHAMIZ
son = 1 # son ga 1 qiymatini beramiz
while son<=5: # while tsikli son digan o'zgavchini 5ga teng boguncha 1 qo'shi boradi
    print(son, end=' ') # son ni konsolga chiqaramiz,
    son = son+1 # songa 1 qo'shamiz.
#Natija: 1 2 3 4 5

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit': 
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
#Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): 5
#25.0
#Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): exit deb yozilsa kod kvadrat hisoblashdan to'xtaydi

#Ishora
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
#bunda exit deb yozilsa ishora truedan false ga o'zgarib kod kvadrat hisoblashdan to'xtaydi

#Break operatori
sonlar = list(range(1,11))
for son in sonlar: 
    if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
        break
    print(f"{son} ning kvadrati {son**2} ga teng")
#Natija:
# 1 ning kvadrati 1 ga teng 
#kod 1 dan 4gacha shunday chiqdi 5 ga kelib to'xtaydi qo'lganin hisoblamaydi


#Continue operatori
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")
#Natija:
# 1 ning kvadrati 1 ga teng 
#kod 1 dan 10gacha shunday chiqdi faqat 5ga kelib 5ni tashlab ketadi 

son = 0
while son<10:
    son += 1
    if son%2!=0: # !=0 bo'lsa to'g' sonlar chiqadi !==0 bolsa juft sonlar chiqadi
        continue
    else:
        print(son)
#Natija: 
# 1
# 3 
# 5  
# 7
# 9