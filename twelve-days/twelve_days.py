def recite(start_verse, end_verse):
    days = [ "first", 
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
            "tenth",
            "eleventh",
            "twelfth"]

    verses = [
            "a Partridge in a Pear Tree",
            "two Turtle Doves",
            "three French Hens",
            "four Calling Birds",
            "five Gold Rings",
            "six Geese-a-Laying",
            "seven Swans-a-Swimming",
            "eight Maids-a-Milking",
            "nine Ladies Dancing",
            "ten Lords-a-Leaping",
            "eleven Pipers Piping",
            "twelve Drummers Drumming"
        ]
    
    song = []
        
    for i in range(start_verse, end_verse + 1):
        day_number = days[i - 1]

        if i > 1:
            delimiter=', '
            gifts = delimiter.join(verses[i - 1:0:-1]) + ', and {}'.format(verses[0])
        else:
            gifts = verses[0]

        msg = f"On the {day_number} day of Christmas my true love gave to me: {gifts}."
        song.append(msg)

    return song

