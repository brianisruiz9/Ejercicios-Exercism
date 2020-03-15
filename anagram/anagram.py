def find_anagrams(word, candidates):
    anagrams = []
    for i in candidates:
        if sorted(word)== sorted(i.lower()) and i.lower() != word:
            anagrams.append(i)

    return anagrams
