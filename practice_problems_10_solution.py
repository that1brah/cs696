"""
practice_problems_10_solution.py
VERSION 0.1
CONTACT Klevi@sdsu.edu

This is an expansion to the previous homework's FastaReader class. For this practice you should:

    1. Write the clean_lines() function below this class. It should take in lines from FASTA files that
        have sequences on multiple lines between each header, like the bad_example.fasta for example:
            ['>header1', 'seq1', 'seq1.1', 'seq1.2', '>header2', 'seq2', 'seq2.1', 'seq2.2', '>header3', 'seq3', '>header4', 'seq4']))
        The sequences between each line should be concatenated to look like so:
            ['>header1', 'seq1seq1.1seq1.2', '>header2', 'seq2seq2.1seq2.2', '>header3', 'seq3', '>header4', 'seq4']))
        These new lines are then returned

    2. The __init__ function should also recognize if the input is a file or a directory using os.path.isfile()
         If the input is a Fasta file, it should be read and checked with clean_lines() normally
         If the input is not a file (and is a directory), then every Fasta file in the directory should
          be read and cleaned into self.lines

    3. Add Docstrings to the FastaReader class and class methods (you NEED to do the class Docstring)
        See: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html#google-vs-numpy
         for a brief overview of Google and NumPy Docstrings by Sphinx

    4. Solve the missing code in the methods, get_complements(), get_amino_acids(), write_csv(), and duplicate_headers()

    (continued for Practice Problems 10)

    5. Add the 5 definitions that use regular expressions to the FastaReader class,
        they should all return the total number of matches found across all sequences in the fasta file.

    6. Implement the functionality of args.d which should print the documentation for the FastaReader class
        To test this without a terminal in pycharm: Run -> Edit Configurations -> Parameters, type in "-d"

    7. The ASSERT test cases now only run when this script is run with --test or -t; add a check to see if the file
        'bad_example.fasta' exists; if it does not, generate it before running the tests.




"""
import sys, argparse
import re
import os

VERSION = 0.1

#  this dict is used for the complement() def, but there is no reason hiding it from other defs
COMP_DICT = {"A": "T", "T": "A", "C": "G", "G": "C"}

# this dict was removed from inside the function, its just a style choice
DNA_TO_AA = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'}


class FastaReader:
    """
    Your docstring here
    """

    def __init__(self, fname):
        self.name = fname

        if os.path.isdir(fname):
            files = [os.path.join(fname, x) for x in os.listdir(fname)]
        else:
            files = [fname]

        self.lines = []
        for f in files:
            self.lines += [x.strip() for x in open(f)]

        self.lines = _clean_lines(self.lines)
        self.headers = [x for x in self.lines if x.startswith('>')]
        self.seqs = [x for x in self.lines if not x.startswith('>')]

    def to_dict(self):
        return {h:s for h,s in zip(self.headers, self.seqs)}

    def get_headers(self, n):
        return self.headers[:n]

    def get_seqs(self, n):
        return self.seqs[:n]

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.headers)


    def get_complements(self):
        """
        :return: a list of all complemented sequences in the FASTA file
        """
        return [complement(x) for x in self.seqs]


    def get_amino_acids(self):
        """
        :return: a list of all translated amino acid strings from self.seqs
        """
        return [translate(x) for x in self.seqs]


    def duplicate_headers(self):
        """
        :return: True if duplicate headers exist, False otherwise
        """
        return not (len(self.headers) == len(set(self.headers)))


    def write_csv(self, csv_filename):
        """
        Write the contents of the Fasta file to CSV format,
        where the first column is the header,
        and the second column is the sequence.
        :return: a string of the absolute path to csv_filename using os.path.abspath(csv_filename)
         (https://stackoverflow.com/questions/51520/how-to-get-an-absolute-file-path-in-python)
        """
        # these next 3 lines could be a single line, but they SHOULD NOT be
        with open(csv_filename, 'w') as outfile:
            for head, seq in zip(self.headers, self.seqs):
                outfile.write("{},{}\n".format(head, seq))

        return os.path.abspath(csv_filename)



    def zinc_finger(self):
        """
        Using re.findall(), return the count of matched motifs to the zinc finger motif across all FASTA sequences
        in the string.  The motif is:
        a C
        followed by 2 to 4 of any Amino Acid
        followed by a C
        followed by 3 of any Amino Acid
        followed by a single L, I, V, M, F, Y, W, or C
        followed by any 8 Amino Acids
        followed by a single H
        followed by 3 to 5 of any Amino Acid
        followed by a single H
        """
        count = 0
        pattern = r'.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H'
        for seq in self.seqs:
            count += len(re.findall(pattern, seq))
        return count


    def kinase_count(self):
        """
        Using re.findall(), return the count of matched motifs to the kinase motif across all FASTA sequences
        in the string.  The motif is:
        a S or T
        followed by any 2 Amino Acids
        followed by a D or E
        """
        count = 0
        pattern = r'[ST].{2}[DE]'
        for seq in self.seqs:
            count += len(re.findall(pattern, seq))
        return count


    def atp_binding_count(self):
        """
        Using re.findall(), return the count of matched motifs to the ATP binding motif across all FASTA sequences
        the ATP binding motif is:
        An "A" or "G"
        followed by any 4 Amino Acids
        followed by a "G"
        followed by a "K"
        followed by a "S" or "T"
        """
        count = 0
        pattern = r'[AG].{4}GK[ST]'
        for seq in self.seqs:
            count += len(re.findall(pattern, seq))
        return count


