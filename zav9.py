def main(a,b,c):
    cile = 0
    if a.is_integer():
        cile +=1
    if b.is_integer():
        cile +=1
    if c.is_integer():
        cile +=1
    print("Кількість цілих чисел = ",cile)

a = float(input("Pershe chislo: "))
b = float(input("Druge chislo: "))
c = float(input("Trete chislo: "))

main(a,b,c)