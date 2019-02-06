from collections import defaultdict
from xlrd import open_workbook


def inviteList (graph) :
    graph =graph.copy()
    people =list(graph.keys())
    size =len(graph.keys())
    for i in people :
        if len(graph[i]) <5 or size-5 < len(graph[i]) :
            graph.pop(i)
            for j in graph.keys() :
                if i in graph[j]:
                    graph[j].remove(i)

    return list (graph.keys())


if __name__ == "__main__" :
    graph =defaultdict(list)

    file =open_workbook("list.XLS")
    sheet =file.sheet_by_index(0)
    size =int(sheet.cell(0,1).value)
    for i in range(1,size+1) :
        name =sheet.cell(i,0).value
        n =int(sheet.cell(i,1).value)
        for j in range(2,n+2) :
            graph[name].append(sheet.cell(i,j).value)


    invited =inviteList(graph)
    print("List of the invited people : ",invited)
    uninvited =graph.keys()-invited
    print("List of the uninvited people : ",uninvited)





