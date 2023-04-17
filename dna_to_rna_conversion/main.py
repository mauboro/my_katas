def dna_to_rna(dna):
    return "".join(["U" if l == "T" else l for l in dna])

def dna_to_rna_refactored(dna):
    return dna.replace("T", "U")
