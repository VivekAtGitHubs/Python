# most common sentence
from collections import Counter
sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = Counter(words)
top_three = frequency.most_common(3)
print("Three most common words:")
for word, count in top_three:
    print(word, ":", count)