# *args Usuli
#Quyidagi misolni ko'raylik. summa() nomli funksiyamiz istalgancha sonlarni qabul qilib oladi, va ularning yi'gindisi hisoblaydi:
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1,2))
print(summa(1,2,3,4,5))
#Natija: 
# 3 
# 15

def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)

print(summa(4,5,6,7))
#Natija: 22
#bu kod sonlarni yindisini aniqlash uchun eng osson usuli


def summa(x,y,*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return x+y+sum(sonlar)

print(summa(2,2))
#Natija: 4
#bu kodda kamida 2ta raqam yozish kerak boladi


# **kwargs usuli
#**kwargs — keyword arguments (kalit so'zli argumentlar)
def avto_info(kompaniya,model,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
print(avto2)
#Natija: {'rang': 'qizil', 'narh': 35000, 'kompaniya': 'Kia', 'model': 'K5'}
