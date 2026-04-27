import string


def rotate(text, key):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    shifted_lower = lowercase[key:26] + lowercase[0:key]
    shifted_upper = uppercase[key:26] + uppercase[0:key]

    mapped = str.maketrans(lowercase+uppercase, shifted_lower+shifted_upper)

    return text.translate(mapped)