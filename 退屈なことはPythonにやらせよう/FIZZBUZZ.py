i = str(input("数値を入力してください:"))

if str.isdigit(i) == True:
    num = int(i)
    if num%6 == 0:
        print("FIZZBUZZ")
    elif num%3 == 0:
        print("BUZZ")
    elif num%2 == 0:
        print("FIZZ")

else:
    print("誤った入力値です")


print("おわり")







