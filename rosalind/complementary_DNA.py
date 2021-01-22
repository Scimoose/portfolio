# This code makes complimentary DNA strand to the one given

dataset = open("rosalind_revc.txt").read()
# dataset = "AAAACCCGGT"


# make a trantab with complimentary bases: A-T, T-A, C-G, G-C
intab = "ATCG"
outtab = "TAGC"
comp = dataset.maketrans(intab, outtab)
comp = dataset.translate(comp)

# reverse the string/list to get complimentary string
rev = comp[::-1]

print(rev)
