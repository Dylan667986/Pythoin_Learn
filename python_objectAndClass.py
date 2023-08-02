#Simple object

class Cat():
    pass
class Cat:
    pass

a_cat = Cat()

#屬性
'''
class Cat:
    pass
a_cat = Cat
another_cat = Cat

a_cat.age = 3
a_cat.name = "Mr Fuzzybuttons"
a_cat.namesis = another_cat

a_cat.namesis.name = 'Mr. Bigglesworth'

 #methon 
 #init 如果你想要在建立期指派物件屬性

class Cat:
    def __init__(self):
        pass
'''
        
class Cat():
    def __init__(self, name):
        self.name = name

furball = Cat('Grumpy')
'''
這一行做了這些事
查看 CAT 類別的定義
在記憶體中實例化(建立)一個新物件
呼叫該物鍵的_init_()方法 將這個新建立的物件傳給self 將另一個引數(Grumpy) 傳給 name
在物件中儲存name的值
回傳新物件
將物件指派給變數 furball
'''

print('Our latest addition:', furball.name)

#繼承
#父類別繼承
class Car():
    def exclaim(self):
        print("I'm a Car!")
class Yugo(Car):

issubclass(Yugo,Car)
#True
give_me_a_car = Car()
give_me_a_yago = Yugo()
#Yugo is a Car
give_me_a_car.exclaim()
#I'm a Car !
give_me_a_yago.exclaim()  #Yugo可以執行 父類別 car的東西
#I'm a Car !

#使用過多的繼承 會讓程式難以管理 事實上 很多人建議使用 聚合 或組合

#複寫方法 替換或複寫

class Car():
    def exclaim(self):
        print("I'm a CAR!")
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Muchh like a Car , but more Yugo-ish")
#製作物件
give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
#I'm a CAR!
give_me_a_yugo.exclaim()
#I'm a Yugo! Muchh like a Car , but more Yugo-ish

#添加方式
# 子類別也可以添加父類別沒有的方法
class Car():
    def exclaim(self):
        print("I'm a CAR!")
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Muchh like a Car , but more Yugo-ish")
    def need_a_pugh(self):
        print("A little help here")
#此時Yugo 可以做一些 Car無法做到的事情

#用super()來取得父類別的幫助
#如果我們想要呼叫父類別
class Person():
    def __init__(self, name): 
        self.name = name
#子類別增加 email
class EmailPerson(Person):
    def __init__(self, name,email):
        super().__init__(name)
        self.email = email 


#多重繼承
class Mule(Donkey, Horse):
    pass
#mixin

#自 self 衛
#python 使用self引數來尋找正確的物件的屬性與方法


#屬性存取
 #直接存取
 class Duck:
    def __init__(self, input_name):
        self.name = input_name
fowl = Duck('Daffy')
fowl.name
#如果有人想要偷改 也容易就改掉
#增加隱私 getter setter 存入 property
class Duck():
    def __init__(self, input_name):
        self.hidden_name =input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)

#第二種做法事加入一些裝飾器
class Duck():
    def __init__(self, input_name):
        self.hidden_name =input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

fowl = Duck('Howard')
fowl.name
#inside the getter
#Howard
fowl.name = 'Donald'
#inside the setter
fowl.name
#inside the getter
#Donald

#用 property 回傳算出來得值
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
c =Circle(5)
c.radius
#5
c.diameter
#10
#更改屬性
c.radius = 7
c.diameter
#14
#如果你沒有指定 setter property 你就不能在外面設定它 (唯讀)
c.diameter = 20
#excpet
#使用 property 還有一個比直接存取鼠性更好的地方: 當你更改屬性定義時 你只要修改類別定義是裡面的程式就可以了 不需要修改所有的呼叫方