def translate(seq):
    """
    Same with complement, this may be useful to other classes
    """
    return ''.join([DNA_TO_AA[seq[i:i+3]] for i in range(0,len(seq),3)])


def complement(seq):
    """
    This definition was not part of the homework, but it's best practice to keep it outside of the class here
    """
    return ''.join([COMP_DICT[x] for x in seq])


def _clean_lines(lines):
    """
    if the lines of a FASTA file do not alternate sequence and header,
    then concatenate all sequences between each header and return a list of the new lines
    (Remember, the "_" Underscore at the beginning of a definition means it is intended to
      be 'private', but nothing is really 'private' in python -
      see https://mail.python.org/pipermail/tutor/2003-October/025932.html for a laugh)
    """
    # this is a verbose solution with decent time
    new_lines = []
    seq = ''
    header = None
    for line in lines:
        if line.startswith('>'):
            if seq:
                new_lines.append(header)
                new_lines.append(seq)
                seq = ''
            header = line.rstrip()
        else:
            seq += line.rstrip()
    new_lines.append(header)
    new_lines.append(seq)

    return new_lines




if __name__ == '__main__':
    # Uncomment the next 2 lines to generate bad_example.fasta and example.fasta:

    # with open('bad_example.fasta', 'w') as outfile:
    #     outfile.write('\n'.join(['>header1', 'seq1', 'seq1.1', 'seq1.2', '>header2', 'seq2', 'seq2.1', 'seq2.2', '>header3', 'seq3', '>header4', 'seq4']))
    #
    # with open('example.fasta', 'w') as outfile:
    #     outfile.write('\n'.join(['>header1', 'seq1', '>header2', 'seq2', '>header3', 'seq3', '>header4', 'seq4']))

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-d', help='Prints the full FastaReader class docstring', action='store_true')
    parser.add_argument('-v', '--version', dest='asdf', help='Prints the version of FastaReader', action='store_true')
    parser.add_argument('-t', '--test', help='Runs the assert statements to test '
                                             'this class using the file "bad_example.fasta",'
                                             'at the start of args.test, check if the file exists using os,'
                                             'if the file is not available, generate it before running the tests', action='store_true')

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(1)

    if args.d:
        print(FastaReader.__doc__)
        sys.exit(0)

    if args.version:
        print("FastaReader version {}".format(str(VERSION)))
        sys.exit(0)

    if args.test:
        ff = FastaReader('bad_example.fasta')

        x = ff.to_dict()
        assert x == {'>header1': 'seq1seq1.1seq1.2', '>header2': 'seq2seq2.1seq2.2', '>header3': 'seq3', '>header4': 'seq4'}, print(x)

        x = ff.headers
        assert x == ['>header1', '>header2', '>header3', '>header4']

        x = ff.get_headers(2)
        assert x == ['>header1', '>header2']

        x = ff.seqs
        assert x == ['seq1seq1.1seq1.2', 'seq2seq2.1seq2.2', 'seq3', 'seq4']

        x = ff.get_seqs(3)
        assert x == ['seq1seq1.1seq1.2', 'seq2seq2.1seq2.2', 'seq3']

        x = len(ff)
        assert x == 4

        x = str(ff)
        assert x == 'bad_example.fasta'




