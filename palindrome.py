from pip._vendor.msgpack.fallback import xrange


def isPalindrome (s) :
    lenString = len(s)
    for i in xrange(0, int(lenString/2)):
        if (s[i] != s[lenString-i-1]):
            return False
    return True

val = isPalindrome ("neereen")
if val :
    print ("palindrome")
else:
    print ("not palindrome")

