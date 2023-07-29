'''
 #tuple 不可變 使用逗號與()建立

empty = ()
one_marx = ('Groucho')
type(one_marx)
#<class 'str'>

maxrx_tuple = 'Groucho' , 'Chico', 'Harpo'
type(maxrx_tuple)
#<class 'tuple'>

#python safe 
maxrx_tuple_1 = ('Groucho' , 'Chico', 'Harpo')
type(('Groucho' , 'Chico', 'Harpo'))
#<class 'tuple'>

a, b, c = maxrx_tuple_1

a 
#'Groucho'
b
#'Chico'
c
#'Harpo'

marx_list = ['Groucho' , 'Chico', 'Harpo']
tuple(marx_list)
#('Groucho' , 'Chico', 'Harpo')

#+
('Groucho') + ('Chico', 'Harpo')
#('Groucho' , 'Chico', 'Harpo')
#*
('yada',) * 3
('yada','yada','yada')

#compare tuple
a =(7,2)
b =(7,2,9)
a == b
#False
a <= b
#True
a < b 
#True


#for in tuple
words = ('fresh', 'out', 'of', 'ideas')
for word in words :
    print(word)

#edit tuple 
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop')
t1 + t2 
#('Fee', 'Fie', 'Foe', 'Flop')

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop')
t1 += t2
t1
##('Fee', 'Fie', 'Foe', 'Flop')

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop')
id(t1)   #id() 觀察變數狀況
#4365405712
t1 += t2 
id(t1)
#4364770744
}
'''
#List 用 [] 建立 可變
empty_list = []
leap_years = [2000, 2000, 2008] #值不必是唯一的

another_empty_list = list()
another_empty_list
#[]

list('cat')
# ['c', 'a','t']

a_tuple =('ready', 'fire', 'aim')
list(a_tuple)
['ready', 'fire', 'aim']

talk_like_a_pirate_day = '9/19/2019'
talk_like_a_pirate_day.split('/')
#['9','19','2019']

#offset 取得項目
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0]
#'Groucho'
marxes[1]
#'Chico'
marxes[2]
#'Harpo'

#slice
marxes[0:2] #間格2 
['Groucho', 'Chico']
marxes[::2]
['Groucho', 'Harpo']
marxes[::-2] #間格2 從左邊取出
['Harpo', 'Groucho']
marxes[::-1]
['Harpo', 'Chico', 'Groucho']

marxes.reverse #反轉
#這些都部會改變list 本身

#slice 可以指定無效的索引 不會產生例外
#會回傳最接近的有效損引 或回傳空
marxes[4:]
#[]
marxes[-6:]
['Groucho', 'Chico', 'Harpo']
marxes[-6:-2]
['Groucho']
marxes[-6:-4]
[]

#append()
marxes.append('Zeppo')
['Groucho', 'Chico', 'Harpo','Zeppo']

#insert and offset to appned
marxes.insert(2, 'Gummo')
['Groucho', 'Chico', 'Gummo', 'Harpo']

marxes.insert(100, 'Zeppo')
['Groucho', 'Chico', 'Gummo', 'Harpo', 'Zeppo']

marxes * 3 

#extend() or +
others = ['Gummo', 'Karl']
marxes.extend(others)
['Groucho', 'Chico', 'Harpo','Gummo', 'Karl']
marxes += others
['Groucho', 'Chico', 'Harpo','Gummo', 'Karl']

#!!!! 如果使用 append()
marxes.append(others)
['Groucho', 'Chico', 'Harpo',['Gummo', 'Karl']]

# 用 offset 來改變一個項目
marxes[2] = 'Wanda'
['Groucho', 'Chico', 'Wanda']

#用slice
numbers = [1,2,3,4]
numbers[1:3] = [8,9]
numbers
[1, 8, 9, 4]

numbers = [1,2,3,4]
numbers[1:3] = [7,8,9]
numbers
[1, 7, 8, 9, 4]

numbers = [1,2,3,4]
numbers[1:3] = []
numbers
[1, 4]

numbers = [1,2,3,4]
numbers[1:3] = 'wat?'
numbers
[1, 'w', 'a', 't', '?', 4]

#del A(offset)
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
marxes[-1]
'Karl'
del marxes[-1]
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']

#remove()
marxes.remove('Groucho')

#pop(offset) 
marxes.pop()  #-1
marxes.pop(1) #
#'Chico'

#clear()  
marxes.clear() #刪除所有

#index(offset)  find 
marxes.index('Chico')
1

#in 檢查
'Groucho' in marxes
True
'Bob' in marxes
False

#count
marxes.count('Chico') #確認此list 裡面的文字重複幾次
1

#join()  list convert to string
', '.join(marxes)
'Groucho, Chico, Harpo'

#sort() or sorted() 排列項目
#sort( 就地排序)
#sorted() 回傳排序後的串列複本
sorted_marxes = sorted(marxes)
['Chico', 'Groucho', 'Harpo'] #按照字母大小排序 並且不會改變原本的list
 
marxes.sort()  #會改變原本的list

#反向排序
marxes.sort(reverse=True)

len(marxes)
3

# = value
a= [1,2,3]
b = a
[1,2,3]
a[0] = 'surprise'
a
['surprise, 2, 3']

#copy(), list()  或 slice 來複製

b = a.copy()
c = list(a)
d = a[:]

#deepcopy()
a = [1,2,[8, 9]]
b = a.copy()
c= list(a)
d = a[:]

a[2][1] = 10
#[1,2,[8,10]]
import copy
a = [1,2,[8,9]]
b = copy.deepcopy(a)

#compare 
a =[7,2]
b =[7,2,9]
a == b
False

#for in 
cheeses =['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)

#zip() 迭代
days = ['Monday', 'Tuesday', 'Wednesday']
fruits =['banana', 'orange', 'peach']
drinks = ['coffe', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day , fruit, drink, dessert in zip(days , fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
#Monday : drink coffe - eat banana - enjoy tiramisu

#用生成式來建立串列
1
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
2
for number in range(1,6):
    number_list.append(number)
3
number_list = list(range(1, 6))

#4
number_list = [number for number in range(1, 6)]
number_list = [number-1 for number in range(1, 6)]
0,1,2,3,4,5
number_list = [number for number in range(1, 6) if number %2 == 1]
1,3,5

#5
a_list =[]
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)
#6
rows = range(1,4)
cols =range(1,3)
for row in rows:
    for col in cols:
        print(row,col)
'''
1 1
1 2
2 1
2 2
'''
#7
rows = range(1,4)
cols = range(1,3)
cells = [(row, col), for row in rows for col in cols]
    print(cells)
(1,1)
(1,2)
..

for row, col in cell:
    print(row,col)
1,1
1,2
2,1
....

#list 的 list

#tuple vs list
#tuple 佔用空間較少
#你不可以破壞tuple項目
#可以將tuple當成字典鍵來用
#具名tuple 可以當成簡單的物件跌代品
#不打算協系介紹tuple 日常編成中 串列語字典比較常用
#python沒有 tuple 生成式