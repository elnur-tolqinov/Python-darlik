#lambda YOHUD NOMSIZ FUNKSIYA
lambda argument:ifoda
#Lambda funksiyalari istalgan miqdordagi argumentlarga ega bo'lishi mumkin, ammo funksiya badanida faqat bitta ifoda mavjud bo'ladi.
# Ifoda bajariladi va qaytariladi (return operatori shart emas).

import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10)) #math funksiyasi python saytdan olingan
#Natija: 62.83185307179586

def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")
#Natija: 3-ning kvadrati 9 ga, kubi 27 ga teng


#map() Funksiyasi
from math import sqrt

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar))
#Yuqoridagi misolda avval 0 dan 10 gacha sonlar ro'yxatini tuzib oldik, keyin esa map funksiyasiga ro'yxat va sqrt 
# funksiyasini uzatib, ro'yxatdagi barcha sonlarning ildizini hisoblab oldik. 
#map() funksiyasi map obyekt qaytargani sababli, qaytgan obyektni ro'yxatga o'tkazib olish uchun list() funksiyasidan foyydalandik.

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x #bu sonlarni kavdratni hisoblayabdi

print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz
#Natija: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

kvadratlar = list(map(lambda x:x*x,sonlar)) #sonlar ning kvadratini lambda yordamida hisoblaydi
print(kvadratlar)
#Natija: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b)) #betta x ni a olinyapdi y esa b deb olinyapdi
print(a_plus_b)
#Natija: [11, 13, 15]

ismlar = ['hasan','husan','olim','umid']
print(list(map(lambda matn:matn.upper(),ismlar)))
#Natija: ['HASAN', 'HUSAN', 'OLIM', 'UMID']


#filter() funksiyasi
import random as r #ramdom funksiyasi ungan berilgan malumotni istagan bittasi tanlab chiqarib beradi

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar

def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
    return x%2==0

juft_sonlar = list(filter(juftmi,sonlar))
print(sonlar)
print(juft_sonlar)
#bu kodda randdomdan kelgan kodni ichidagi juft sonlarni ajratadi


import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

print(sonlar)
print(juft_sonlar)
#bu  kodda lambda yordamida randdomdan kelgan sonlarni ichidagi juft sonlarni ajratadi


mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevalar_b)
#bu kodda b boshlangan gapni ajratib oladi

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)
#Natija: ['olma', 'anor', 'anjir', "o'rik", 'qovun', 'banan']
#mevalar ro'yxatidan harfi 5 yoki undan kam harfdan iborat mevalarni tanlab oladi
