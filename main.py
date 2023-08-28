def main(number):
    return "Вы выйграли" if number == "5" else "Вы проиграли"

def game():
    while True:
        toast = input("Введите число от 1 до 10: ")
        print(main(number=toast))

if __name__ == '__main__':
    arr = []
    for i in range(1,11):
        arr.append(i)
    print(arr[7::])
    # game()