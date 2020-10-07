from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('container')
    print('そのクラス名を持つ要素<{}>をみつけた！'.format(elem.tag_name))
except:
    print('そのクラス名を持つ要素は見つからない')
