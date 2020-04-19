from typing import Set, List
import random

class newNode:
    def __init__(self, x, y, nodeVal):
        self.val = nodeVal
        self.x = x
        self.y = y
        self.adjList = set()

class GridGraph:
    def __init__(self):
        self.nodesList = set() 

    def AddGridNode(self, x:int, y:int, nodeVal:str)-> None:
        Node = newNode(x, y, nodeVal)
        self.nodesList.add(Node)
        return Node

    def addUndirectedEdge(self, first:newNode, second:newNode)-> None:
        first.adjList.add(second)
        second.adjList.add(first)
        if (abs(first.x- second.x) == 1 and abs(first.y- second.y) == 0) or(abs(first.x- second.x) == 0 and abs(first.y- second.y) == 1):
            first.adjList.add(second)
            second.adjList.add(first)

    def removeUndirectedEdge(self, first:newNode, second:newNode)->None:
        first.adjList.remove(second)
        second.adjList.remove(first)
    
    def getAllNodes(self)->Set[newNode]:
        return self.nodesList

    def getNode(self, x:int, y:int)->newNode:
        set = self.nodesList
        for node in set:
            if node.x == x and node.y == y:
                return node
        return None
    
def main():

    def createRandomGridGraph(num:int)->GridGraph:
        n = num+1
        gridGraph = GridGraph()
        dict = {}
        for i in range (n):
            for j in range (n):
                nodeVal = random.randint(1,10000)
                N = gridGraph.AddGridNode(i,j, nodeVal) 
                ans = dict.get(N, "no")
                if ans != "no": #means nodeVal is not original
                    flag = True
                    while flag:
                        N = gridGraph.AddGridNode(i,j, i*2) 
                        ans = dict.get(N, "no")
                        if ans == "no":
                            flag = False
                dict[N] = 1  
        allNodes = gridGraph.getAllNodes()
        for node in allNodes:
            x = node.x
            y = node.y
            r = random.randint(1,4)
            if r == 1:
                node2 = gridGraph.getNode(x, y+1)
            elif r == 2:
                node2 = gridGraph.getNode(x, y-1)
            elif r == 3:
                node2 = gridGraph.getNode(x-1, y)
            elif r == 4:
                node2 = gridGraph.getNode(x+1, y)
            gridGraph.addUndirectedEdge(node,node2)
        return gridGraph

    def manhattanDistance (srcNode:newNode, finalNode:newNode)-> int: 
        srcx = srcNode.x
        srcy = srcNode.y
        finalx = finalNode.x
        finaly = finalNode.y
        d = abs(finalx - srcx) + abs(finaly-srcy)
        return d

    def astar(sourceNode:newNode, destNode:newNode)-> List[newNode]: 
        visited = set()
        distancedict = {}
        parentDict = {}
        distancedict[sourceNode] = 0
        parentDict[sourceNode] = None
        finalDist = {}
        finalDist[source] = manhattanDistance(sourceNode, destNode)
        curr = sourceNode
        a = True
        while a:
            adjlist = curr.adjList
            for neighbor in adjlist:
                if neighbor not in visited: 
                    if distancedict.get(neighbor) == None: #same as infinite
                        distancedict[neighbor] = distancedict[curr] 
                        parentDict[neighbor] = curr
                        finalDist[neighbor] = distancedict[neighbor] + manhattanDistance(neighbor,destNode)
                    else:
                        if distancedict[curr]  < distancedict[neighbor]:
                            distancedict[neighbor] = distancedict[curr] 
                            parentDict[neighbor] = curr
                            finalDist[neighbor] = distancedict[neighbor] + manhattanDistance(neighbor,destNode)
            visited.add(curr)
            min_ = float('inf')
            for node in distancedict: #get the smallest val in dictionary
                if node not in visited:
                    if finalDist[node] < min_:
                        min_ = finalDist[node]
                        curr = node
            if curr == destNode:
                break
        final_array = []
        final_array.insert(0, destNode) 

        parent = parentDict[destNode]
        while parent:
            final_array.insert(0, parent)
            parent = parentDict[parent]
        
        return final_array
        


if __name__ == "__main__":
    main()
