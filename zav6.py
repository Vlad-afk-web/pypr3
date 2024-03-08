def main(a,b):
    if a == b:
        a = 0
        b = 0
    else:
        v = max(a,b)
        a = v
        b = v
    print(a,b)
a = int(input("Перше число "))
b = int(input("Друге число "))
main(a,b)
