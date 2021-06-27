'''
棋牌类 OOD

- 棋类
- 类棋类
    - Tic tac toe
    - 扫雷
- 扑克牌

'''

'''
棋牌类特点
- 玩家
- 规则
- 胜负
- 积分

棋牌类状态
- 一局棋牌，分为那些状态

- initialization(摆盘，洗牌)
- Play
- Win/Lose check + Tie
'''

'''
Tic tac toe

- 玩家：是否需要专门的Player 类？
    - 关键点在于 player 之间有什么区别，比如要不要积分什么的

- 规则 
- 确认胜负规则

先是init，
然后 play, move啊， 啥的
最后 win/lose check
'''

class TicTacToe:
    Borad board
    char currentPlayer

    def makeMove(): ## 调用 board的make move
    
    def changePlayer(): ## makeMove 调用这个函数

class board:
    [][]board
    def initBoard():
        pass

    def move(row, col, currentPlayer):
        pass
    
    def checkwin():
    
    def isBoardFull():


'''
chess game
'''

class Cheese():
    player1
    player2
    player currentPlayer
    Board board
    steps int

    def joinGame():
    
    def initBoard():
    
    def move(board, row, col):
    
    def checkwin():
    
    def __changePlayer():
    
    def __isCurrentPlayerWin():
    
    def gameDraw():


class piece: ### 棋子
    Role role
    Color ChildProcessError

class Color(Enum):
    red 
    black

class Role(Enum):
    gereral
    horse
    ...

class Board:
    board

class player:
    point int
    def updatePoints():