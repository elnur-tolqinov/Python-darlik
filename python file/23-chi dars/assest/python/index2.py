import avto_info_mod # avto_info_mod faylini (modulini) chaqiramiz

avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
avto_info_mod.info_print(avto1)

#MODULGA QISQA NOM BERISH
import avto_info_mod as aim # as fuksiyasi orqali avto_info_mod ni qisqa nom aim bilan chaqiriladi 

avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
aim.info_print(avto1)

#MODUL ICIHDAN MA'LUM FUNKSIYALARNI KO'CHIRIB OLISH
from avto_info_mod import avto_info, info_print

avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)

#FUNKSIYALARGA QISQA NOM BERISH
from avto_info_mod import avto_info as ainfo, info_print as iprint

avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
iprint(avto1)

#MODUL ICHIDAGI BARCHA FUNKSIYALARNI KO'CHIRIB OLISH
from avto_info_mod import *

avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)

# sqrt()- qavs ichida berilgan qiymatning kvadrat ildizini qaytaradi
import math

x=400
print(math.sqrt(x))
#Natija: 20.0

#pow(x,y) - x ning y-darajasini qaytaradi
print(pow(5,5))
#Natija: 3125

#pi -  ning qiymatini saqlovchi o'zgaruvchi
from math import pi
print(pi)
#Natija: 3.141592653589793

# log2(x) va log10(x)ning 2 va 10-lik logorifmini qaytaruvchi funksiyalar
print(math.log2(8))
print(math.log10(100))

#random  MODULI 
#randint(a,b)
import random as r # random modulini r deb chaqirayapmiz

son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
print(son)


#choice(x)
ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

x = list(range(0,51,5))
print(x)
print(r.choice(x))
#Natija: [0,5,10,15,20,25,30,35,40,45,50]
#20


#shuffle(x)
x = list(range(11))
print(x)
r.shuffle(x)
print(x)
#[0,1,2,3,4,5,6,7,8,9,10]
#[6,10,2,4,9,1,5,0,3,7,8]
