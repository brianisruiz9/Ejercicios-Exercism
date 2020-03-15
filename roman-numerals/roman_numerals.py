def roman(number):
    NUMEROS = {
        1 : "I",
        2 : "II",
        3 : "III",
        4 : "IV",
        5 : "V",
        6 : "VI",
        7 : "VII",
        8 : "VIII",
        9 : "IX",
        10 : "X",
        40 : "XL",
        50 : "L",
        90 : "XC",
        100 : "C",
        400 : "CD",
        500 : "D",
        900 : "CM",
        1000 : "M",
    }

    res = ""
    for key in reversed(sorted(NUMEROS.keys())):
        if number >= key:
            count = number // key
            res += NUMEROS[key] * count
            number -= key * count
    return res
    
