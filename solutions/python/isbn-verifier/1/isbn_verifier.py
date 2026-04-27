import re


def is_valid(isbn):
    
    isbn_cleaned = isbn.replace("-", "")

    if len(isbn_cleaned) != 10:
        return False
    
    for i in isbn_cleaned[:-1]:
        if not i.isdigit():
            return False
        
    if isbn_cleaned[9] not in "0123456789X":
        return False
    
    int_list = [10 if i == "X" else int (i) for i in isbn_cleaned]

    summ = 0

    for i in range(0, 10, 1):
        summ += int_list[i] * (10-i)

    return summ % 11 == 0