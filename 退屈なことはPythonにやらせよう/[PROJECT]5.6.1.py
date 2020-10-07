#ファンタジーゲームの持ち物リスト

stuff = {'ロープ': 6,'金貨': 42,'手裏剣': 1,'矢': 12}

def display_inventory(inventory):
    print('持ち物リスト')
    for k ,v in stuff.items():
        print(str(v) +' '+ str(k))
        all_items = 0
        all_items = all_items + int(v)
    print('アイテム総数 ' + str(all_items))

display_inventory(stuff)
