
def optimalPlan (NY,SF,move) :
    optN =[0]
    optNPath =[]
    optS =[0]
    optSPath =[]
    size =len(NY)
    for i in range(1,size+1) :
        if optN[i-1] < (optS[i-1]+move) :
            optN.append(NY[i-1]+optN[i-1])
            optNPath.append("NF")
        else :
            optN.append(NY[i-1]+optS[i-1]+move)
            optNPath =optSPath[0:i-1].copy()
            optNPath.append("NF")
        if optS[i-1] < optN[i-1]+move :
            optS.append(SF[i-1]+optS[i-1])
            optSPath.append("SF")
        else :
            optS.append(SF[i-1]+optN[i-1]+move)
            optSPath =optNPath[0:i-1].copy()
            optSPath.append("SF")

    result =[]
    if optN[size] < optS[size] :
        result.append(optNPath)
        result.append(optN[size])
    else :
        result.append(optSPath)
        result.append(optS[size])

    return result



if __name__ == "__main__" :
    print("How many months will you enter :",end ="")
    month =int(input())

    print("Enter the moving cost :",end="")
    move =int(input())

    NY =[]
    for i in range(0,month) :
        print("Enter New York's %d. month cost :" %(i+1) ,end="")
        cost =int(input())
        NY.append(cost)

    SF =[]
    for i in range(0,month) :
        print("Enter San Francisco's %d. month cost :" %(i+1) ,end="")
        cost =int(input())
        SF.append(cost)


    print("Months         ",end="")
    for i in range(1,month+1) :
        print("%-5d" %(i), end="")
    print("")

    print("New York       ",end="")
    for i in range(0,month) :
        print("%-5d" %(NY[i]),end="")
    print("")

    print("San Francisco  ",end="")
    for i in range(0,month) :
        print("%-5d" %(SF[i]),end="")
    print("\n")

    plan =optimalPlan(NY,SF,move)
    print("Optimal plan :",plan[0])
    print("Total cost for this plan :",plan[1])





