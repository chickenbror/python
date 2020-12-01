

"""
fill in the functions so that they catch the appropriate errors and return "caught".

example:
>> test_list = []
>> catch_all_expeptions(test_list[10])
>> "caught"

"""


def catch_all_expeptions():
    pass

####### It works if I write them globally but I don't know how to put them in a function :(
test_list = []
try:
    test_list[10]
except:
    print('caught')


def catch_index_error():
    pass
try:
    test_list[10]
except IndexError as err:
    print('caught', err)

def catch_value_error():
    pass
try:
    int('haha')
except ValueError as err:
    print('caught', err)



 
