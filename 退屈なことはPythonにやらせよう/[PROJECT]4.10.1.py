#カンマ付け

spam = ['apples','bananas','tofu','cats']


def func_sort(list):
    list.insert(-1,"and")
    print("'",end='')
    for i in range(len(spam)-1):
        print(spam[i],end=', ')
    print(spam[-1]+ "'")

    
func_sort(spam)


