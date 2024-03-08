def main(a,b,c):
    negative = 0
    if a < 0:
        negative +=1
    if b < 0:
        negative +=1
    if c < 0:
        negative +=1
    print("Кількість негативних чисел = ",negative)

a = int(input("Pershe chislo: "))
b = int(input("Druge chislo: "))
c = int(input("Trete chislo: "))
main(a,b,c)