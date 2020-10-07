import random

messages = [
    '確かにそうだ',
    'はい',
    'なんとも。もういちどやってみて',
    '後でもういちどきいてみて',
    '集中してもう一度聞いてみて',
    'あたしの答えはノーです',
    '見通しはそれほど良くない',
    'とても疑わしい']

print(messages[random.randint(0,len(messages) -1)])
    
