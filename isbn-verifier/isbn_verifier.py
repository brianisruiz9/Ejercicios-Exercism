import re

def is_valid(isbn):
    pattern = re.compile('^[0-9]{9}[0-9X]$')
    isbn = isbn.replace("-", '')
    if pattern.match(isbn):
        return sum([(n + 1) * (10 if m == 'X' else int(m)) for n, m in enumerate(reversed(isbn))]) % 11 == 0
    return False