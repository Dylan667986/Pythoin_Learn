

#函式 管理小程式

def nothing():
    print('123')

nothing()
#123

##呼叫
def agree():
    return True 
agree()

if agree():
    print('Splendid!')
else:
    print('That was unexpected.')

#Splendid

##
#引述與參數
def echo(anything):
    return anything + ' ' + anything
echo('Rumplestiltskin')
#Rumplestiltskin #Rumplestiltskin


#None 不等於 False 雖然他可以被當作布林值的False
thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")
#It's no thing
if thing is None:
    print("It's nothing")
else:
    print("It's something")
#It's nothing

#利用None來區分 [缺漏值 missing value] 與 [空值 empty value] 
# 0 ,0.0 , '', [], (,), {}, set() 這些都是False 而不是None

####################
#位置性引數(position argument)
def menu(wine, entree , dessert):
    return {'wine': wine , 'entree' :entree , 'dessert': dessert}
menu('chardonnay', 'chicken', 'cake')
#缺點 你得記住每個位置代表的意思

#關鍵字引數 為了避免位置引數造成混亂
menu(entree='beef', dessert='bagel',wine ='bordeaux')
{'wine': 'bordeaux','entree': 'beef' ,'dessert':'bordeaux'}
#如果你同時使用位置引數以及關鍵字引數  位置引數放在最前面
####################

#####指定預設參數值####
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree':entree, 'dessert', dessert}

menu('chardonnay','chicken')
#'wine': chardonnay, 'entree':chicken, 'dessert', pudding

#當你提供引數他就不在是預設值
menu('dunkelfelder', 'duck', 'doughnut')
#'wine': dunkelfelder, 'entree':duck, 'dessert', doughnut

#預設參數跌
def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy(a)
['a']
buggy(b)  #預期是 ['b']
['a','b']
#修改

def works(arg):
    result = []   #每次都創鍵一個空集合就會與預期結果一致
    result.append(arg)
    return result 
#又或者

def nonbuggy(arg, result=None):
    if result is None:
        result = []
        result.append(arg)
        print(result)
nonbuggy(a)
['a']
nonbuggy(b)
['b']


#用 * 來炸開 / 收集位置引數 position Argument
# C / C++ * 代表指標 , Python 沒有指標
def print_args(*args):
    print('Positional tuple :' ,args)
print_args()
#Positional tuple : ()

print_args(3,2,1, 'wait', 'uh...')
#Positional tuple : (3,2,1, 'wait', 'uh...')
#很適合用來編寫print()等引數數量不一定的函式 

#如果已的函式也需要位置引數 你要把他們放前面
def print_more(requiresd1, required2, *args):
    print('Need this one:', requiresd1)
    print('Need this one too :', required2)
    print('All the rest:', args)
print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
'''
Need this one: cap
Need this one too : gloves
All the rest:('scarf', 'monocle', 'mustache wax')

使用*時 不一定要將tuple引數稱為*args 部過他在pytohn裡面是一種習慣用法 雖然他技術上應該稱為 *params
'''
print_args(2, 5, 7, 'x')
#(2, 5, 7, 'x')

args = (2, 5, 7, 'x')
print_args(args)
#((2, 5, 7, 'x'),)
print_args(*args)
#(2, 5, 7, 'x')

'''
你只能在函式呼叫式或定義式裡面使用 *
在函式裡面 *args 會將所有tuple args 炸成以鬥後分開的位置參數
在函式外面 *args 會將所以位置參數收集成單一 args tuple 你也可以使用 *params 和 params 這種名稱 但大家習慣在引數外面與參數裡面使用 *args

'''


#用 ** 來炸開 / Keyword Argument收集關鍵字引數
# ** 將關鍵字引數組成字典 引數名是鍵 值是相應的字典值
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs()
#'Keyword arguments:': {}
print_kwargs(wine ='melot', entree='mutton', dessert='macaroon')
#Keyword arguments: {'dessert': 'macaroon', 'wine': 'merlot', 'entree': 'mutton'}

