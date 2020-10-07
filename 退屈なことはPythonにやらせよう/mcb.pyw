#! python3
# mcb.pyw - クリップボードのテキストを保存・復元
# Usage:
# py.exe mcb.pyw save <keyword>
# py.exe mcb.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
# py.exe mcb.pyw lilst - 全キーワードをクリップボードにコピー

import shelve, pyperclip, sys

mcb_shelve = shelve.open('mcb')

# TODO: クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # TODO: キーワード一覧と内容の読み込み
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        


mcb_shelf.close()


