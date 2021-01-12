f = open('F:\Bioinformatics I\dataset_3_2.txt')

pattern = f.readline()
pattern = pattern[ : len(pattern)-1]

compliment = str("")

for base in pattern:
    if base == 'A':
        compliment += 'T'
    elif base == 'G':
        compliment += 'C'
    elif base == 'C':
        compliment += 'G'
    elif base == 'T':
        compliment += 'A'

print(compliment[::-1])