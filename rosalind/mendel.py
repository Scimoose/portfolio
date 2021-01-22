# Counts probability of the offspring having at least one dominant allele
import scipy.special.comb as comb


population = [2, 2, 2]


def mendel_dominant_prob(dom, het, rec):
    sum = dom + het + rec
    total = comb(sum, 2)
    print(total)


mendel_dominant_prob(population)
