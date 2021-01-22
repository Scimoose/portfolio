# This scripts aim is to translate RNA strands to protein
from itertools import zip_longest
from textwrap import wrap


dataset = open("rosalind_prot.txt").read()
# dataset = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

data = wrap(dataset, 3)
print(data)
#
INPUT = ["GCU", "GCC", "GCA", "GCG", "UGU", "UGC", "GAU", "GAC", "GAA", "GAG",
         "UUU", "UUC", "GGG", "GGC", "GGA", "GGU", "CAU", "CAC", "AUU", "AUC",
         "AUA", "AAA", "AAG", "UUA", "UUG", "CUA", "CUU", "CUC", "CUG", "AUG",
         "AAU", "AAC", "CCU", "CCC", "CCA", "CCG", "CAA", "CAG", "CGU", "CGC",
         "CGA", "CGG", "AGA", "AGG", "UCA", "UCC", "UCG", "UCU", "AGU", "AGC",
         "ACU", "ACA", "ACC", "ACG", "GUU", "GUG", "GUA", "GUC", "UGG", "UAU",
         "UAC"]
OUTPUT = ["A", "A", "A", "A", "C", "C", "D", "D", "E", "E", "F", "F", "G", "G",
          "G", "G", "H", "H", "I", "I", "I", "K", "K", "L", "L", "L", "L", "L",
          "L", "M", "N", "N", "P", "P", "P", "P", "Q", "Q", "R", "R", "R", "R",
          "R", "R", "S", "S", "S", "S", "S", "S", "T", "T", "T", "T", "V", "V",
          "V", "V", "W", "Y", "Y"]

str = ""

for bases in data:
    for i, o in zip_longest(INPUT, OUTPUT):
        if i == bases:
            str += o

print(str)
