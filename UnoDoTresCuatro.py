import random
from typing import Set, Dict

class newNode:
    def __init__(self, nodeVal):
        self.val = nodeVal
        self.adjList = {}

class WeightedGraph:
    def __init__(self):
        self.listVertex = set() 
    def addNode(self, nodeVal:str)-> None:
        N = newNode(nodeVal)
        self.listVertex.add(N)
    def addUndirectedEdge(self, first:newNode, second:newNode, weight:int) -> None:
        first.adjList[second] = weight
    def removeUndirectedEdge(self, first:newNode, second:newNode) -> None:
        del first.adjList[second]
    def getAllNodes(self)-> Set[newNode]:
        return self.listVertex

def main():

    def createRandomCompleteWeightedGraph(n:int) -> WeightedGraph:
        weightedGraph = WeightedGraph()
        dicts = {}
        for i in range (n):
            weightedGraph.addNode(i)
        allNodes = weightedGraph.getAllNodes()
        for node1 in allNodes:
            for node2 in allNodes:
                weightVal = random.randint(0, 10)
                if node1 != node2:
                    weightedGraph.addUndirectedEdge(node1, node2,weightVal) #creates a edge between every node and every other node
        return weightedGraph

    def createLinkedList (n:int) -> WeightedGraph:
        weightedGraph = WeightedGraph()
        node1Val = 0
        weightedGraph.addNode(node1Val)
        for i in range (1,n):
            node2Val = i
            weightedGraph.addNode(node2Val)
            allNodes = weightedGraph.getAllNodes()
            for node in allNodes:
                if node.val == node1Val:
                    Node1 = node
                if node.val == node2Val:
                    Node2 = node
            weightedGraph.addUndirectedEdge(Node1, Node2, 1)
            node1Val = node2Val
        return weightedGraph

    def dijkstras (start, g:newNode) -> Dict[newNode, int]:
        listNodes = g.getAllNodes()
        NumNodesGraph = len(listNodes)
        visited = set()
        distancedict = {}
        parentDict = {}
        distancedict[start] = 0
        parentDict[start] = None
        curr = start
        while len(visited) != NumNodesGraph:
            adjlist = curr.adjList
            for neighbor in adjlist:
                if neighbor not in visited: 
                    if distancedict.get(neighbor) == None: 
                        distancedict[neighbor] = distancedict[curr] + adjlist[neighbor]
                        parentDict[neighbor] = curr
                    else:
                        if (distancedict[curr] + adjlist[neighbor]) < distancedict[neighbor]:
                            distancedict[neighbor] = distancedict[curr] + adjlist[neighbor]
                            parentDict[neighbor] = curr
            visited.add(curr)
            min_ = float('inf')
            for node in distancedict:
                if node not in visited:
                    if distancedict[node] < min_:
                        min_ = distancedict[node]
                        curr = node
        return distancedict
    

if __name__ == "__main__":
    main()
