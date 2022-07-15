import random

def son_top(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato men o'ylagan son bundan kattaroq. Yana harakat qilib ko'rin:")
        elif taxmin>tasodifiy_son:
            print("Xato men o'ylagan son bundan kichikroq. Yana harakat qilib ko'rin:")
        else:
            break
    print(f"Tabriklamiz. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar 

# son_top()

def sontop_pc(x=10):
    print(f"1 dan {x} gacha son oylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x

    while True:
        # taxminlar +=1
        if quyi != yuqori:
            taxmin=random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
        f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())

        if javob =='-':
            yuqori=taxmin -1
        elif javob == '+':
            quyi = taxmin +1
        else:
            break
    print("Topdim")
    # print("Men {taxminlar} ta taxmin bilan topdim!")
    # return taxminlar

# sontop_pc()

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = son_top(x)
        taxminlar_pc = sontop_pc(x)

        if taxminlar_user>taxminlar_pc:
            print("Men yudim!")
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutdingiz")
        else:
            print("Durrang")
        yana = int(input("Yana o'ynaysizmi? Ha (1)/Yo'q(0):"))

play()