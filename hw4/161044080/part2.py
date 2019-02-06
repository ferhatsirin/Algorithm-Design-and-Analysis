

def check (dict, str) :
    return str.lower() in dict


def splitValidWords (dict,text) :

    splitPoint =[False]*(len(text)+1)
    words =[]
    splitPoint[0] =True
    for i in range(0,len(text)+1):
        for j in range(0,i) :
            if splitPoint[j] and check(dict,text[j:i]) :
                splitPoint[i] =True
                words.append(text[j:i])

    result =[]
    result.append(splitPoint[len(text)])
    result.append(words)
    return result


def updateDict (dict):
    while (True) :
        print("Current dictionary :",dict)
        print("Enter the word, to end the loop enter a number like 1")
        str =input()
        if str.isdigit() :
            break
        else :
            dict.append(str)

    return dict


if __name__ == "__main__" :
    dictionary =["the","was", "it", "best", "of", "times"]
    print("Default dictionary is :",dictionary)
    print("Do you want to add any word to it  yes or no : ",end="")
    str =input()
    if str[0].lower() == "y" :
        dictionary =updateDict(dictionary)
        print("Current dictionary : ",dictionary)

    print("Enter the corrupted text : ",end="")
    text =input()

    result =splitValidWords(dictionary, text)
    if result.pop(0) :
        print("Corrupted text split into ", result.pop())
    else:
        print("Corrupted text could not split after the ",result.pop())



