from collections import defaultdict
from collections import deque

def isConnected (graph,x,y) :
    queue = deque()
    visited = [False] * (len(graph) + 1)
    queue.append(x)
    visited[x] = True

    while (0 <len(queue)):
        vertex = queue.popleft()
        for s in graph[vertex]:
            if y == s :
                return True
            if visited[s] == False:
                queue.append(s)
                visited[s] = True

    return False



def checkConstraints (equality,inequality) :
    while 0 <(len(inequality)) :
        list =inequality.pop(0)
        x =list.pop()
        y =list.pop()
        if isConnected(equality,x,y) :
            result =[False]
            result.append([y,x])
            return result

    result =[True]
    return result



if __name__ == "__main__" :
    print("Enter the variable size ", end="")
    size =int(input())
    equality =defaultdict(set)
    for i in range(0,size+1) :
        equality[i]

    equalityList =[]
    print("Enter the equality constraints")
    print("Equality input should be like this : 1 2 means x1 = x2 ")
    while (True) :
        print("Current equality list :",equalityList)
        try :
            print("Enter the first variable, to end the loop enter a letter like 'e' " )
            var1 =int(input())
            print("Enter the second variable ")
            var2 =int(input())
            equalityList.append("X%d=X%d"%(var1,var2))
            equality[var1].add(var2)
            equality[var2].add(var1)

        except :
            break
    inequality =[]
    inequalityList =[]
    print("Enter the inequality constraints")
    print("Inequality input should be like this : 1 2 means x1 != x2 ")
    while (True) :
        print("Current inequality list :", inequalityList)
        lst =[]
        try :
            print("Enter the first variable, to end the loop enter a letter like 'e'" )
            var1 =int(input())
            lst.append(var1)
            print("Enter the second variable ")
            var2 =int(input())
            lst.append(var2)
            inequalityList.append("X%d!=X%d"%(var1,var2))
            inequality.append(lst)
        except :
            break



    print("Equalities : ", equalityList)
    print("Inequalities : ",inequalityList)

    result =checkConstraints(equality,inequality)
    if result.pop(0) :
        print("The constraints can be satisfied ")
    else :
        list =result.pop()
        print("The constraints can not be satisfied because X%d and X%d is equal " %(list[0],list[1]))




