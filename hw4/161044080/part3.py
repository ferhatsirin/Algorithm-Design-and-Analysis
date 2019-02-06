
def merge(arr1, arr2) :
    output =[]

    if len(arr1) ==0 :
        output.extend(arr2)
        return output

    if len(arr2) ==0 :
        output.extend(arr1)
        return output

    if arr1[0] <arr2[0] :
        output.append(arr1[0])
        arr1.pop(0)
    else:
        output.append(arr2[0])
        arr2.pop(0)

    output.extend(merge(arr1,arr2))

    return output


def combineArrays(list) :
    if len(list) == 1 :
        return list.pop()

    result =merge(list.pop(),list.pop())
    list.append(result)

    return combineArrays(list)



if __name__ == "__main__" :

    print("How many array do you want to enter : ",end="")
    n =int(input())
    print("Enter the size of the arrays : ",end="")
    size =int(input())

    list=[]
    for i in range(n) :
        innerList =[]
        for j in range(size) :
            print("Enter %d. array %d. number : " % (i+1,j+1) ,end="" )
            innerList.append(int(input()))
        innerList.sort()
        list.append(innerList.copy())

    print("List of arrays :", list)

    list =combineArrays(list)
    print("After combining the arrays : ",end="")
    print(list)


