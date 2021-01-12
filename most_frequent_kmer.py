
def BetterFrequentWords(Text, k):
    kmers = {}
    hf = 0

    for i in range(len(text) - k):
        p_kmer = text[i : i+k]
        if p_kmer in kmers.keys():
            kmers[p_kmer] += 1
            if kmers[p_kmer] > hf:
                hf = kmers[p_kmer]
        else:
            kmers[p_kmer] = 1
            if kmers[p_kmer] > hf:
                hf = kmers[p_kmer]
    
    frequentPatterns = [key for key in kmers.keys() if kmers[key] == hf]
    return frequentPatterns

f = open('F:\Bioinformatics I\dataset_2_13.txt')
text = f.readline()
text = text[ : len(text)-1]
k = int(f.readline())

print(BetterFrequentWords(text, k))



