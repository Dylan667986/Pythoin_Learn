#製作一個稱為Thing 而且沒有內容的類別 並將它印出 接著用這個類別建立一個稱為example的物件 也將它印出

class Thing:
    pass
print(Thing)

example = Thing()
print(example)

#製作一個稱為Thing2的新類別，並將'abc'值指派給一個稱為letters的類別屬性印出letters

class Thing2:
    letters = abc 
print(Thing2.letters)

#在製作一個類別 鄉當然 將它命名為Thing3這次將'xyz'值指派給一個稱為letters的實例(物件)屬性印出letters

class Thing3:
    def __init__(self,letters):
        self.letters = 'xyz'
        
print(Thing3.letters)

somthing = Thing3()
print(somthing.letters)
'xyz'

#製作一個稱為Element的類別 加入實例屬性name, symbol, number 用值 'Hydrigen' 'H' 與 1
# 建立一個這種類別的物件稱為 hydrogen

class Element :
    def __init__(self, name, symbol, number):
        self.name =name
        self.symbol =symbol
        self.number =number 
hydrogen = Element()

#用這些鍵與值製作一個字典 'name', 'Hydrogen', 'symbol':'H','number':1
#再用Element 類別與這個字典建立一個名為hydrogen的物件

el_dict = {'name' : 'Hydrogen', 'symbol':'H', 'number':1}
hydrogen =Element(el_dict['name'],el_dict['symbol'],el_dict['number'])

hydrogen.name
#'Hydrogen'
#但是你也可以用字典直接初始化物鍵 因為它的鍵名稱符合__init__的引數
hydrogen = Element(**el_dict)
hydrogen.name
'Hydrogen'

#為Element類別定義一個名為dump()的方法 讓他印出物件鼠性的值(name , symbol, number) 
# 用這個新定義建立hydrogen物件 並使用dump()來印出它的屬性
class Element :
    def __init__(self, name, symbol, number):
        self.name =name
        self.symbol =symbol
        self.number =number
    def dump(self):
        print('name =%s ,symbol = %s, number =%s ' % (self.name,self.symbol,self.number))
hydrogen = Element(**el_dict)
hydrogen.dump()
#name = hydrogen, symbol=H , number =1

#呼叫print(hydrogen) 在Element的定義中 將方法dump的名稱改為__str__ 
#建立一個新的hydrogen物件 並再次呼叫print(hydrogen)
print(hydrogen)
#<__main__.Element object at 0x1006f5310>
class Element :
    def __init__(self, name, symbol, number):
        self.name =name
        self.symbol =symbol
        self.number =number
    def __str__(self):
        print('name =%s ,symbol = %s, number =%s ' % (self.name,self.symbol,self.number))
hydrogen = Element(**el_dict)
print(hydrogen)
#name=hydrogen, symbol =H ,number =1
#__str__ 是python的魔術方法 來取得它的字串表示法

#修改Element 讓name symbol 與 number 變成私用的為每一個屬性定義getter proerty 並回傳它得值
class Element :
    def __init__(self, name, symbol, number):
        self.name =name
        self.symbol =symbol
        self.number =number
    @property
    def name(self):
        return self.__name
    def symbol(self):
        return self.__symbol
    def number(self):
        return self.__number
    
hydrogen = Element('hydrogen','H',1)
hydrogen.name
hydrogen.symbol
hydrogen.number

#定義三個類別 : Bear Rabbit Octothorpe 在每個類別中定義一個方法
#eats() 讓它回傳'berries'(Bear) 'clover'(Rabbit)與 'campers'(Octothorpe)
#用各個類別建立一個物件並印出它吃什麼東西
class Bear :
    def eats(self):
        return 'berries'
