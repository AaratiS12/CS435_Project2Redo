import random
from typing import Set, List

class newNode:
    def __init__(self, nodeVal):
        self.val = nodeVal
        self.adjList = set()

class DirectedGraph:
    def __init__(self):
        self.listVertex = set() 
    def addNode(self, nodeVal:str) -> None:
        N = newNode(nodeVal)
        self.listVertex.add(N)
    def addUndirectedEdge(self, first:newNode, second:newNode)-> None:
        first.adjList.add(second)
    def removeUndirectedEdge(self, first:newNode, second:newNode) -> None:
        first.adjList.remove(second)
    def getAllNodes(self) -> Set[newNode]:
        return self.listVertex

class TopSort:
    def Kahns(self, graph:DirectedGraph) -> List[newNode]:
        counterList = {}
        listNodes = graph.getAllNodes()
        for n in listNodes:
            counterList[n] = 0
        for node in listNodes:
            adjList = node.adjList
            for n in adjList:
                counterList[n] += 1
        queue = []
        for node in counterList:
            if counterList[node] == 0:
                queue.append(node)
                counterList[node] -= 1

        for item in queue:
            adjList = item.adjList
            for n in adjList:
                counterList[n] -= 1
            for node in counterList:
                if counterList[node] == 0:
                    queue.append(node)
                    counterList[node] -= 1
        return queue
   
    def mDFS(self, graph:DirectedGraph)-> List[newNode]: 
        listNodes = graph.getAllNodes()
        start = next(iter(listNodes))
        visited = set()
        stack = []
        for node in listNodes:
            if node not in visited:
                self.mDFSHelper(node, visited, stack)
        stack.reverse()
        return stack

    def mDFSHelper(self,n, visited, stack):   
        visited.add(n)
        listNodes = n.adjList
        for node in listNodes:
            if node not in visited:
                self.mDFSHelper(node, visited, stack)
        stack.append(n)

def main():
    
    def createRandomDAGIter(n:int)-> DirectedGraph:
        g = DirectedGraph()
        dicts = {}
        for i in range (n):
            flag = True
            while flag:
                nodeVal = random.randint(0, 100000)
                ans = dicts.get(nodeVal, "no")
                if ans == "no": #means nodeVal is orginal
                    dicts[nodeVal] = 1
                    flag = False
                    g.addNode(nodeVal)
        allNodes = g.getAllNodes()
        allNodesList = list(allNodes)
        for i in range(n):
            if i< (n-2):
                g.addUndirectedEdge(allNodesList[i], allNodesList[i+2])
        return g
    

if __name__ == "__main__":
    main()
