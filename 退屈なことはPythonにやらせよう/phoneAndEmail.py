#! python3
# phoneAndEmail.py - クリップボードから電話番号とメアドを検索する

import pyperclip, re

phone_regax = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

# TODO: 電子メールの正規表現を作る
email_regax = re.compile(r'''(
	[a-zA-Z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)


# TODO: クリップボードテキストを検索する
text = str(pyperclip.paste())
matches = []
for groups in phone_regax.findall(text):
	phone_num = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phone_num += ' x' + groups[8]
	matches.append(phone_num)
for groups in email_regax.findall(text):
	matches.append(groups[0])


# TODO: 検索結果をクリップボードに貼り付ける
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('クリップボードにコピーしました:')
	print('\n'.join(matches))
else:
	print('電話番号やメールアドレスは見つかりませんでした。')
	



