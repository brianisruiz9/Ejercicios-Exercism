def to_rna(dna_strand):
    msg=""
    for i in dna_strand:
        if i == "G":
            msg += "C"
        if i == "C":
            msg += "G"
        if i == "T":
            msg += "A"
        if i == "A":
            msg += "U"
    
    return msg