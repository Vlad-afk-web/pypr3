def main():
    numbers = []
    for i in range(3):
        num = int(input("Chisla: "))
        numbers.append(num)
    squared = [num ** 2 for num in numbers if num >= 0]
    to_the_fourth_power = [num ** 4 for num in numbers if num < 0] 
    print (squared, to_the_fourth_power)

if __name__ == "__main__":
    main()
