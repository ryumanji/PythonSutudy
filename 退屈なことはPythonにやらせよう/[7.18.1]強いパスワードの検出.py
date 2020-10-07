#! python3
# 演習プロジェクト - 強いパスワードの検出

import re

password = input('パスワードを入力してください：')

def Check_Password(password):
    password_regax = re.compile(r'''(
    #a-zA-Z0-9{8,}
    ^[a-z+$]
    #^\w+$
    ^[0-9+$]
    )''', re.VERBOSE)
    s = password_regax.search(password)
    print(s)
    
    if s == None :
        print('このパスワードは強力ではありません。')
        
    else:
        print('このパスワードは強力です。')

Check_Password(password)

