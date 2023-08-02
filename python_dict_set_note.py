#dict 用 {} 建立
empty = {}

#傳統
acme_customer = {'first': 'Wile','middle': 'E', 'last': 'Coyote'}

#dict 作法
acme_customer = dict(first= 'Wile',middle = 'E', last = 'Coyote')

#list to dict
lol = [['a','b']
       ,['c','d']
       ,['e','f']] 
result_dict = dict(lol)
#{'a': 'b', 'c': 'd', 'e': 'f'}
print(result_dict)

# [key] 或 get() 取得一個項目
pythons ={
   'Graham' : 'Chapman',
   'John' : 'Cleese',
   'Eric' : 'Idle',
    'Terry' : 'Gilliam',
    'Michael' : 'Palin',
    'Terry' :'Jones' ,
}

pythons['John'] 
'Cleese'

'Groucho' in pythons
#False

pythons.get('Eric','no key')
#True 'Idle' ,False = no key
pythons.get('ABC')
#None

list(pythons.keys()) #列出所有的key 
list(pythons.values()) #列出所有的value
list(pythons.items()) #列出所有key/value
len(pythons) #列出長度 6


#用{**a, **b} 來結合字典
first = {'a':'agony', 'b':'bliss'}
second = {'b' : 'bagels', 'c' : 'candy'}
{**first,**second}
#{'a':'agony', 'b' : 'bagels', 'c' : 'candy'}
third = {'d' : 'donus'}
{**first,**second,**third}
#{'a':'agony', 'b' : 'bagels', 'c' : 'candy','d' : 'donus'}

#update() 結合字典
others = {'Marx' :'Grouch','Howard':'Moe'}
pythons.update(others)

#del pop clear  刪除項目
del pythons['John']
pythons.pop('John')
len(pythons)
pythons.clear() #刪除所有的項目

#用in來檢查
'Eirc' in pythons
True

# = 來賦值
signals = {'green':'go',
            'yellow':'go faster',
            'red':'smile for the camera'}

signals['blue'] = 'confuse everyone'

# 用copy 來複製 如原本的dict改變也會跟著改變
original_signals = signals.copy()
signals['blue'] ='confuse everyone'

#用 deepcopy()來複製 與copy不同的是 deepcopy是獨立的 

#comapre dict
a ={1:1, 2:2, 3:3}
b ={3:3, 1:1, 2:2}
a==b 
#  ==  !=
#True
#其他運算子沒有效果 <= < 

#for in  key
accusation = {'root' : 'ballroom', 'weapon' : 'lead pipe', 'person':'Col.Mustard'}
for card in accusation.keys(): #或 for car in :
    print(card)
for card in accusation.value(): #或 for car in :
    print(card)
#room
#weapon
#person

#用tuple來回船鍵與值
for item in accusation.items():
    print(item)
#('room', 'ballroom')
#..

#字典生成式
word ='letters'
#1 letter_counts = {letter: word.count(letter) for letter in word}
letter_counts = {letter: word.count(letter) for letter in set(word)}  #python寫法
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num ** 2 for num in numbers}
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


#set 就像是沒有值 只有鍵的字典 必須是獨一無二

empty_set = set()
even_numbers = {0,2,4,6,8}
odd_numbers = {1,3,5,7,9}

#set 轉換

set( 'letters' )
#{'l','r','s','t','e'}  #丟棄重複的字母:

#用list / tuple 製作集合
set(['Dasher', 'Dancer','Prancer','Mason-Dixon'])
#{'Dasher', 'Dancer','Prancer','Mason-Dixon'}
set(('Ummagumma','Echoes','Atom Heart Mother')) 
#{'Ummagumma','Echoes','Atom Heart Mother'}

#當你用字典丟給set()只會留下鍵

len(even_numbers)
#5

#add()
#remove()
#for in ()
#in

#交集
drinks = {
    'marttini' : {'vodka','vermouth'},
    'black russian' : {'vodka','kahlua'},
    'white russian' : {'cream','kahkya','vodka'},
    'manhattan' : {'rye','vermouth','bitters'},
    'screwdriver' : {'orange juice', 'vodka'}
    }
