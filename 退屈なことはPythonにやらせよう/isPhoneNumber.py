def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[1].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = '明日415-555-1011に電話してください。オフィスは415-555-9999です。'
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print('電話番号が見つかりました: '+chunk)

print('完了')
