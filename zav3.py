def main(a,b):
    c = 180 - (a + b)
    total = a + b + c 
    if total == 180 and 0 < a < 180 and 0 < b < 180 and 0 < c < 180:
        if a == 90 or b == 90 or c == 90:
            print("Прямокутник існує і є прямокутним")
        else:
            print("Прямокутник існує")
    else:
        print("Прямокутник не існує")

a = int(input("перший кут "))
b = int(input("другий кут "))

result = main(a,b)