#修飾名稱來保護隱私
#將hidden_name 改為 __name python不允許在類別定義事的外面看到屬性有一種命名規範: 在開頭使用雙底線
class Duck():
    def __init__(self,input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name
fowl = Duck('Howard')
fowl.name
#inside the getter 
'Howard'
fowl.name = 'Donald'
#inside the setter
fowl.name
#inside the getter
'Donald'
#看起來沒問題 你無法存取__name屬性
#但
fowl._Duck__name
'Donald'
#雖然名稱裝飾不是婉美的保護機制 但它可以防止意外或故意直接存取屬性

#類別與物件屬性
class Fruit:
    color = 'red'
blueberry = Fruit()
Fruit.color
'red'
blueberry.color 
'red'
#如果你改變子物件的屬性的值 它不會影響類別屬性
blueberry.color = 'blue'
blueberry.color
'blue'
Fruit.color
'red'
#如果你稍後改變類別屬性它部會影響既有的子物件
Fruit.color = 'orange'
Fruit.color
'orange'
blueberry.color
'blue'
#但它會影響新的
new_fruit = Fruit()
new_fruit.color
'Orange'

#方法型態 *有些方法是類別本身的一部分 有些是用那個類別建立的物件的一部分 有些不屬於兩者
'''
如果它的前面沒有識別器它是實例方法 它的第一個引數應該是self 用來飲用個別的物件本身
如果它的前面有@classmethod 裝飾器 它是類別方法 它的第一個引數應該是cls 引用類別本身
如果它的前面有@staticmethd裝飾器 它是靜態方法 它的第一個引數不是物件或類別
'''
#實例方法
    #當類別定義裡面的方法第一個引數事self時 它就是"實例方法"
#類別方法
    #類別方法會影響到整個類別 @classmethod
    class A():
        count = 0
        def __init__(self):
            A.count += 1
        def exclaim(self):
            print("I'm an A!")
        @classmethod
        def  kids(cls):
            print("A has", cls.count, "little objects")
    
    easy_a = A()
    breezy_a = A()
    wheezy_a = A()
    A.kids()
    #A has 3 little objects.

#靜態方法
    #在類別定義第三個方法既不影響類別 也不影響物件 它只是為了不四處漂流而待在那裏 它是靜態方法 沒有開頭的self 或 cls
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This coyoteWeapon has been brought to you by Acme')
CoyoteWeapon.commercial()
#不需要建立CoyoteWeapon類別的物鍵就可以使用這個方法了

#鴨子定型 
#鴨子定型是一種動態類型的概念，它強調在判斷物件的適用性時，關注其行為而不是類型。
# 如果一個物件走起路來像鴨子、游泳像鴨子、嘎嘎叫像鴨子，那麼它就可以被視為是一隻鴨子。
# 種概念常用於語言如 Python，其中不同的物件可以實現相同的方法或特性，並被視為同一類型，即使它們的類型不同。
class Quote():
    def __init__(self, person, words):
        self.person  = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'
class QuestionQuote(Quote):
    def say(self):
        return self.words + '?'
class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'
    
hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'say:', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up,doc")
print(hunted1.who(), 'says', hunter.say())

hunted2 =ExclamationQuote('Daffy Duck', "It's rabbit reason")
print(hunted2.who(), 'says:' , hunted2.says())

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'
brook = BabblingBrook()

def who_says(obj):
    print(obj.who(),'says:', obj.says())

who_says(hunter)
#Elmer Fudd says I'm hunting wabbits
who_says(hunted1)
#Bugs Bunny says What's up, doc ?
who_says(hunted2)
#Daffy Duck says It's rabbit season!
who_says(brook)
#Brook says Babble

#魔術方法
#__init__就是一種魔術方法 這些方法開投跟結尾都有爽底線(__) 因為程式員不可能在變數名稱中修改它
#修飾名稱來保護隱私 使用 dunder 來命名可以協助修飾類別屬性名稱以及方法了
class word():
    def __init__(self, text):
        self.text = text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

first = word('ha')
second =word('HA')
third = word('eh')
first.equals(second)
#True
first.equals(third)
#False

#
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2): #魔術方法
        return self.text.lower() == word2.text.lower()
first = Word('ha')
second =Word('HA')
third = Word('eh')
first == second 
#True
first == third
#False
#只要使用python測試相等宇否的特殊方法名稱 __eq__() 就可做到了
#進行比較的魔術方法
'''
__eq__(self,other)   self == other
__ne__(self, other)   self != other
__lt__
__gt__
__le__
__ge__
'''
#進行算數的魔術方法
'''
__add__(self,other)
__sub__(self,other)
__mul__(self,other)
__floordiv__(self,other)  self // other
__truediv__(self,other)   self / other
__mod__(self,other)       self % other
__pow__(self,other)       self ** other
'''
#other 魔術方法
'''
__str__   str(self)
__repr__  repr(self)
__len__   len(self)
'''

