from Bio import SeqIO


data = open("D:/Projects/python code/rosalind/rosalind_motif.txt")
seq = data.readline()
domain = data.readline().rstrip('\n')

''' Testing purposes
seq = "GATATATGCATATACTT"
domain = "ATAT"
'''

''' Implementation of FASTA read
record = []
for seq_rec in SeqIO.parse("D:/Projects/python code/rosalind/ls_orchid.fasta", "fasta"):
    record.append(seq_rec.seq)

seq = record[0]
'''

locations = []
count = 0
loc = 0

while (count < len(seq)):
    loc = seq.find(domain, count)
    if (loc > 0):
        count = loc + 1
        locations.append(loc + 1)
    else:
        count = count + 1

print(' '.join(map(str, locations)))
