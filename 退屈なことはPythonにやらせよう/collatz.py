#collatz数列

print("整数を入力してください:")
number = int(input())

def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1

print(collatz(number))
