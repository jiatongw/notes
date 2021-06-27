'''
管理类 OOD
比如 parking lot
gym
restaurant
library
supermarket
hotel

特点 每个题目后面 都可以接上 “管理员”
设计一个模拟/代替管理员日常工作的系统 
'''

'''
 clarify:
 key point: vehicle 

 考虑这个管理系统中，input 和 output是什么

 比如，电梯Linput: request output: 选择一台elevator

 use case -> 从管理员角度考虑 
 - Reserve
 - serve
 - checkout

 class
 在设计类图的时候，经常可以使用收据的形式，来保管信息
 例子：图书馆

 User
加一个 receipt 类， 记载哪个用户借了哪本书
 Book
'''

'''
Design a parking lot

parking lot管理什么？ vehicle / parking spot 

vehicle -> parking lot -> parking spot

parking lot有没有层？露天的？
vehicle 什么类型？
parking spot 有没有残趴？

针对本题：
- parking lot: 考虑多层的parking lot, 没有错层
- vechicle: 考虑三种大小的 车
- spot: 不考虑残疾人停车位/充电车位

停车场有哪些规则？
1. 如何停车？
2. 收费？


cases:
 - parking 
 - get available count
 - park vehicle
 - clear spot
 - calculate price

 management 类 常见 use case:
 - reservation
 - serve: park vehicle
 - check out: clear spot + calculat price
'''

class ParkingLot:
    levels = [] ## list of Levels
    hourlyRate = 6

    def getAvailableCount():
        pass
    def findSpotsForVehicle(self, vehicle):
        pass

    def parkVehicle(self, v): ## 调用 findSpotsForVehicle
        ###some code
        findSpotsForVehicle(v)

        ## return 一个 ticket class, 映射车和spot的关系
    def clearSpot(self, ticket):


'''
use case: get availabe count for each level
'''
class level:
    __spot = [] ## list of Spot
    availableCount = 0
    def getAvailableCount():

class spot:
    isavailable = True
    def isAvaible():
        pass
    def takSpot():
    
    def leaveSpot():
'''
use case:park vehicle
- parking lot checks the size of vehicle
- parking lot find an available spot for this vehicle
- vehicle takes the spot
'''
class vehicle:
    size = 0

    def getSize(self):
        return vehicle.size

class car(vehicle):
    size = 20

'''
use case: clear spot
'''
class ticket:
    def __init__(self, vehicle, spots, starttime): ## vehicle 是车类，spot是 list of spot
        self.veichle = vehicle
        self.spots = spots
        self.time = starttime


class handleException:
    pass