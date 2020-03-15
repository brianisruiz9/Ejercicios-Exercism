import re
def abbreviate(words):
    res = words.replace("\n", "").lower()
    lis = re.findall(r"[a-z0-9]+(?:'[a-z]+)?", res)
    
    new = ""
    for i in lis:
        new += i[0]
    
    return new.upper()
