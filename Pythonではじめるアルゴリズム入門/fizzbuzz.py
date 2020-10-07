#1から50の数を出力
#なお、3の倍数の時はFizz, 5の倍数の時はBuzz, 3の倍数かつ5の倍数の時はFizzBuzzと出力

def fizzbuzz(i):
        if (i % 3 == 0):
            if (i % 5 == 0):
                 return 'FizzBuzz'
            return 'Fizz'
        elif (i % 5 == 0):
            return 'Buzz'
        else:
            return i

for i in range(1, 51):
    print(fizzbuzz(i), end=' ')