import sys
import math
import sys as system
#zad1
sporty=["pilka nozna","siatkowka","skoki narciarskie"]
sporty.reverse()
sporty.extend(("hokej","golf"))
print(sporty)

#zad2

skroty={"al":"aleja","cd":"ciag dalszy","dr":"doktor","lek":"lekarz"}
print(skroty)

#zad3
#slownik gier. klucz to nazwa gry, a wartosc typ gry

gry={"fifa":"sportowa","quake":"strzelanka","half-life":"strzelanka","guitar hero":"muzyczna"}

#zad4
print("Program liczy literke 'a'")
zdanie=input("Wpisz dowolny tekst\n")
b=zdanie.count("a")
print(b)

#zad5
system.stdout.write("podaj a  ")
a=system.stdin.readline()
system.stdout.write("podaj b  ")
b=system.stdin.readline()
system.stdout.write("podaj c  ")
c=system.stdin.readline()
a=int(a)
b=int(b)
c=int(c)
wynik=a**b*c
system.stdout.write(str(wynik))






#zad6

a=input("podaj a  ")
b=input("podaj b  ")
c=input("podaj c  ")

if (a>b)&(a>c):
    print("Liczba a jest najwieksza")
elif (b>a)&(b>c):
    print("liczba b jest najwieksza")
else:
    print("liczba c jest najwieksza")

#zad7

lista=[4,5.5,8,10,3.4,11,9]
lista2=[]
for liczba in lista:
    wynik=liczba**2
    lista2.append(wynik)
    print(wynik)



#zad9
a=input("podaj liczbe  ")
a=int(a)

if (a>0):
    wynik=math.sqrt(a)
    print("pierwiastek z tej liczby to "+str(wynik))
else:
    print("podano nieprawidlowa wartosc")
