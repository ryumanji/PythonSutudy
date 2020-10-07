# マルバツゲーム
class tictactoe():
    def __init__(self):
        self.the_board = {'top-L': ' ','top-M': ' ','top-R': ' ',
                    'mid-L': ' ','mid-M': ' ','mid-R': ' ',
                    'low-L': ' ','low-M': ' ','low-R': ' '}

    def print_board(self, board):
        print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
        print('-+-+-')
        print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
        print('-+-+-')
        print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

    def play_game(self):
        turn = 'X'
        for i in range(9):
            self.print_board(self.the_board)
            print('ターン: ' + str(i))
            print(turn + 'の番です。どこに打つ？')
            move = input()
            self.the_board[move] = turn
            if turn =='X':
                turn = 'O'
            else:
                turn = 'X'