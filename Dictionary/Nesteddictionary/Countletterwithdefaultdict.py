#count. number of words 
from collections import defaultdict
word = input("Enter a word: ")
counts = defaultdict(int)
for ch in word:
    counts[ch] += 1
print(dict(counts))