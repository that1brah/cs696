"""
Lecture 10 - Regular Expressions (Pattern matching)
"""


## Introduction - what is the problem?

# Here is a short hypothetical protein
protein = "HHCHYMLKTPPLPTWKQPAHHCCHGVACCCCGKTEWSNVMIFMVVEIEIFASKSNEENWSGMNIIEDDDPQHHFKNIYRKYLDFQ"

# Remember: each one of those letters is a molecule with different properties, http://www.jalview.org/help/html/misc/aaproperties.html
# If two amino acids are similar enough, its possible to swap one for the other and still have the same biological function
# Therefore, to investigate a protein we often need flexible pattern matching

# There are many different proteins that interact with DNA, some of them bind to DNA using a "Zinc finger" motif: https://en.wikipedia.org/wiki/Zinc_finger
# Let's consider a hypothetical motif (we will use the term motif to describe a repeated pattern).
# A modified Zinc Finger motif is:
#   2     (H)istidine
#   1-2   (C)ystine
#   1     (H)istidine

# How do we search our protein for this pattern?

for i in range(len(protein)):  # bug prone, crashing if motif at end, or missing long motifs if stopped too soon
    if protein[i] == "H":
        if protein[i+1] == "H":
            if protein[i+2] == "C":
                if protein[i+3] == "C" or protein[i+3] == "H":
                    if protein[i+4] == "H" and not protein[i+3] == "H":
                        print("Size 5 motif at: {}".format(i))
                    elif protein[i+3] == "H":
                        print("Size 4 motif at: {}".format(i))



# How annoying is that? and that was a simple pattern too!
# What if the pattern was:
#    a C
#    followed by 2 to 4 of any Amino Acid
#    followed by a C
#    followed by 3 of any Amino Acid
#    followed by a single L, I, V, M, F, Y, W, or C
#    followed by any 8 Amino Acids
#    followed by a single H
#    followed by 3 to 5 of any Amino Acid
#    followed by a single H



### Regular Expressions

## Most common ways you will use and see re

'''
import re

re.finditer(pattern, string) # Finds ALL non-overlapping matches, yields(returns) a MATCH OBJECT
re.findall(pattern, string)  # Finds ALL non overlapping matches, returns a list of tuples
re.split(pattern, string)    # Same as split(), but uses a regular expression
re.sub(pattern, new, string) # Same as .replace(), but uses a regular expression
re.compile(pattern)          # it exists, and you may see it, but it's almost never needed - see below

Uncompiled patterns are automatically compiled, the following two examples are the same:

# prog = re.compile(pattern)
# result = re.findall(prog, string)
and
# result = re.findall(pattern, string)

Both results are the same, and re caches recently used patterns automatically - don't use compile unless you know you need it.
'''

## Basic Examples - (No regex syntax, only our usual string patterns)
import re
test_protein = "YYLMHMWSFMMRFRKGGKPYHTVADARGPYDNGHLHKTYYLKNLMYYTVGMWVKEQLCCRHEPRSFLLAFIWSWCLAGVYRLTHRGSGPEMNRVVMFQYQDECSYLLQVTDVAYCNEQAWYARFWSCIAYYLSSFEMSSHELHTQHYYTLTGSVDWNMYVQNGVWAHGIACSMTDNQDGSCRQPIMDTDYVDTHDHEKRYRQRGLCSTPCNDQFPGYEFPTVHGTMAWISGEMMCASGYKPYNFKHGEFSPKSIWEWQLFACCCCGKTEWSNVMIFMVVEIEIFASKSNEENWSGMNIIEDDDPQHHFKNIYRKYLDYYLFQFYLIYGGYRMGFLHHRDSMINALVCKTGRWQQMHSFLKCDRRCKYLINIYADGKWYDNWSKVEDKVLDRGIRFLQSWNATEMVNSSMYRKPFYQSQYAPRFCWETFCQHEIYFHQEYASNCKARCGSYQSSAQSATLAIKYSELYQGFWGTSEWGHHQLFIHRWGVQIYQVKLHDSIMRPWIDWSRKCKWLLHRLHCDIELVPIHWEHKPQRVSFYYFKAMTDVLREICWSAQYHVVIQKFAFITMAWICTFYVHMYPSLDRHGSVTGIAWKLSGQWTGQEAYSKLNTEKETITEHNCPRVANIIVDCLEHEQVEMRMKRCHTWMVEVMKYPEQKFLWQCEHFRALYGLVGHNCPIKAWVRWIPHYYLMEQKVCSYFRRAYFMMLKNPMSRDSVCRREMEYDMAISRMPYGDCHAVGKWLPYFLNRYTPWWVWIWMAPFQGNRFFYHYKKDWRHCGNYLGGLCVLMTFWHHPIYVPCPKTKADFKQACCYCGKTRQACTDENMDTQRQKFQALHQARICQPYTVRNMSIQCGKNPIKANHNNNVRRPTMHICNLPAMTRRFVYTPFMKLKQSLGHDKWHIPEIQPYMDFTYHSVWIHQPHMNSCAACTGTVALALALALHYYTHPIQGEYIIYTSCDARYKSQKQEDIYQITSTCLEFSSKFKAQMMGTTWEIAGMNFCKVIETSCRQKI"


