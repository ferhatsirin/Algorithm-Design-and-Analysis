from xlrd import open_workbook
from collections import defaultdict
from collections import deque

def breadthFirstSearch (graph, start) :
    queue = deque()
    visited = [False] * (len(graph)+1)
    queue.append(start)
    visited[rootV] =True

    print("Breadth First Search Visit Order : ",end ="")
    breadthSearch(graph,queue,visited)

def breadthSearch(graph,queue,visited):
    if queue :
        vertex = queue.popleft()
        for s in graph[vertex]:
            if visited[s] == False:
                queue.append(s)
                visited[s] = True

        if queue :
            print(vertex ,"-> ",end ="")
        else :
            print(vertex)

        breadthSearch(graph,queue,visited)

def depthFirstSearch(graph,vertex,visited =None) :
    if visited is None:
        visited =set()
        visited.add(vertex)

        print ("Depth First Search Visit Order : ",end ="")

    else :
        visited.add(vertex)

    if len(visited) <len(graph) :
        print(vertex,"-> ",end="")
    else :
        print(vertex)

    for s in graph[vertex] :
        if s not in visited :
            depthFirstSearch(graph,s,visited)






if __name__ == "__main__" :
    graph =defaultdict(list)

    file =open_workbook("Graph_data.XLS")
    sheet =file.sheet_by_index(0)
    rootV =int(sheet.cell(0,1).value)
    for x in range(3,sheet.nrows) :
        graph[int(sheet.cell(x,0).value)].append(int(sheet.cell(x,1).value))
        graph[int(sheet.cell(x,1).value)]

    breadthFirstSearch(graph,rootV)
    depthFirstSearch(graph,rootV)
