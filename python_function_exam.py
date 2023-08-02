#定義一個稱為good()的函是 用它回傳串列['Harry','Ron','Hermione']

def good():
    return ['Harry','Ron','Hermione']
#定義一個稱為get_odds()的產生器函式 用它回傳range(10)的奇數 使用for迴圈來找到並印出第三個回傳值

def get_odds():
    for number in range(1, 10, 2):
        yield number

count = 1

for i in get_odds():
    if count == 3 :
        print(i)
        break
    count += 1

#定義一個稱為test的裝飾器用它在一個函式被呼叫時印出'start'在那個函式結束時印出'end'

def test(func):
    def new_func(*args,**kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

@test
def greeting():
    print("Greetigns, Earthing")
greeting()
#start
#Greetings, Eearthling
#end

#定義一個稱為OopsException的例外 並印出 'Caught an oops'
class OopsException :
    pass
#raise OopsException

try:
    raise OopsException
except:
    print('Caught an oops')