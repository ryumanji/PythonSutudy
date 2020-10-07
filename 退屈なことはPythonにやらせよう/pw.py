#! python3
# pw.py - パスワード管理プログラム（脆弱性あり）

PASSWORDS = {'email': 'email-pass',
             'blog': 'blog-pass',
             'luggage': '12345',
             'ckn3211ryubon@gmail.com': 'パスワード'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方: python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.argv[1] # 最初のコマンドライン引数がアカウント名

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました')
else:
    print(account + 'というアカウント名はありません')
