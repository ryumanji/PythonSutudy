import sys

args = sys.argv

int1 = args[1]
int2 = args[2]
symbol = args[3]

class calc():
        def __init__(self, int1,int2,symbol):
                try:
                        self.num1 = int(int1)
                        self.num2 = int(int2)
                except ValueError:
                        print("[ERROR]: 計算する値は数値を入力してください。")
                        exit()
        def calculate(int1,int2,symbol):
                if symbol == "+":
                        print(plus())
                elif symbol == "-":
                        minus()
                elif symbol == "*":
                        cross()
                elif symbol == "/":
                        division()
                else:
                        print("第3引数には + - * / のいずれかの記号を入力してください。")
                        
        def plus(self):
                self.num1 + self.num2
                
        def minus(self):
                self.num1 - self.num2

        def cross(self):
                self.num1 * self.num2
        
        def division(self):
                try:
                        self.num1 / self.num2
                except ZeroDivisionError:
                        print("[ERROR]: 割り算を行う際に0徐算が発生しました。第2引数を0以外の数値にしてください。")
                        exit()
   

        

        



        




