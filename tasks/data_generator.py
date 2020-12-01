


"""
create a class that, given a list of text files, will at each iteration return
the first line of the text only if the file is not suppose to be ignored (see example files below)

example:

lets assume we have the following files and that the first line of each file is the name of the file
``
files = ["file1.txt", "file2.txt", "ingore_this_file1.txt", "file3.txt", "ingore_this_file1.txt", "file4.txt"]


following code should run:

>> my_generator =  DataGenerator(files)
>> for data in my_generator:
..      print(data)
..      if "3" in data:
..          break
>>"file1.txt"
>>"file2.txt"
>>"file3.txt"
>> next(my_generator)
>>"file4.txt"

"""

class DataGenerator:
    pass