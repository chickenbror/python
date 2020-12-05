


"""
create a class that, given a list of text files, will at each iteration return
the first line of the text only if the file is not suppose to be ignored (see example files below)

example:

let's assume we have the following files and that the first line of each file is the name of the file

files = ["file1.txt", "file2.txt", "ingore_this_file1.txt", "file3.txt", "ingore_this_file2.txt", "file4.txt"]


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

class DataGenerator():
    
    def __init__(self, filelist):
        self.filelist = filelist
        self.firstlines = []
        self.update(filelist) # Update 'firstlines' list
        self.idx=-1
        
    # Iterate over 'firstlines'
    def __iter__(self):
        return self
    def __next__(self):
        if self.idx > len(self.firstlines):
            raise StopIteration
        self.idx+= 1
        return self.firstlines[self.idx]
        
        
    def update(self, filelist):
        for file in self.filelist:
            # open > read > close each file
            with open(file, 'r') as f:
                first_line = f.readline()
                if 'ignore' not in first_line:
                    self.firstlines.append(first_line)
        

import os
def newfolder(files, destination):
    """
    Make a folder of txt files. Each file has the same filename and content.
    """
    newfolder = destination
    try:
        os.mkdir(newfolder)
    except OSError:
        print ("Failed to create %s " % newfolder)
    else:
        print ("Created %s " % newfolder)
       
    for file in files:
        with open(newfolder+'/'+file, 'w+') as f:
            f.write(file)
            
            
files = ["file1.txt", "file2.txt", "ignore_this_file1.txt", "file3.txt", "ignore_this_file2.txt", "file4.txt"]
# newfolder(files, 'dataGen_test')
txtfiles = ['dataGen_test/'+file for file in files]
       

my_generator = DataGenerator(txtfiles)
print(my_generator)
for data in my_generator:
    print(data)
    if "3" in data:
        break
print(next(my_generator))