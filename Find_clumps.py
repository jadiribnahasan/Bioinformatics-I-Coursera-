f = open('F:\Bioinformatics I\dataset_4_5.txt')

text = f.readline()
text = text[ : len(text)-1]

k = 8
l = 27
t = 4

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
    
    return kmers

for i in range(len(text) - l):
    window = text[i : i+l]
    freqmap = BetterFrequentWords(window, k)
    clumps = [ key for key in freqmap.keys() if freqmap[key] >= t]
print(clumps)