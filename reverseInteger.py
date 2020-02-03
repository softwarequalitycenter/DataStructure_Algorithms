def reverseInt(n) :
    strn = str(n)
    lenn = len(strn)
    strnrev =''
    for i in range(0, lenn ):
        strnrev = strnrev + strn[lenn-1-i]
    return strnrev

print (reverseInt(123))
