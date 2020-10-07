#! python
# print_table.py - リストの中身を整理して表示する

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table(data):
    values_0 = ''
    values_1 = ''
    values_2 = ''
    values_3 = ''
    max_length_list = [[],[],[],[]]
    
    for value in range(len(data)):       
        
        for i in range(len(data)+1):
                    
            #print(data[value][i])
            
            length = len(data[value][i]) # 要素の文字数を計算
            if i == 0 :
                max_length_list[i].append(length)
                values_0 += data[value][i]
            elif i == 1 :
                max_length_list[i].append(length)
                values_1 += data[value][i]
            elif i == 2 :
                max_length_list[i].append(length)
                values_2 += data[value][i]
            elif i == 3 :
                max_length_list[i].append(length)
                values_3 += data[value][i]
            max_length_list[i].sort(reverse = True)
            
    
            while len(max_length_list[i]) != 1:
                
                del max_length_list[i][1]
                
    print(max_length_list)
    print(values_0)
    print(values_1)
    print(values_2)
    print(values_3)
    
        
print_table(table_data)

