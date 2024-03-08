def main(a,b,c,k):
    if a % k == 0:
        print(k, " є дільником числа ", a)
    if b % k == 0:
        print(k,  "є дільником числа " , b)
    if c % k == 0:
        print(k, " є дільником числа ", c )

a = float(input("Pershe chislo: "))
b = float(input("Druge chislo: "))
c = float(input("Trete chislo: "))
k = float(input("Dilnik: "))

main(a,b,c,k)
