def response(hey_bob):
    
    #first strip off whitespaces
    hey_bob_stripped = hey_bob.strip()

    if hey_bob_stripped == "":
        return "Fine. Be that way!"
    
    elif hey_bob_stripped.isupper() and hey_bob_stripped.endswith("?"):
        return "Calm down, I know what I'm doing!"
    
    elif hey_bob_stripped.isupper():
        return "Whoa, chill out!"
    
    elif hey_bob_stripped.endswith("?"):
        return "Sure."
       
    else:
        return "Whatever."