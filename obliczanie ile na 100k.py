print("Obliczanie ile na 100k")

kraj = int(input("Ile osób jest w twoim kraju? "))
zakazenia = int(input("Ile jest osób zakazonych dziennie? "))

kk = kraj / 100000
wynik =  zakazenia / kk

print(wynik)

if wynik>70:
    print("NARODOWA KWARANTANNA")

if 50<wynik<70 :
    print("BEZPIECZNIK")

print("(c) Badis 2020")

wyjscie = int(input("kliknij enter aby zakończyć program..."))
print(wyjscie)