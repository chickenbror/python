
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
        key_to_delete = None
        for existing_key in self.keys():
            if existing_key[0] <= key[0] <= existing_key[1] \
                or existing_key[0] <= key[1] <= existing_key[1]:
                key_to_delete = existing_key
        
        if key_to_delete:
            self.pop(key_to_delete)
        super().__setitem__(key, item)
        

my_range_dict = RangeDict({(1,10):1, (30,34): 2, (5,10):5})
my_range_dict[(25,29)] = 3
my_range_dict[(5,15)] = 3