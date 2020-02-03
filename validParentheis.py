def validParenthesis (parstring) :
    stack = []
    for i in range(0,len(parstring)-1):
        if parstring[i] == '[' or parstring[i] == '{' or parstring[i] == '(' :
            stack.append (parstring[i])
        else :
            popped = stack.pop()
            if (parstring[i] == opposite(popped)):
                print("ppped -- " + popped)
            else:
                print('not ok')
                return

    print ("allok")

def opposite(c):
    if c=='[' :
        return ']'
    elif c=='{' :
        return '}'


validParenthesis ('[{}]')





