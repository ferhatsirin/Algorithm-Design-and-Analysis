
def checkPattern(str,pattern,patternList):

    if len(str) == 0 and len(pattern) == 0 :
        return True

    if len(pattern)  ==0 :
        print("Pattern is not valid for a given string because remaining string \"%s\" does not have any match" %(str))
        return False
    if len(str) == 0:
        print("Pattern is not valid for a given string because remaining pattern \"%s\" does not have any match" % (pattern))
        return False

    if patternList[pattern[0]] ==str[0:len(patternList[pattern[0]])] :
        return checkPattern(str[len(patternList[pattern[0]]):],pattern[1:],patternList)
    else :
        print("Pattern is not valid for a given string because string's \"%s\" does not match with pattern's \"%s\"->%s " % (str[0:len(patternList[pattern[0]])],pattern[0],patternList[pattern[0]]))
        return False

if __name__ == "__main__" :
    print("First create your pattern list")
    print("To create a pattern list first enter a string then its representation like \"A\" -> \"to\"")
    print("Enter -1 to exit the loop")
    patternList =dict()
    while True :
        print("Enter a string : ",end ="")
        str =input()
        if str.isalpha() :
            print("Enter representation of \""+str+"\" : ",end="")
            patternList[str] = input()
        else :
            break

    print("Your pattern list is : ",patternList)
    choice ="yes"
    while choice[0].lower() =="y":
        print("Now, enter your string : ",end="")
        str =input()
        print("Now, enter your pattern to check if given string is valid for it : ",end="")
        pattern =input()
        result =checkPattern(str,pattern,patternList)
        if result :
            print("Pattern \"%s\" is valid for given string \"%s\" "%(pattern,str))

        print("Do you want to use the program with the same pattern list -> yes or no : ",end ="")
        choice =input()

        



