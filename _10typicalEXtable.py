from math import *


table=[1,2,3,4,5]
abc=['Abc','B','C']
word="Programmeerimine"
word_list=list(word)
print(word)
print(word_list)
while True:
    print("1 - lisab täht loeteluse")
    print("2 - limib loeteluse")
    print("3 - sisestab täht valitud i- positsionile")
    print("4 - kustutab element")
    print("5 - sorteerib vastavalt kasvale")
    print("6 - sorteerib vastavalt kahanevale")
    print("7 - kustutab tähe vastavalt valitud positsioonile")
    print("8 - jagab loetelu")
    print("9 - kuvad sisestatud numbri all")
    print("10 - puhastab loetelu")
    try:
        valik=int(input())
    except:
            print("Vale andmetüüp")
    if valik==1:
        try:
            a=input("Sisesta täht: ")
            word_list.append(a)
            print(f"Lisanud {a} uue loeteluse",word_list)
        except:
            print("Vale andmetüüp")
    elif valik==2:
        try:
            word_list.extend(abc)
            print(word_list)
        except:
            print("Vale andmetüüp")
    elif valik==3:
        try:
            a=input("sisesta täht, mille tahad lisada: ")
            i=int(input("sisesta number positsiooni, kuhu tahad lisada: "))
            word_list.insert(i-1,a)
            print(word_list)
        except:
            print("Vale andmetüüp")
    elif valik==4:
        try:
            a=input("sisesta täht, mille tahad kustutada: ")
            n=word_list.count(a)
            if n>0:
                for i in range(n):
                    word_list.remove(a)
            else:
                print("Sellist tähte pole: ")
            print(word_list)
        except:
            print("Vale andmetüüp")
    elif valik==5:
        try:
            word_list.sort()
            print(word_list)
        except:
            print("Vale andmetüüp")
    elif valik==6:
        try:
            word_list.sort(reverse=True)
            print(word_list)
        except:
            print("Vale andmetüüp")
    elif valik==7:
        try:
            i=int(input("vali tähe positsiooni, kust tahad kustutada: "))
            word_list.pop(i)
            print(word_list)
        except:
            print("Vale andmetüüp")
    elif valik==8:
        try:
            a=input("sisesta täht, mille tahad jagada: ")
            i=int(input("vali palju korda tahad jagada: "))
            x=word.split(a,i)
            print(x)
        except:
            print("Vale andmetüüp")
    elif valik==9:
        try:
            a=int(input("sisesta number: "))
            print(word_list(a-1))
        except:
            print("Vale andmetüüp")
    elif valik==10:
        try:
            word.clear()
            print(word)
        except:
            print("Vale andmetüüp")