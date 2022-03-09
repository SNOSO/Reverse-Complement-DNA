def complement(DNA):
    comp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    compDNA = ''
    for b in DNA:
        compDNA += comp[b]
    return compDNA

def reverse(DNA):
    return DNA [::-1]

def reverse_complement(DNA):
    compDNA = complement(DNA)
    revcompDNA = reverse(compDNA)
    return revcompDNA


DNA = input('Please enter DNA sequence')
revcompDNA = reverse_complement(DNA)
print(' you have entered: ', DNA)
print('reverse comp', revcompDNA )
