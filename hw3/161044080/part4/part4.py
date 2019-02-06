
def sumArray(arr) :
    sum =0
    for i in range(0,len(arr)) :
        sum +=arr[i]

    return sum

def findMax(arr) :
    mid =int((len(arr)-1)/2)
    sum =0
    leftSum =arr[0] -1
    start =mid
    for i in range(mid,-1,-1) :
        sum +=arr[i]
        if sum > leftSum :
            leftSum  =sum
            start =i
    sum =0
    rightSum =arr[mid+1]-1
    end =mid+1
    for i in range(mid+1,len(arr)):
        sum +=arr[i]
        if sum > rightSum :
            rightSum =sum
            end =i

    return arr[start:end+1]



def findMaxSubSet(arr) :
    if len(arr)==1 :
        return [arr[0]]

    midPoint =int((len(arr)-1)/2)

    arr1 =findMaxSubSet(arr[0:midPoint+1])
    sum1=sumArray(arr1)

    arr2 =findMaxSubSet(arr[midPoint+1:len(arr)])
    sum2 =sumArray(arr2)

    arr3 =findMax(arr[0:len(arr)])
    sum3 =sumArray(arr3)

    if sum1 > max(sum2,sum3) :
        return arr1
    elif sum2 > max(sum1,sum3) :
        return arr2
    else:
        return arr3


if __name__ == "__main__" :

    arr =[]
    print("Enter numbers in turn, to end loop, enter a letter like 'e' ")
    i =1
    while True  :
        print("Enter %d. number : " %(i) ,end="")
        try :
            arr.append(int(input()))
            i +=1
        except :
            break


    print("Your array is : ",arr)
    subSet =findMaxSubSet(arr)
    sum =sumArray(subSet)

    print("Largest subset is :",findMaxSubSet(arr)," = ",sum)
