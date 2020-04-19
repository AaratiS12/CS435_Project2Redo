import random
from typing import Set, List

class newNode:
    def __init__(self, nodeVal):
        self.val = nodeVal
        self.adjList = []

class Graph:
    def __init__(self):
        self.listVertex = set() 
   
    def addNode(self, nodeVal: str) -> None: 
        N = newNode(nodeVal)
        self.listVertex.add(N)

    def addUndirectedEdge(self, first:newNode, second:newNode) -> None: 
        first.adjList.append(second)
        second.adjList.append(first)

    def addUndirectedEdgeOneWay(self, first:newNode, second:newNode) -> None:
        first.adjList.append(second)

    def removeUndirectedEdge(self, first:newNode, second:newNode) -> None: 
        first.adjList.remove(second)
        second.adjList.remove(first)
     
    def getAllNodes(self) -> Set[int]: 
        return self.listVertex

class GraphSearch:

    def __init__(self):
        pass

    def DFSIter(self, start:newNode , end:newNode) -> List[int]:
        stack = []
        visited_list = []
        stack.append(start) #stack.push()
        visited_list.append(start)

        while stack: #checks that stack is not empty
            peek = stack[-1] #stack.peek()
            if peek == end:
                return visited_list
            adjNodes = peek.adjList
            notVisited = []

            for node in adjNodes:
                if node not in visited_list:
                    notVisited.append(node)
            if notVisited:
                stack.append(notVisited[0])
                visited_list.append(notVisited[0])
            else:
                stack.pop()
        return None
  
    def DFSHelper(self, node, visited, end):
        visited.append(node)
        if node == end:
            return visited
        listNodes = node.adjList
        while listNodes:
            notVisited = []
            for n in listNodes:
                if n not in visited:
                    notVisited.append(n)
            if notVisited:
                visited = self.DFSHelper(notVisited[0], visited, end)
                if visited[-1] == end:
                    return visited
            else:
                return visited

    def DFSRec(self, start:newNode , end:newNode) -> List[newNode]:
        visited = []
        visited = self.DFSHelper(start, visited, end)
        return visited
   
    def BFTIter(self, graph:Graph)-> List[newNode]:
        listNodes = graph.getAllNodes()
        start = next(iter(listNodes))
        queue = []
        visited_list = []
        queue.append(start)
        visited_list.append(start)
        while queue: #checks that queue is not empty
            element = queue[0] 
            adjNodes = element.adjList
            notVisited = []
            for node in adjNodes:
                if node not in visited_list:
                    notVisited.append(node)
            for node in notVisited:
                queue.append(node)
                visited_list.append(node)
            del queue[0]
        return visited_list

    def BFTHelper(self, node, visited, queue):
        listNodes = node.adjList
        notVisited = []
        for node in listNodes:
            if node not in visited:
                notVisited.append(node)
        for node in notVisited:
            visited.append(node)
            queue.append(node)
        del queue[0] #removes the head
        if queue:
            Node = queue[0]
            self.BFTHelper(Node, visited, queue)
        return visited

    def BFTRec(self, graph:Graph )-> List[newNode]:
        visited = []
        queue = []
        listNodes = graph.getAllNodes()
        start = next(iter(listNodes))
        visited.append(start)
        queue.append(start)
        visited = self.BFTHelper(start, visited, queue)
        return visited

def main():

    def createRandomUnweightedGraphIter (n:int)-> Graph:
        graph = Graph()
        dicts = {}
        for i in range (n):
            flag = True
            while flag:
                nodeVal = random.randint(0, 10)
                ans = dicts.get(nodeVal, "no")
                if ans == "no": #means nodeVal is orginal
                    dicts[nodeVal] = 1
                    flag = False
                    graph.addNode(nodeVal)
        allNodes = graph.getAllNodes()
        for node1 in allNodes:
            for node2 in allNodes:
                if node1 != node2:
                    graph.addUndirectedEdgeOneWay(node1, node2) #creates a edge between every node and every other node
        return graph

    def createLinkedList (n:int) -> Graph:
        graph = Graph()
        node1Val = 0
        dicts = {}
        dicts[node1Val] = 1
        graph.addNode(node1Val)
        for i in range (1,n):
            flag = True
            while flag:
                nodeVal2 = i
                ans = dicts.get(nodeVal2, "no")
                if ans == "no": #means nodeVal is orginal
                    dicts[nodeVal2] = 1
                    flag = False
                    graph.addNode(nodeVal2)
                    allNodes = graph.getAllNodes()
                    for node in allNodes:
                        if node.val == node1Val:
                            N1 = node
                        if node.val == nodeVal2:
                            N2 = node
                    graph.addUndirectedEdgeOneWay(N1, N2)
                    node1Val = nodeVal2
        return graph

    def BFTRecLinkedList (graph:Graph) -> List[newNode]:
        graph = createLinkedList(10000)
        Gs2 = GraphSearch()
        array_list = Gs2.BFTRec(graph)
        return array_list

    def BFTIterLinkedList (graph:Graph) -> List[newNode]:
        graph = createLinkedList(10000)
        Gs2 = GraphSearch()
        array_list = Gs2.BFTIter(graph)
        return array_list

if __name__ == "__main__":
    main()