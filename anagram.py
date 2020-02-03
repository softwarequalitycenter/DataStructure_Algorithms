def anagram (s1,s2) :
    if (sorted (s1) == sorted(s2)) :
        return True
    return False

if  anagram("geeks", "kseeg") :
    print ("yes")
else :
    print ("no")