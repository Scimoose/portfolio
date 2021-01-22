# Transcribes DNA to RNA strand

# import dataset
# dt = open("rosalind_rna.txt").read()

# for testing purpose
dt = "AAATCCGGGTTCG"


# change T to U
def dna_rna(dataset):
    return dataset.replace("T", "U")


# invoke the method
print(dna_rna(dt))
