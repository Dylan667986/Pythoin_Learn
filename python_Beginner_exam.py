
#chapter 1
# install python  3.11 
# launch python 
# start simple progrmming

#chapter 2  data, type, value, variable, name / page 21
def chapter2():
    #2.1 將整數直99指派給變數prince，並列出它
    prince = 99 
    return print(prince)
    #值 5 的型態 int
    #值2.0的型態 float
    #運算式 5+2.0 的型態 float
    
#chapter 3 number / page 52
def chapter3(): 
    #3.1 a hour = ? second 
    minute_per_hour = 60   # 1h = 60m
    second_per_minute = 60 # 1m = 60s
    #return minute_per_hour *  second_per_minute
    #3.2 將結果指派給 second_per_hour
    second_per_hour = minute_per_hour *  second_per_minute
    #3.3 second per day
    hour_per_day = 24 
    second_per_day = hour_per_day * second_per_hour
    print(f'{second_per_day / second_per_hour}')  #24.0
    print(f'{second_per_day // second_per_hour}') #24

#chapter 4  if
def chapter4_1():
   
    #4.1
    #選擇一個介於1和10之間的數字 並將它指派給變數secret。 接著選擇另一個介於1和10之間的數字，將它指派給變數guess
    #接下來編寫條件測試式(IF、else 與 elif)，當guess 小於secret時印出字串'too low'當它大於secret時印出'too high'
    #當它等於secret時印出'just right'
    import random  
    #使用random來隨機生成1~10
    secret = random.randrange(1, 10)
    guess = random.randrange(1, 10)
    if secret < guess :
        return print(f'secret : {secret} < guess : {guess}, result : to low')
    elif secret > guess :
        return print(f'secret : {secret} < guess : {guess}, result : to high')
    else: 
        return print(f'secret : {secret} < guess : {guess}, result : just right')
def chapter4_2():
    #4.2 將True 或 False 指派給變數small 與green 寫出 if/else陳述式來印出下列哪種東西符合這些選擇: cherry pea watermelonn pumpkin
    small = input('That size is samll ? (\'True\' or \'False\')')
    green = input('That color is green ? (\'True\' or \'False\')')

    if small and green:
        print("pea")
    elif small and not green:
        print("cherry")
    elif not small and green:
        print("watermelon")
    else:
        print("pumpkin")

#chapter 5 text string
def chapter5():
    #5.1將m開頭的單字改成大寫
    song = """When an eel grabs your arm,
    ... And it causes great harm,
    ... That's - a Moray!"""
    words =song.split()

    for i in range(len(words)):
        if words[i].startswith('m') or words[i].startswith('M'):
            words[i] = words[i].capitalize()
    
    update_song = ' '.join(words)
    print(update_song)

#while and for 
def chapter6():
    #使用for loop print list [3, 2, 1, 0]
    list = [3, 2, 1, 0]
    for i in list:
        print(f'{i}', end=' ')
'''
    my_list = [3, 2, 1, 0]
    index = 0
    while index < len(my_list):
        print(f'{my_list[index]}', end='')
        index += 1
'''

def main():

    chapter_list = ['1', '2', '3', '4.1', '4.2', '5', '6']
    chapter_number = input("chioce chapter ")
    if chapter_number == chapter_list[0] :
        print('start python')
    elif chapter_number == chapter_list[1] :
        chapter2() 
    elif chapter_number == chapter_list[2] :
        chapter3()
    elif chapter_number == chapter_list[3] :
        chapter4_1()
    elif chapter_number == chapter_list[4] :
        chapter4_2()
    elif chapter_number == chapter_list[5] :
        chapter5()
    elif chapter_number == chapter_list[6] :
        chapter6()
    else:
        print(f'please input {chapter_list} ')




if  __name__ == '__main__':
    main()