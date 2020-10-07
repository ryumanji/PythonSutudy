import sys

while True:
    print('終了するにはexitと入力して下さい。')
    responce = input()
    if responce == 'exit':
        sys.exit()
    print(responce + 'と入力されました。')
