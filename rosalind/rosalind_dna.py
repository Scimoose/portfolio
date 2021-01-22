# Count how much ATCG nucleotides are there in DNA sample
# It's a pretty straighforward solution, I had to accidentaly stumble upon (took 4 tries with different code)


# importing dataset
dataset = open("rosalind_dna.txt").read()


print("There are: ", dataset.count("A"), "A ", dataset.count("C"), "C", dataset.count("G"), "G", dataset.count("T"), "T")
    
