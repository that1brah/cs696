"""
Classes

Custom organization of information and functionality
thats all we are doing, organizing information and functions
all of these things can be done without classes, the only difference is organization and information sharing
"""


### Why?

## An example case

# Get all sequences from a FASTA file into a list
# Don't you wish you could just do this?
seqs = FastaReader('test.fasta').get_seqs()

# or this:
# generate a dictionary from a FASTA file
fasta_dict = FastaReader('test.fasta').to_dict()

# what if you're working with many FASTA files in a folder and want them all in 1 dictionary?
fasta_dict = FastaReader('../fasta_files/').to_dict()





## Reusability
# Up until now, we have assumed that our code will only be run once, or at most a couple times.
# This is obviously not always going to be true. Some code will be reused, reread, and rewritten frequently.
# If you find yourself accessing the same information/data repeatedly, or you find yourself rewriting the same
#  few lines of code repeatedly, its probably a good idea to write a class.

class FastaReader:
    pass

# done! it was that easy

fasta_dict = FastaReader('../fasta_files/').to_dict()  #  Notice how the red underline is gone. This class now exists!

# however, if we run this line, we get an error:  "TypeError: FastaReader() takes no arguments"
# this happens because we try to pass ('../fasta_files/') to FastaReader, without defining an __init__ function.



### Anatomy of a Python Class

## What are the mandatory and important defs?

class FastaReader:  # we named it - good start!
    """
    This is a docstring, you can access it with FastaReader.__doc__
    You should place all of your documentation and use cases here
     so they can be accessed by people trying to use your code.
    This is also the first place you should go if you are trying
     to learn more about a class.
    Don't be afraid to make this docstring very long.
    """

    def __init__(self, fasta_file_name):  # REMEMBER: 'self' links the definition to the information stored in the class
        """
        This is the initilization method, it takes in arguments when the class is first constructed
        In our case it should take in ('test.fasta') or the location to many fasta files.
        """
        self.file_name = fasta_file_name
        self.lines = [x.strip() for x in open(fasta_file_name)]
        self.headers = [x.strip() for x in open(fasta_file_name) if x.startswith('>')]  # Here we set an attribute of the FastaReader object,
                                                                                #  other definitions can access this with self.headers
        return


    def __str__(self):
        """
        When we print(FastaReader('test.fasta')), this method's return statement will be what is printed.
        If this method is not defined, it will print: <__main__.FastaReader object at 0x045BEE70>
         and that is not very useful for anyone.
        :return: ALWAYS A STRING
        """
        return "Fasta File: {}, Length:{}".format(self.file_name, len(self))


    def __len__(self):
        """
        This definition defines how to answer the question:  len(FastaReader())
        How should we determine the length of a FASTA file? Up to you.
        :return: int
        """
        return len(self.headers)


    def to_dict(self):
        """
        This is like a normal definition, but, because it is part of a class and has a 'self' input,
         it must be called on a FastaReader() object. You cannot run x = to_dict(); it must be
         x = FastaReader().to_dict()
        :return: dict
        """
        return {self.lines[i]: self.lines[i+1] for i in range(0,len(self.lines),2)}


## What does our class look like without all of the documentation?

class FastaReader:

    def __init__(self, fasta_file_name):
        self.file_name = fasta_file_name
        self.lines = [x.strip() for x in open(fasta_file_name)]
        self.headers = [x.strip() for x in self.lines if x.startswith('>')]


    def __str__(self):
        return "Fasta File: {}, Length:{}".format(self.file_name, len(self))


    def __len__(self):
        return len(self.headers)


    def to_dict(self):
        return {self.lines[i]: self.lines[i+1] for i in range(0,len(self.lines),2)}



## How do we use it?

# create a new instance ("ff" is short for "fasta file")
ff = FastaReader('data/example.fasta')

# make a dictionary
x = ff.to_dict()
print(x)

# how many entries?
print(len(ff))

# what is ff?
print(ff)

# loop over each header
for header in ff.headers:
    print("Header is: '{}'".format(header))


