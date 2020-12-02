

"""
fill in the functions so that they catch the appropriate errors and return "caught".

example:
>> test_list = []
>> catch_all_exceptions(test_list[10])
>> "caught"

"""

#######
def catch_all_exceptions(func):
    try:
        func()
    except: #Catches any error
        print('caught')


def catch_index_error(func):
    try:
        func()
    except IndexError as err:
        print('caught:', err)

def catch_value_error(func):
    try:
        func()
    except ValueError as err:
        print('caught:', err)
#========================================
def test():
    l = [1,2,3]
    print(l[1]) #in range
    print(l[10]) #index out of range

    
catch_all_exceptions(test)
catch_index_error(test)



def value_err():
    print(int(1.2345))
    print(int('hello'))

catch_value_error(value_err)
 
