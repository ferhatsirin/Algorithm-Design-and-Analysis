
def optimumOrder (timeList, weightList) :
    jobOrder =[]
    for i in range(0,len(timeList)) :
        list =[(i+1)]
        list.append(float(weightList[i])/timeList[i])
        jobOrder.append(list.copy())

    size =len(jobOrder)
    for i in range(0,size) :
        max=i
        for j in range(i+1,size) :
            if jobOrder[max][1] < jobOrder[j][1] :
                max =j

        temp =jobOrder[i]
        jobOrder[i] =jobOrder[max]
        jobOrder[max] =temp

    sum =0
    finish =0
    for i in range(0,size) :
        jobList =jobOrder.pop(0)
        job =jobList[0]-1
        time =timeList[job]
        weight =weightList[job]
        finish =finish+time
        sum =sum +finish*weight
        jobOrder.append(job+1)

    result =[jobOrder,sum]
    return result

if __name__ == "__main__" :
    print("How many jobs will you enter :" ,end="")
    size =int(input())
    timeList =[]
    weightList =[]

    for i in range(1,size+1) :
        print("Enter the %d. job's time :" %(i) ,end="")
        time =int(input())
        print("Enter the %d. job's weight :" %(i) ,end="")
        weight =int(input())
        timeList.append(time)
        weightList.append(weight)

    order =optimumOrder(timeList,weightList)
    print("\nOptimum job order :",order[0])
    print("Weighted sum of completion times :",order[1])


