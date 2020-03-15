def is_isogram(string):
    new = string.lower().replace(" ", "").replace("-", "")
    for i in range(0, len(new)):
        for j in range(i + 1, len(new)):
            if new[i] == new[j]:
                return False
    return True
