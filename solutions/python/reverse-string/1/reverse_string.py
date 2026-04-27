def reverse(text):
    
    arr = list(text)
    strr = ""

    for i in range(len(arr)-1, -1, -1):
        strr += arr[i]

    return strr