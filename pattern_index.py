f = open('F:\Bioinformatics I\dataset_3_5.txt')

pattern = f.readline()
pattern = pattern[ : len(pattern)-1]
text = f.readline()
text = text[ : len(text)-1]

index= []
for i in range(len(text) - len(pattern)):
    if text[i : i+len(pattern)] == pattern:
        index.append(i)

print(*index)
