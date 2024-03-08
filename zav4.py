def main(x,y):
    if x == y:
        print("Числа рівні")
    elif x > y:
        v = (x + y) / 2 
        b = (x * y) * 2
        x = b
        y = v
        print(x,y)
    else:
        b = (x + y) / 2 
        v = (x * y) * 2
        x = b
        y = v
        print(x,y)

x = int(input("Перше число "))
y = int(input("Друге число "))
main(x,y)
