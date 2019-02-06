from collections import defaultdict

def optimalPath (hotelList) :
    hotelList.insert(0,0)
    optPenalty =[0]
    optPath =defaultdict(list)
    optPath[0] =[]

    for i in range(1,len(hotelList)) :
        min = optPenalty[0]+(200-(hotelList[i]-hotelList[0]))**2
        index =0
        for j in range(1,i) :
            value =  optPenalty[j]+(200-(hotelList[i]-hotelList[j]))**2
            if value < min :
                min = value
                index =j

        optPenalty.append(min)
        optPath[i] =optPath[index].copy()
        optPath[i].append(i)
    result =[]
    result.append(optPath[len(hotelList)-1])
    result.append(optPenalty[len(hotelList)-1])
    return result


def takeList() :
    print("How many hotel do you want to enter : ",end="")
    size =int(input())
    list =[]
    for i in range(0,size) :
        print("Enter %d. hotel distance from start point :" %(i+1) ,end="")
        list.append(int(input()))

    return list

if __name__ == "__main__" :
    hotelList =[190,220,410,580,640,770,950,1100,1350]
    print("Default hotel distance list : ",hotelList)
    print("Will you use the default list (yes) or enter a new list (no) : ", end="")
    str =input()
    if str[0].lower() =="n" :
        hotelList =takeList()

    print("Hotel distance List : ",hotelList)
    result =optimalPath(hotelList)
    print("Optimal path for this list :", result[0])
    print("Total penalty for this path is : ",result[1])



