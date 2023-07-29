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
letter_counts = {letter: word.count(letter) for letter in word}
