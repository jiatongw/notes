'''
design restaurant

input: party
output: table

功能:
- 预约
- dine-in/ dine-out

思考模式：
1. 
party 进入餐馆 -> host指引倒空桌 -> assign waiter -> 点菜 -> 
chief 拿到order , cook by order -> serve order -> checkout

2. 
 - 客人进入餐馆，返回一个table
 - 点菜 -> 返回一桌菜
 - checkout -> 餐馆清空table
'''

class restaurant:
    tables = [] ## list of tables
    menu = [] ## list of meal
    dict() ## map table and orders
    def findTable():##return table

    def takeOrder(order):

    def checkout(order):

class party:

class table:
    isavailable = True
    def isavailable():

    def markUnavailable():
    
    def markAvailable():

class order:
    meals = [] ## list of meals
    table = None

    def getPrice():

class meal:
    price = 0

    def getPrice():

'''
预定类题目 解题思路
 use case:
 - search
 - select
 - cancel

 search criteria - search() -> list result -> select() -> receipt
'''