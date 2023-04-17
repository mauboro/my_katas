
def DNA_strand(dna):
    return "".join(["A" if x == "T" else "T" if x == "A" else "G" if x == "C" else "C" if x == "G" else 0 for x in dna])

def DNA_strand_refactored(dna):
    return dna.translate(dna.maketrans("ATGC", "TACG"))

def DNA_strand_refactored_again(dna):
    pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(pairs[x] for x in dna)
