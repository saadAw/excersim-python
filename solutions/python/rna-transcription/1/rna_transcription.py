def to_rna(dna_strand):
    
    dna = "GCTA"
    rna = "CGAU"

    mapped = str.maketrans(dna, rna)

    return dna_strand.translate(mapped)