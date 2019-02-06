
def search(arr,low,high) :
    if high >= low :
        midPoint =int((high+low)/2)
        if arr[midPoint] == midPoint :
            print ("A[%d] = %d "%(midPoint,midPoint))
        if midPoint <= arr[midPoint] :
            search(arr,low,midPoint-1)
        if arr[midPoint] <= midPoint:
            search(arr,midPoint+1,high)


if __name__ == "__main__" :

    arr =[]
    print("Enter numbers in turn, to end loop, enter a letter like 'e' ")
    i =0
    while True  :
        print("Enter %d. number : " %(i) ,end="")
        try :
            arr.append(int(input()))
            i +=1
        except :
            break

    arr.sort()
    print("Your array is : ",arr)
    search(arr,0,len(arr)-1)
