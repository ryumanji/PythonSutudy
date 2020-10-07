import random


print('1から20までの数を当ててください。')
count_list = []
number = random.randint(1,20)
while True:
    print('数を入力してください')
    value = int(input())
    count_list.append(value)
    if value > number:
        print('大きいです')
    elif value < number:
        print('小さいです')
    elif value == number:
        break
    
print('あたり！' + str(len(count_list) + 1) + '回で当たりました！')
