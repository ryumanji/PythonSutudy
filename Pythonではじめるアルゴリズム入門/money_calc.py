#おつりの枚数を最小にするプログラム

import sys
try:
    insert_price = int(input('insert: '))
    product_price = int(input('product: '))
except ValueError:
    print("整数を入力してください")
    sys.exit()
    
value = [5000, 1000, 500, 100, 50, 10, 5, 1]

def calc():
    change = insert_price - product_price
    if change < 0:
        print('金額が不足しています。')
        sys.exit()

    for e in value:
        print(e, ' : ', change // e)
        change %= e
calc()