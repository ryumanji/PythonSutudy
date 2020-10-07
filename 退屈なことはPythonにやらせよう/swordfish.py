while True:
    print('あなたは誰？')
    name = input()
    if name != 'Joe':
        continue
    print('こんにちはJoe。パスワードは何？(魚の名前)')
    password = input()
    if password == 'swordfish':
        break
print('認証しました。')
    
