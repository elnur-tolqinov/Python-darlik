#KLASS YARATISH
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

#KLASSDAN OBYEKT YARATAMIZ
talaba1 = Talaba("Alijon","Valiyev",2000)

#OBYKETNING XUSUSIYATLARINI KO'RISH
print(talaba1.ism)
#Natija: Alijon
print(talaba1.familiya)
#Natija: Valiyev

#KLASSDAN BIR NECHTA OBYEKTLAR YARATISH
talaba2 = Talaba("Olim","Olimov",1995)
talaba3 = Talaba("Husan","Akbarov",2004)
talaba4 = Talaba("Hasan","Akbarov",2004)

print(talaba2.ism)
print(talaba4.familiya)
#Natija:
#Olim 
# Akbarov

#KLASSGA METODLAR QO'SHAMIZ
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")
#OBYEKTNING METODLARIGA MUROJAT QILAMIZ
talaba4 = Talaba("Hasan","Akbarov",2004)
talaba4.tanishtir()
#Natija: Ismim Hasan Akbarov. 2004 yilda tu'gilganman

#Klassimiz istalgancha metodlardan iborat bo'lishi mumkin:
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")

talaba1 = Talaba("Alijon","Valiyev",2000)
print(talaba1.get_fullname())
#Natija: Alijon Valiyev


#ARGUMENT QABUL QILUVCHI METODLAR
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil
    
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")

talaba1 = Talaba("Alijon","Valiyev",2000)
print(talaba1.get_age(2021))
#Natija: 21