first = Word('ha')
#獲得預設自串版本 <__main__.Word object at 0x1006ba3d0>

#將 __str__() 與__repr__()方法加入Word類別讓它更完美
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("' + self.text +'")'
    
first =Word('ha')
first        #使用__repr__
Word("ha")
print(first) #使用__str__
#參考文件探索更多特殊方法

#聚合與組合
#當你希望子類別的多數動作都與它的父類別相同時 繼承是一種很好的技術
#但有時使用組合(composition) 或聚合(aggregation)比較合理
#鴨子 is a 鳥(繼承) 但 has a 尾巴(組合) 尾巴不是一種鴨子 但它是鴨子的一部分 
class Bill():
    def __init__(self, description):
        self.description = description
class Tail():
    def __init__(self, length):
        self.length = length
class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a' ,self.tail.length, 'tail')

a_tail = Tail('long')
a_bill = Bill('wide ornage')
duck = Duck(a_bill, a_tail)
duck.about()
#This duck has a wide orange bill and a long tail


#何時該使用物件或其他東西
'''
當你需要使用需多個別的實例 們有相似的行為(方法) 但內部的狀態(屬性)不同時 物件是最實用得選擇
類別可以繼承 模組不行

如果你只需要使用一個某種東西 模組可能是最好的選擇 無論你在程式眾參考某個python模組幾次 它都只會載入一個複本

如果你有許多變數 他們裡面有許多值 這些變數可以當成引數傳給多個函式 將他們定義成類別可能比較好

使用最簡單的問題解決方式 字典 串列 與 tuple 都比模組更簡單 更小 且更快 而模組通常比類別簡單
'''

#具名 tuple
#tuple的子類別 讓你可以用.name與 [offset]來存取值
#*名稱
#*欄位名稱字串 以空格分開
from collections import namedtuple
Duck = namedtuple('Duck','bill tail')
duck = Duck('wide orange', long)
#Duck(bill='wide orange', tail ='long')
duck.bill
'wdie orange'
duck.tail
'long'
#你也可以用字典來製作具名tuple:
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 =Duck(**parts)
duck2
#Duck(bill='wide orange', tail = 'long')
#**parts 它是kwargs 它會取出parts 字典的鍵與值並將它當成引數傳給Duck() 它的效果相當於:
duck2 = Duck(bill = 'wide orange', tail = 'long')
#具名tuple是不可變的 但你可替換一或多個欄位 並回傳另一個命名tuple:
duck3 =duck2._replace(tail= 'magnificent', bill='crushing')
#Duck(bill='crushing', tail ='magnificent')

#也可以將Duck定義為字典
duck_dict = {'bill':'wide orange','tail':'long'}
#{'tail':'long','bill':'wide orange'}

#可以將欄位加入字典
duck_dict['color'] = 'green'
#{'color':'green','tail':'long','bill':'wide orange'}

#但不能加入具名tuple
duck.color = 'green'
'''
tuple的優點
它的外觀與行為像個不可變物件
它的物件更節省空間與時間
你可以用具點標記法取代字典風格的終括號來存取屬性
你可以將它當成字典鍵來使用
'''

#資料類別
#恨多人建立物件的主因是為了儲存資料 python3.7 資料類別 dataclass
class TeenyClass():
    def __init__(self, name):
        self.name = name
teeny =TeenyClass('itsy')
teeny.name
'itsy'

#用資料類別做同一件事看起來有點不同
from dataclasses import dataclass
@dataclass
class TeenyDataClass :
    name : str
teeny =TeenDataClass('bitsy')
teeny.name
'bitsy'

#建立資料類別物件 你要按照引數在類別內的定義順序提供它們 或是使用具名引數 以任何順序提供
from dataclasses import dataclass
@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0

snowman = AnimalClass('yeti','Himalayas',46)
duck = AnimalClass(habitat='lake', name='duck')
snowman
#AnimalClass(name='yeti', habitat='Himalayas', teeth=46) 
duck
#AnimalClass(name='duck', habitat='lake', teeth=0) 
duck.habitat
'lake'
snowman.teeth
'46'

#Attrs
'''
定義 __init__()
將它引數指派給self
以及建立諸如__str__()等dunder
具名tuple
資料類別
是標準程式庫提供的替代品

或者使用第三方程式庫 attrs 優點: 打字量較少 可以驗證資料 
'''