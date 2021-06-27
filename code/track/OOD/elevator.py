'''
ask:
1. 客梯还是一般的电梯  - 这里倾向一般的电梯
2. 是否有多个电梯口 - 当按键按下时，有多少电梯相应
        - 倾向于 每层只有一处能搭乘电梯，所有电梯都能相应
3. 如何判断电梯超重
        - passenger class 包含重量
        - 有个sensor自动感应
4。 当按下按钮时，那一台电梯响应？
        - 同方向 》 静止 》 反方向
        - 当运行时不能按下反方向楼层

request --> elevatorSystem --> elevator  ---> elevatorButton
'''


class elevatorSystem:
    __elevator = elevator.elevator()

    def handleRequest(ExternalRequest):



'''
- take external rquest
- take internal request
- open gate
- close gate
- check weight
'''
class elevator:
    buttons = [] ## list of type elevatorButton
    stopsforUp = [] ## list of int
    stopsforDown = [] ## list of int
    status = "idle" ### up, down, idle
    currentLevel = 0
    weightLimit = 1500
    
    def handleExternalRequest(ExternalRequest):

    def handleInternalRequest(internalRequest): 

    def isRequestValid(internalRequest): -> bool

    def getCurrentWeight(): -> float

    def openGate():
    
    def closeGate():
    
    
'''
press button
'''
class elevatorButton:
    button = ['1', '2', '3']

class invalidExternalRequestException:
    def isValid()

class ExternalRequest:
    __direction = "" ## up, down
    __level = 0

class internalRequest:
    __level = 0