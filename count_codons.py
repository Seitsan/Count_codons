def count_codons(dna:str) -> dict:
    """
    Takes DNA sequence as input, splits it at codons, than counts these codons
    :param dna: DNA sequence as string
    :return: Dict with codons as keys and these quality as value
    """
    codons = {}
    count = 1
    for i in range(0, len(dna)-2, 3):
        codon = dna[i:i+3]
        codons[codon] = codons.get(codon, 0) + 1
    return codons


def dna_verification(dna:str) -> bool:
    """
    Takes DNA sequence as input and check if all characters are nucleotides
    :param dna: A DNA sequence as string
    :return: True or False
    """
    return set(dna).issubset({'A', 'T', 'G', 'C'})


def main():
    sequence = input('Input a DNA sequence: ')
    dna = sequence.upper()
    if dna_verification(dna):
        sorted_codons = dict(sorted(count_codons(dna).items(), key=lambda item: item[1], reverse = True))
        print(sorted_codons)
    else:
        print('This string is not a DNA sequence')

main()