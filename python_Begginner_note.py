#python 3.11.3

#Basic DATA Type 
bool : True ; False 
int  1
float 1.1  
complex (3j,5+9j),
str 'abc' , "def" 
list, ['first','second','third']            #Variable 
tuple, (2,4,8)
bytes b'ab\xff'
bytearray, (....)                           #Variable
set, set([1,2,3,4])                         #Variable
frozenset, frozenset(['Elsa', 'Otta'])
dict {'key' : 'value' , ..}                 #Variable 

# + = * / // %  **

'''
HEX，英文全稱 Hexadecimal，表示十六進制。 0x 0X   0x16 = 10 
 
DEC，英文全稱 Decimal，表示十進制。10

OCT，英文全稱 Octal，表示八進制。0o12 0O12

BIN，英文全稱 Binary，表示二進制。0b1010 0B

'''
int(True) = 1
int(False) = 0 
bool(1) = True
bool(0) = False  
int(98.6) = 98 
int(1.0e4) = 10000
bool(1.0) = True
bool(0.1) = False
int ('99') = 99
int('10', 2) = 10
int('10', 8) = 8
int('10', 16) = 16
True + 2 = 3
False + 5.0 = 5.0 

disaster = True 
if disaster : 
    print("Woe")
else : 
    print("wheel")

#/ != / < / <= / > />=
disaster = True 
if disaster == True : 
    print("Woe")
else : 
    print("wheel")

#What is false
bool False
null None
0
0.0
''
[]
()
{}
set()

tr1 = 1 + \
      2 + \
      3 + \
      4 + \
      5


vowels = 'aeiou'
letter = 'o'
letter in vowels
#True 
if letter in vowels : 
    print(letter,'is a vowel')

#String 
print('Give', "us", '''some''', """space""", '\n')
str(9.8)
#'9.8'
A = 'A man \nA plan\n, A canal:\nPanama.'
#tab
A = 'A man \tA plan\t, A canal:\tPanama.'
# + 
A = 'A man + A plan +, A canal:+Panama.'
# * 
A = 'A man' * 4 + '\n'
# A man
# A man 
# A man 
# A man

#sring []
letters = 'abcdefghijklmnopqrstuvwxyz'
letters[3] 
'd'

name = 'Hennt'
name.replace('H','P')
'Pennt'
or
'P' + name[1:]
'Pennt'

#slice (string)
[:]
[start : ]
[: end]
[start : end]
[start : end : step]


letters[-3:] #= 'xyz'
letters[::7] #= 'ahov'  
letters[4:20:3] #= 'ehknqt' #start 4 end 20 step 3
len(letters) #= 26 

empty = ""
len(empty) 
#= 0 

#split()
letters_split ('a,b,c,d,e,f,g')
letters.split(',')
#['a'.'b','c','d','e','f','g']

letters.split() #換行符號 空格 與 tab
#join
letters.join()
crypto_list = ['a', 'b', 'c', 'd', 'e']
crypto_list_string = ', ' .join(crypto_list)
print('show ',crypto_list_string)
#a, b, c, d, e

#replace
temp = letters.replace('dcba','abcds') #只換找到的第一個
temp = letters.replace('dcba','abcds', 100) # 100 個

#strip 剔除
world = "   earth   "
world.strip()   #' ', '\t' ,'\n'
#earth
world.strip(' ') #指定
#earth
world.lstrip()   #left
#'earth    '
world.rstrip()   #right
#'    earth'

world.strip(' thrae')
#''

#Find & pick
letters[:13]
#abcdefghijkl
len(letters)
#26

#if letters = 'a b c d...'
letters.startswith('a') #if hard = a
letters.endswith('z') #if end = z 

#
word = 'd'
letters.find(word)  #第一個出現 最左邊
letters.index(word)
#a b c d...    = 7
#if no found the word = -1 

letters.rfind(word)   #最右邊 也就是最後一個
letters.rindex(word)  

letters.count(word)   #重複幾次
letters.isalnum #使否只有字母與數字  

setup = 'a duck goes into a bar ...'
setup.strip('.')
#a duck goes into a bar

setup.capitalize #首字大寫
#A duck goes into a bar ...
setup.title()  #所有單字第一個字母
#A Duck Goes Into A Bar ...
setup.upper()  #全部大寫
setup.lower()  #全部小寫
setup.swapcase() #小<->大

#排版 對齊
setup.center(30) #center 在30個空格內置中的字串
setup.ljust(30) #left
setup.rjust(30) #right

thing = 'woodchunk'
#%s %d %x %o %f %e %g
# %s ,%12S %+12s %-12s %.3S %12.3%s %-12.3s

'%s' % thing 
'woodchunk'
'   woodchunk'
'   woodchunk'
'woodchunk   '
'woo'
'   woo'
'woo   '

'format'
'{}'.format(thing)
place = 'lake'
'The {} is in the {}.'.format(thing,place)


#Format - 3.6 f-strings
head = 123
hand = 456
print(f'hello {head}')
f'{head =}, {hand =}'
#'head =123, hand=456'


#while and for 
count = 1
while count <= 5:  #while True
    print(count)
    count += 1
    break
    continue


# for & in 
for letters in word :
    if letter == 'x':
        print('y')
        break
    print(letters)
else:
    print("No 'x' in there ")

#range 
for x in range(0,3):  #類似 slice (start, end, step)
list( range(0,3))
#[0, 1, 2]
list( range(2, -1 ,-1))
#[2,1,0]
list(range(0, 11,2))
#[0, 2, 4, 6, 8, 10]
