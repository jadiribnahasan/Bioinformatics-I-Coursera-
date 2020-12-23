f = open('F:\Bioinformatics I\dataset_2_7.txt')

text = f.readline()
text = text[ : len(text)-1]
pattern = f.readline()
pattern = pattern[ : len(pattern)-1]

count = 0
for i in range(len(text) - len(pattern)):
    if text[i : i+len(pattern)] == pattern:
        count += 1
print(count)
