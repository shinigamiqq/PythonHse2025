def is_plagiat(word1: str, word2: str):
    set1 = set(word1.lower())
    set2 = set(word2.lower())

    return len(set2 - set1) <= 1

word1 = input()
word2 = input()

print(is_plagiat(word1, word2))

