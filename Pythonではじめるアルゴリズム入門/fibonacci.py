def fibonacci(n):
    if n== 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("数字を入力してください: "))
for i in range(n):
    print(fibonacci(i))