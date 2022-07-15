def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])#bunda : bo'lish belgisi ro'yhatdan nusxa oladi va ichidagi malumotlarni o'zgarishiga yo'l qoymidi
print(baholar)
print(talabalar)
#Natija:
#Talaba Husanning bahosini kiriting: 5
# Talaba Hasanning bahosini kiriting: 5
# Talaba Valining bahosini kiriting: 5 
# Talaba Alining bahosini kiriting: 5
# {'husan': '5', 'hasan': '5', 'vali': '5', 'ali': '5'}
# ['ali', 'vali', 'hasan', 'husan']
