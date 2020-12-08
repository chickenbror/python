
""""

implemet a child-class of dict called RangeDict that takes pairs of ints; (int, int) which
signifies a range. eg. (1,10), (30,34).
Given an int will return the value of the range the int is inside

so if out dict contain the keys (1,10), (30,34), and we run:

>> my_range_dict[7]
>> (1,10)

furthermore;

when you try to add a range that overlaps with an existing range, for example
trying to add (5,11) when we have (1,10), overwrite the overlapping span.

>> my_range_dict
>> {(1,10):1, (30,34): 2}
>> my_range_dict[(5,11)] = 3
>> my_range_dict
>> {(30,34): 2, (5,11):3}

"""

class RangeDict(dict):
  
    def __getitem__(self, arg):
        for key in self.keys():
            if key[0] <= arg <= key[1]:
                return key
    
    def __setitem__(self, key, item):
        keys_to_delete = []
        for existing_key in self.keys():
            if existing_key[0] <= key[0] <= existing_key[1] \
                or existing_key[0] <= key[1] <= existing_key[1]:
                keys_to_delete.append(existing_key)
        
        if keys_to_delete != []:
            for k in keys_to_delete:
                self.pop(k)
        super().__setitem__(key, item)
        

my_range_dict = RangeDict({(1,10):1, (30,34): 2, (5,10):5, (100,101):4})
my_range_dict[(9,32)] = 3
# my_range_dict[(5,15)] = 3
print(my_range_dict)