'''
kwargs 是字典的參數
引數的順序是:
必需的位置引數
選用的位置引數(*args)
選用的關鍵字引數(**kwargs)
與args依樣 你不一定要將罐鍵字引數稱為kwargs 他只是常見的稱呼
'''

#純關鍵字引數 *代表接下來的start 與end 必須用具名引數來提供
def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)

data = ['a','b','c','d','e','f']
print_data(data)
'''
a
b
c
d
e
f
'''
print_data(data,start =4)
#e
#f
print_data(data,end =2)
#a
#b

#可變與不可變引數
#list 可變 整數字串不可變
outside = ['one', 'fine', 'day']
def mangle(arg):
    arg[1] = 'terrible'

mangle(outside)
['one', 'terrible', 'day']
#這是不好的作法 要麻 你要說明引數可能會被修改 要麻 你要return新值


#Docstrings  #docstring是在源代碼中指定的字符串文字，用於記錄特定的代碼段
#你可以在函式內文的開頭加入一個字串來為函式定義加上說明 這就是docstring:
def echo(anything):
    'echo returns its input argument'
    return anything

#python help() 可以印出函式的 docstring
help(echo)
'''
Help on function echo in module _main_ :

echo(anything)
    echo returns its input argument
'''
#如果你只想查看原始的docstring
print(echo._doc_)
#echo returns its input argument

#函式式一級公民 python 的魔咒 一切都是物件 包括 數字、字串、tuple、串列、字店-函式
#你可以指配給變數 當成引數傳給其他函式 讓函釋回傳 其他語言很難或辦不到
def answer():
    print(42)
def run_something(func):
    func()
#42
run_something(answer)
type(run_something)
#<class 'function'>
#在python中 小括號代表呼叫該函式 Python 會將沒有括號的函示當成熱和其他物件一般看待 如同 python的任何其他東西 他是物件

def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)
#add_args(5,9)


def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

run_with_positional_args(sum_args,1,2,3,4) #tuple (1,2,3,4)
#10

#內部函式
def outer(a,b):
    def inner(c,d):
        return c+d
    return inner(a,b)

outer(4,7)
#11
#如果你要在一個函式裡面進行多次執行複雜動作 可以使用內部函式來避免編寫重複的迴圈或程式碼

def knights(saying):
    def inner(quote):
        return "We are the knights who say : '%s'" % quote
    return inner(saying)
knights('Ni!')
#"We are the knights who say : 'Ni!'"

#Closure 內部函式可以當成Closure使用 可以更改和記得在函式外面建立的變數的值

def knights2(saying):
    def inner2():
        return "We are the knights who say : '%s'" % saying
    return inner2
#inner2()可以直接使用外面的saying參數，不需要用引數來取得
#knights2()會回傳inner2函式名稱 而不是呼叫他
#inner2()函式知道被傳入的saying的值 並且記得 return inner2這一行會回傳這個客製化的inner2函數的"複"本但部會呼叫他 它是一個closure
#一種動態建立的並且記得它來自哪裡的函式

a = knights('Duck')
b = knights('Hasenpfeffer')
type(a)
type(b)
#<class 'function'> 也是 closure
a , b
#<function knights2.<locals>.inner2 at 0x123456>

a()
#We are the knights who say : 'Duck'
b()
#We are the knights who say : 'Hasenpfeffer'



#匿名的函式 : lambda
#取代一些小函式

def edit_story(words, func):
    for word in words :
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']


edit_story(stairs, lambda word: word.capitalize()+'!')
#Thud!
#Meow!
#Thud!
#Hiss!

#lambda 難懂 定義許多小型函式 並且記住它們的名稱時用來取代它們 #圖形化使用著介面裡面使用lamb來定義回呼函式









