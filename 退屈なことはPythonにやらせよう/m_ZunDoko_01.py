import random

words = ["ズン","ドコ"]
s_array = []
while s_array != ["ズン","ズン","ズン","ズン","ドコ"]:
    r = random.choice(words)
    s_array.append(r)
    print(r)
    if len(s_array) == 6:
        del s_array[:1]
        continue
print("ズンズンズンズンドコ")
print("KI･YO･SHI")
