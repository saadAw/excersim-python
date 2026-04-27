import re


def is_pangram(sentence):
    

    strr = sentence.lower()
    strr = re.sub(r'[^a-z]', '', strr)

    counted = []

    for char in strr:
        if char in counted:
            continue
        if char not in counted:
            counted.append(char)

    return len(counted)==26