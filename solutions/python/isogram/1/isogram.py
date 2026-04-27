import re


def is_isogram(string):
    

    strr = string.lower()
    strr = re.sub(r'[^a-z]', "", strr)
    
    print(strr)

    my_set = set(strr)

    return len(strr)==len(my_set)
