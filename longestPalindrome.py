def longestPalindrome(s) :
    maxLenPalindrome = 0
    for i in range (0, len(s)) :
        if isPalindrome(s[i : len(s)]) :
            lenPalindrome = len (s[i : len(s)])
            if lenPalindrome > maxLenPalindrome :
                maxLenPalindrome = lenPalindrome
                maxPalindrome = s[i : len(s)]
    print ("longest palindrome(" + s[i : len(s)] + ")" + maxPalindrome )

def isPalindrome(s) :
    revstr = ""
    for i in s:
        revstr = i+revstr
    if revstr == s :
        return True
    return False

longestPalindrome("efef")
