def score(word):
    new = word.upper()
    suma=0
    letter = {
        0: [''],
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10: ['Q', 'Z']
    }
    
    for i in letter.keys():
        for n in new:
            if n in letter[i]:
                suma+=i
    return suma