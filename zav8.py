def main(a,b,c):
    positive = 0
    if a > 0:
        positive +=1
    if b > 0:
        positive +=1
    if c > 0:
        positive +=1
    print("Кількість позитивних чисел = ",positive)

a = int(input("Pershe chislo: "))
b = int(input("Druge chislo: "))
c = int(input("Trete chislo: "))
main(a,b,c)