for name, contents in drinks.item(): 
    if contents & {'vermouth','orange juice'}:
        print(name)
        #screwdriver
        #martini
        #manhattan

for name, contents in drinks.item(): 
    if 'vodka' in contents and not contents & {'vermouth','orange juice'}:
        print(name)
        #screwdriver
        #black russian

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1,2}
b = {2,3}

#a & b  或者 a.intersection(b)
#{2}
bruss & wruss 
a.intersection(b)
#{'kahlua', 'vodka'}

#聯集
a | b
a.union(b)
{1,2,3}

#差集 屬於第一個集合 但不屬於第二個集合
a - b
a.difference(b)
{1}

bruss - wruss
#set()
wruss - bruss
#{cream}
#互斥或

a^b
a.symmetric_difference(b)
{1,3}

#子集合  <= issubset() 查看集合式不是另外一個集合的子集合 (第一個集合的所有成員都屬於第二個集合)
a <= b
a.issubset(b)
#False
#所有集合都是他自己的子集合
a <= a
a.issubset(a)
#True

'''
    'black russian' : {'vodka','kahlua'},
    'white russian' : {'cream','kahkya','vodka'},
'''
#a = {1,2}
#b = {2,3}
#真子集(proper subset) 如果第二個集合除了擁有第一個集合的所有成員之外也有其他的成員 
a < b
a < a
#False

bruss < wruss
#True



#超集合 是子集合的相反 (第二個集合的所有成員都是第一個集合的成員)
a >= b 
a.issuperset(b)
#False

wruss >= bruss 
#True

#任何集合都是他自己的超集合
a >= a
a.issubset(a)
#True


# > 真.超集合 (第一個集合除了擁有第二個的所有成員之外 還有其他成員)

a > b
#False 
wruss > bruss 
#True

#集合生成式
#{expression for expression in iterable if condition}
a_set = {number for number in range(1,6) if number % 3 == 1}
{1,4}

#用frozenset() 建立不可變集合
fs = frozenset([3,2,1])
#({1,2,3})
fs.add(4) #失敗



####總結####
list = []
(,) tuple
{} dict or set 

marx_list = ['Groucho','Chico', 'Harpo']
marx_tuple = ('Groucho','Chico', 'Harpo')
marx_dict = {'Groucho': '1','Chico': '2', 'Harpo':'3'}
marx_set = {'Groucho','Chico', 'Harpo'}
marx_list[2]
marx_tuple[2]
marx_dict['Harpo']

'Harpo' in marx_list
'Harpo' in marx_tuple
'Harpo' in marx_dict
'Harpo' in marx_set


#製作更大型的資料結構
marxes = ['Groucho','Chico','Harpo']
pythons = ['Chapman','Cleese','Gilliam','Jones','Palin']
stooges = ['Moe','Curly','Larry']

tuple_of_lists = marxes , pythons, stooges
#( ['Groucho','Chico','Harpo'],['Chapman','Cleese','Gilliam','Jones','Palin'],['Moe','Curly','Larry'])
list_of_lists =[marxes , pythons, stooges]
#[ ['Groucho','Chico','Harpo'],['Chapman','Cleese','Gilliam','Jones','Palin'],['Moe','Curly','Larry']]

dict_of_lists ={'Marxes':marxes,'Pythons': pythons, 'Stooges': stooges}
{
    'Marxes' : ['Groucho','Chico','Harpo'],
    'Pythons' : ['Chapman','Cleese','Gilliam','Jones','Palin'],
    'Stooges' : ['Moe','Curly','Larry']
}

#dict 的鍵不可變 所以 list  dict set 都不能當字典的鍵 但 tuple可以 因為tuple不可變

#例如 GPS 經度 緯度 高度
houses = {
    (44,79, -93.14, 285): 'My House',
    (38.89, -77.03, 13): 'The White House'
}

