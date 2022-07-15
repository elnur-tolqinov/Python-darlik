#FUNKSIYA YARATAMIZ
def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")
# bu kodda funksiya yaratiladi salom_ber() deb yozsak ichidagi Assalomu alaykum! chiqadi
salom_ber()
#Natija: Assalomu alaykum!

#FUNKSIYAGA QIYMAT UZATISH
def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""# bu funksiya haqida malumot yozib qo'yiladi
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
salom_ber('hasan') 
#bu kodda salom_ber('') ichidagi hasan ni ism orqali chaqrib olyapdi 


#DOCSTRING
print(salom_ber.__doc__) #bu kod .__doc__ funksiyaga berlgan mulotni chiqara 
#Natija: Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya #shu korinishda chiqadi

#FUNKSIYAGA BIR NECHA BOR MUROJAT QILISH
salom_ber('hasan')
salom_ber('olim')
#Natija:
#Assalomu alaykum, hurmatli Hasan! 
#Assalomu alaykum, hurmatli Olim!

#Foydalanuvchi funksiyaga murojat qilishda funksiyaga uzatgan qiymat esa argument deb ataladi.
# salom_ber('hasan') kodida 'hasan' bu argument. 


#TO'G'RI TARTIBDA UZATISH
def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")

toliq_ism('olim','hakimov')
#Natija: 
#Foydalanuvchi ismi: Olim
#Foydalanuvchi familiyasi: Hakimov

def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2022-tugilgan_yil} yoshda")

yosh_hisobla('olim', 1997)
yosh_hisobla(tugilgan_yil=1997, ism='olim') #argumentni uzatishda kalit so'z bilan jo'natish ening maquli shu
# Natija:Olim 25 yoshda

