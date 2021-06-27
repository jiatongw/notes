'''
实物类OOD
vending machine
coffee maker
Kindle

解题：
 - 考虑对于事=实物的输入输出
 - design pattern 的运用
'''

'''
Design a vending machine
input: payment
output: item

payment -> vendingMachine -> item
关键字:
vending machine: 
payment: coine, paper money, credit card
item: what item sell? what if sold out?
'''

class VendingMachine:
    list<coins> coins
    list<item> items
    map<teminfo, list of items> items
    map<string, itemInfo> itemIdentifiers
    ItemInfo currentSelection
    list of currentCoins

    def selectItem(selection):
    
    def insertCoin():

    def executeTransaction():

    def refund():

    def refillItems(list  of items):

    

class ItemInfo:
    float price
    def getPrice():


class Coin:

class Item:

'''
design a coffee maker
'''
class CoffeeMaker(object):
     def __init__(self, coffeePack, kindOfCoffee):
        self.coffee = None
        if kindOfCoffee == "DarkRoast":
            self.coffee = DarkRoast()
        elif kindOfCoffee == "Expresso":
            self.coffee = Expresso()
        for _ in range(coffeePack.needMilk):
            self.coffee = WithMilk(self.coffee)
        for _ in range(coffeePack.needSugar):
            self.coffee = WithSugar(self.coffee)

class CoffeePack(object):
    def __init__(self, needMilk, needSugar):
        self.needMilk = needMilk
        self.needSugar = needSugar
        
class Coffee(metaclass=abc.ABCMeta):
    def __init__(self, cost=1.99):
        self.cost = cost
        
    @abc.abstractmethod
    def get_cost(self):
        pass
    
    @abc.abstractmethod
    def getIngredients(self):
        pass

class DarkRoast(Coffee):
    def __init__(self):
        self.cost = 1.99
    
    def get_cost(self):
        return self.cost
    
    def getIngredients(self):
        return "DarkRoast"

class Expresso(Coffee):
    def __init__(self):
        self.cost = 2.99
    
    def get_cost(self):
        return self.cost
    
    def getIngredients(self):
        return "Expresso"

class Decorator(Coffee, metaclass=abc.ABCMeta):
    def __init__(self, coffee):
        self.coffee = coffee
    
    @abc.abstractmethod
    def get_cost(self):
        return self.cost

class WithMilk(Decorator):
    def get_cost(self):
        return self.coffee.get_cost() + 0.2
    
    def getIngredients(self):
        return self.coffee.getIngredients() + ", Milk"
    
class WithSugar(Decorator):
    def get_cost(self):
        return self.coffee.get_cost() + 0.5
    
    def getIngredients(self):
        return self.coffee.getIngredients() + ", Sugar"
    
p1 = CoffeePack(2, 2)
d1 = CoffeeMaker(p1, "Expresso")
print(d1.coffee.getIngredients())
print(d1.coffee.get_cost())