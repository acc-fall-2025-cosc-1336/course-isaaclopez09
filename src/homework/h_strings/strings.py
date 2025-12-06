def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError
    distance = 0
    for a, b in zip(dna1, dna2):
        if a != b:
            distance += 1
    return distance
    
def get_dna_complement(dna):
    complement = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
        "a": "t",
        "t": "a",
        "c": "g",
        "g": "c"
    }

    reversed_dna = dna[::-1]
    result = ""

    for base in reversed_dna:
        if base not in complement:
            raise ValueError(f"Invalid DNA symbol: {base}")
        result += complement[base]

    return result