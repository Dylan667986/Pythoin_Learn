
#tuple and list
#chapter 7

def chapter7():
    years_list = [1997, 1998, 1999, 2000, 2001]
    my_third_birthday = years_list[4]
    my_mostOldest_year = years_list[-1]

    thing = ['mozzarella', 'cinderella', 'salmonella']
    
    for i in range(len(thing)):
        if thing[i] == 'mozzarella':
            thing[i] = thing[i].upper()
        elif thing[i] == 'cinderella':
            thing[i] = thing[i].capitalize()
        elif thing[i] == 'salmonella':
            thing.remove(thing[i])
    print(thing)

def chapter7_():
    surprise = ['Groucho', 'Chico', 'Harpo']
    surprise[-1] = surprise[-1].lower
    surprise = surprise[::-1]
    surprise[-1] = surprise[-1].capitalize()
    print(surprise)

def chapter7_0():
    even = [number for number in range(1, 11) if number %2 == 0]
    print(even)


def main():
    chapter7_0()


if  __name__ == '__main__':
    main()