#產生器 generator (yield)
'''
你可以用它來跌代可能很大的序列，且不需要在記憶體中一次建立或儲存整個序列

range() 會回傳一個串列 所以有記憶體容量的限制
當你的跌代產生器 它都會記住上次被呼叫時的位置 並回傳下一個值 所以它與一般的函式不同
 一般的函式部會記住之前的呼叫 而且永遠都會用同一個狀態從它的第一行開始執行
'''
#跌代器
sum(range(1, 101))
#5050

#如果你想建立龐大的序列 你可以編寫產生器函式 但是它是用yield來回傳值 而不是return
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number  #回傳 number
        number += step 

ranger = my_range(1,5)
#ranger <generator object my_range>

for x in ranger :
    print(x)
'''
1
2
3
4
'''
#產生器只執行一次 串列 集合 字串 與 字典 都會被放在記憶體裡面
#但是產生器可以動態產生它的值 並且透過跌代器一次送出一個值 它部會記得它們 所以你無法重新啟動或備份產生器

for try_again in ranger:
    print(try_again)



#裝飾器 decorator 有時候你想要修改既有的函示 但不更改它的原始碼 有一種常見的情況是加入一個除厝陳旭式來查看引數
'''
接收一個函式並回傳另一個函式
*args **kwargs
內部函式
當成引數的函式
'''
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional argumentts', args)
        print('Keyword argument:', kwargs)
                
        result = func(*args, **kwargs)
        print('result', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

add_ints(3, 5)

cooler_add_inits = document_it(add_ints) #手動指派裝飾器
cooler_add_inits(3, 5)

#也可以使用@deciratir_name
@document_it
def addinits_(a, b):
    return a + b 

addinits_(3, 5)

#同一個函式可以使用多個裝飾器
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result *result
    return new_function 
@document_it
@square_it
def add_inits(a, b):
    return a+b 

add_inits(3, 5)

#改變順序
@square_it
@document_it
def add_inits(a, b):
    return a+b 

add_inits(3, 5)
#結果也會相同

#名稱空間與作用域 全域變數/區域變數
'''
一個名稱可以代表不同的東西 取決它在哪裡被使用
不能再函式裡更改全域變數 也不要去改任何已經宣告好的變數
'''

#在名稱鐘內使用 _ 與 __
'''
python 保留在名稱的開頭與結尾使用兩個底線的寫法
例如函式的名稱被存放在系統變數 funciton._name_ 它的文件字串式function._doc_:
'''
def amazing():
    ''' This is amazing function
    Want to see it again '''
    print('This function is named:', amazing.__name__)
    print('And its docstring is :', amazing.__doc__)
amazing()
#This function is named: amazing
#And its docstring is :''' This is amazing function
#                           Want to see it again '''
#就像是之前的globals 主程式被設為特殊名稱__main__ 
if __name__ == '__main__':
    #如果主程式(函式)就是在main的話
    print('yes')


#遞迴 FP程式開發者必學 也避免去使用 for 或者 while 

def dive():
    return dive()

#遞迴在你處理不平整 uneven的資料很方便
def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item
#yield的核心目的：為了節省記憶體 生成器(generator) yield和return一樣會回傳值，不過yield會記住上次執行的位置

def flatten(lol):
    for item in lol :
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item 
#「yield from 表達式」讓我們把生成器物件的工作「委任」給另一個生成器物件。簡單的說，它讓我們可以把「另一個生成器生成的值」當成「自己要生成的值」
# 
#如果區塊內沒有 yield 表達式，稱為「普通函式（Normal Function）」
#如果區塊內有 yield 表達式，稱為「生成器函式（Generator Function）

#非同步函式 差一點 非同步可以放棄控制權
#python 3.5 
#async /await 附錄C

#函式例外
#try except 處理意外
#可以使用預設例外 也可以自己定義
class UppercaseException(Exception):
    pass
words = ['eenie', 'meenie', 'miny', 'MO']
for word in words :
    if word.isupper():
        raise UppercaseException(word)
#直接使用pass 讓他的父類別決定例外出現要印出什麼
#MO

#可以讀出例外本身
try:
    raise OopsException('panic')
except OopsException as exc :
    print(exc)
    
    