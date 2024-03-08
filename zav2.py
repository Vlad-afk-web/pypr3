import math

def main(x1,x2,y1,y2):
    a = math.sqrt(x1 ** 2 + y1 ** 2)
    b = math.sqrt(x2 ** 2 + y2 ** 2)
    if a < b:
        return "Точка A ближча до початку координат"
    elif b < a:
        return "Точка B ближча до початку координат"
    else:
        return "Точки A і B знаходяться на однаковій відстані до початку координат"

x1 = int(input("Перша координата першої точки: "))
y1 = int(input("Друга координата першої точки: "))
x2 = int(input("Перша координата другої точки: "))
y2 = int(input("Друга координата другої точки: "))

result = main(x1,x2,y1,y2)
print(result)
