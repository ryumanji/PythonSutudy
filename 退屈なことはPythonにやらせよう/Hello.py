#このプログラムは挨拶を表示して名前と年齢を尋ねる

print('Hello World')
print('What is your name?')
my_name = input()
print('It is good to meet you, '+ my_name) #
print('The length of your name is:')# 名前の長さを表示
print(len(my_name))
print('What is your age?')#年齢を尋ねる
my_age = input()
print('you will be ' + str(int(my_age) + 1) + ' in a year.')