# re.findall
pattern = "YYL"
results = re.findall(pattern, test_protein)
print("Found {} results".format(len(results)))
for result in results:
    print(result)


# re.finditer
pattern = "YYL"
results = re.finditer(pattern, test_protein)
# print("Found {} results".format(len(results)))  # CRASH! generators have no len -> convert to list with list(results) if you want len
for result in results:
    print(result)  # they wrote a custom __str__ method for their "match" class! We will take a look later


# re.split - no regex patter used, same as built-in .split()
pattern = "YYL"
split_protein = re.split(pattern, test_protein)
print(split_protein)


# re.sub - no regex pattern used, same as built-in .replace()
pattern = "YYL"
new_prot = re.sub(pattern, "123", test_protein)
print(new_prot)



## What is the core regex syntax I should know?

# Note: its very unlikely that your re module is broken, there is probably an error in your pattern - don't give up!
#  A lot of errors can come from \ characters and single ' and double " quotes. I recommend using raw strings
#  pattern = "my \string"   ->   pattern = r"my \string"
#  Try Printing both out to see the difference

"""
Essential Regex Syntax
Demo with https://regex101.com/

Capture Groups () - most commonly (.*?)
    .   any character
    *   for as long as you want
    ?   if there are multiple end points of this match, choose the shortest one - python defaults to greedy search length

Match a set of characters [] - most commonly [a-zA-Z] to match any letter once (no numbers or symbols)
    [SH]    matches the character S or H (but only one character)
    the[ir][re]     matches the words 'there' and 'their' ((and also "therr" and "theie"))
    [0-9]   match any number once
    [a-z]   match any lowercase letter
    [a-zA-Z][a-zA-Z][a-zA-Z][0-9][0-9][0-9][0-9][0-9][0-9][0-9]   match any 3 letters followed by 7 numbers
            
Match this OR that with (this|that) - must match all characters in order
    (yes|y)         matches "yes" or "y"
    (No|no|N|n)     matches "No" or "no" or "N" or "n"

Match at least x, and and at most y, of a pattern {} - using the above example of 3 letters followed by 7 numbers
    [a-zA-Z]{3,4}[0-9]{7,8}      matches 3 to 4 letters followed by 7 to 8 numbers

Exclude characters with ^ 
    [a-zA-Z]{2,3}[^X][0-9]{7,9}  matches 2 to 3 letters, followed by any character except 'X', followed by 7 to 9 numbers
"""


## Combining Basic re usage with regex patterns

# What if the pattern was:
#    a C
#    followed by 2 to 4 of any Amino Acid
#    followed by a C
#    followed by 3 of any Amino Acid
#    followed by a single L, I, V, M, F, Y, W, or C
#    followed by any 8 Amino Acids
#    followed by a single H
#    followed by 3 to 5 of any Amino Acid
#    followed by a single H

# C
# C.{2,4}
# C.{2,4}C
# C.{2,4}C.{3}
# C.{2,4}C.{3}[LIVMFYWC]
# C.{2,4}C.{3}[LIVMFYWC].{8}
# C.{2,4}C.{3}[LIVMFYWC].{8}H
# C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}
# C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H

pattern = r"C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H"
results = re.findall(pattern, test_protein)
for result in results:
    print(result)



# a single M
# followed by a single V or I
# followed by a single M
# followed by either "VVVV" or "PPP"
# followed by 1 to 10 of the characters M, Q, and Y

# M
# M[VI]
# M[VI]M
# M[VI]M(VVVV|PPP)
# M[VI]M(VVVV|PPP)[MQY]{1,10}



