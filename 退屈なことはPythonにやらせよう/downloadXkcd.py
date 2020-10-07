#! python3
# downloadXkcd.py - XKCDコミックを一つずつダウンロードする

import requests, os, bs4

url = 'http://xkcd.com' # 開始URL
os.makedirs('xkcd', exist_ok=True)   #./xkcdに保存する

while not url.endswith('#'):
    # TODO: ページをダウンロードする
    print('ページをダウンロード中{}...'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    # TODO: コミック画像のURLを見つける
    comic_elem = soup.select('#comic img')
    if comic_elem ==[]:
        print('コミック画像が見つかりませんでした。')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')
        # 画像をダウンロードする
        print('画像をダウンロード中{}...'.format(comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

    # TODO: 画像を./xkcdに保存する
    image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    # TODO: PrevボタンのURLを取得する
    prev_link = soup.select('a[rel="prev"]')[0]
    url ='http://xkcd.com' + prev_link.get('href')


print('完了')
