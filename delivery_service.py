
import sys
from graph import Graph, Vertex
from priority_queue import PriorityQueue

class DeliveryService:
    def __init__(self) -> None:
        """
        Constructor of the Delivery Service class
        """
        self.city_map = Graph()
        self.MST = Graph()
        self.path_elements = []

    def buildMap(self, filename: str) -> None:

        city_graph = Graph() #creates new graph object
        file1 = open(filename,'r') #opens file and reads
        lines = file1.readlines()

        for line in lines:
            items = line.strip().split("|")
            
            #turns the text file items into integer parameters
            node_a = int(items[0])
            node_b = int(items[1])
            cost = int(items[2])
           
            #connects the vertex objects into a graph with bidirectional paths 
            if len(items) == 3:
                city_graph.addEdge(node_a,node_b,cost) #first direction
                city_graph.addEdge(node_b,node_a,cost) #second direction


            self.city_map = city_graph



    def isWithinServiceRange(self, restaurant: int, user: int, threshold: int) -> bool:

        #intial check to see if the user exists
        if self.city_map.getVertex(user) is None:
            return False
        
        #reset values to start 
        for vert in self.city_map:
            vert.setPred(None)
            vert.setDistance(float("inf"))

        
        #execute Dijkstras between resturant and user
        self.dijkstra(restaurant,self.city_map)

        #gets the distance from user node to resturant
        user_vert = self.city_map.getVertex(user)
        distance = user_vert.getDistance()
        
        
        #returns boolean comparing distance with threshold
        return distance < threshold
        

    def dijkstra(self,start,map):
        
        
        pq = PriorityQueue()
        start_vertex = map.getVertex(start)
        start_vertex.setDistance(0)
        pq.buildHeap([(v.getDistance(),v) for v in map])
        while not pq.isEmpty():
            currentVert = pq.delMin()

            
            for nextVert in currentVert.getConnections():
                newDist = currentVert.getDistance() \
                        + currentVert.getWeight(nextVert)
                if newDist < nextVert.getDistance():
                    nextVert.setDistance( newDist )
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert,newDist)
        




    def buildMST(self, restaurant: int) -> bool:
        """
        """
        self.MST = self.prim(restaurant)
        


    def prim(self,start):
        pq = PriorityQueue()
        mst = Graph()
        start = self.city_map.getVertex(start)
        for v in self.city_map:
            v.setDistance(sys.maxsize)
            v.setPred(None)
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(),v) for v in self.city_map])
        while not pq.isEmpty():
            currentVert = pq.delMin()

            #add vertext to MST 
            mst.addVertex(currentVert.getId())
            
            #connect the edges to the predecessor, if it exists
            if currentVert.getPred():
                vert1 = currentVert.getId()
                vert2 = currentVert.getPred().getId()
                weight = currentVert.getWeight(currentVert.getPred())
                mst.addEdge(vert1,vert2,weight)


            for nextVert in currentVert.getConnections():
                newCost = currentVert.getWeight(nextVert)
                if nextVert in pq and newCost<nextVert.getDistance():
                    nextVert.setPred(currentVert)
                    nextVert.setDistance(newCost)
                    pq.decreaseKey(nextVert,newCost)   
        #return the MST 
        return mst



    def minimalDeliveryTime(self, restaurant: int, user: int) -> int:
        """

        """
        #intial check to see if the nodes exist
        if self.MST.getVertex(user) is None:
            return -1
        if self.MST.getVertex(restaurant) is None:
            return -1
        
        #reset values to start 
        for vert in self.MST:
            vert.setPred(None)
            vert.setDistance(float("inf"))
        
        self.dijkstra(restaurant,self.MST)
        
        #gets the distance from user node to resturant
        user_vert = self.MST.getVertex(user)
        delivery_time = user_vert.getDistance()
        #print(delivery_time, "D-Time")
        return delivery_time




        

    def findDeliveryPath(self, restaurant: int, user: int) -> str:

        
        
        #intial check to see if the nodes exist
        if self.city_map.getVertex(user) is None:
            return "INVALID"
        if self.city_map.getVertex(restaurant) is None:
            return "INVALID"
        
        if self.isWithinServiceRange(restaurant,user,float("inf")):
        
            #reset values to start 
            for vert in self.city_map:
                vert.setPred(None)
                vert.setDistance(float("inf"))

            
            #execute Dijkstras between resturant and user
            self.dijkstra(restaurant,self.city_map)

            #retrace path and return list
            path_elements = []
            total_distance = 0

            current = self.city_map.getVertex(user)
            while current is not None:
                path_elements.append(current.getId())
                #gets the weight
                if current.getPred():
                    weight = current.getWeight(current.getPred())
                    total_distance += weight
                current = current.getPred()

            #print(path_elements, "FFFF PATH")

            vertex_path = path_elements
        
            #reverses the list
            vertex_path.reverse()
        

            path_str = ""
            for node in vertex_path:
                path_str += str(node) + "->"
            path_str = path_str.strip("->")
            return path_str + f" ({total_distance})"
        return "INVALID"

        





    def findDeliveryPathWithDelay(self, restaurant: int, user: int, delay_info: dict[int, int]) -> str:
        """

        :param restaurant:
        :param user:
        :param delay_info:
        :return:
        """

        
        
         #intial check to see if the nodes exist
        if self.city_map.getVertex(user) is None:
            return "INVALID"
        if self.city_map.getVertex(restaurant) is None:
            return "INVALID"
        
        if self.isWithinServiceRange(restaurant,user,float("inf")):
        
            #reset values to start 
            for vert in self.city_map:
                vert.setPred(None)
                vert.setDistance(float("inf"))

            
            #execute Dijkstras between resturant and user
            self.dijkstra(restaurant,self.city_map)
            #print(self.path_elements, "DIJ PATH")

            #retrace path and return list
            path_elements = []
            total_distance = 0

            current = self.city_map.getVertex(user)
            while current is not None:
                path_elements.append(current.getId())
                #gets the weight
                if current.getPred():
                    weight = current.getWeight(current.getPred())
                    total_distance += weight
                    
                    delay = delay_info.get(current.getId(), 0)
                    total_distance += delay
                current = current.getPred()

            #print(path_elements, "FFFF PATH")

            vertex_path = path_elements
        
            #reverses the list
            vertex_path.reverse()
            #print("final vertex path",vertex_path)
            #print(vertex_path, "THE PATH")

            path_str = ""
            #z = str(len(vertex_path))
            #distance = 0
            for node in vertex_path:
                path_str += str(node) + "->"
            #print(path_str,"PATH FINAL")
            path_str = path_str.strip("->")
            return path_str + f" ({total_distance})"
        return "INVALID"
        

    
    @staticmethod
    def nodeEdgeWeight(v):
        return sum([w for w in v.connectedTo.values()])

    @staticmethod
    def totalEdgeWeight(g):
        return sum([DeliveryService.nodeEdgeWeight(v) for v in g]) // 2

    @staticmethod
    def checkMST(g):
        for v in g:
            v.color = 'white'

        for v in g:
            if v.color == 'white' and not DeliveryService.DFS(g, v):
                return 'Your MST contains circles'
        return 'MST'

    @staticmethod
    def DFS(g, v):
        v.color = 'gray'
        for nextVertex in v.getConnections():
            if nextVertex.color == 'white':
                if not DeliveryService.DFS(g, nextVertex):
                    return False
            elif nextVertex.color == 'black':
                return False
        v.color = 'black'

        return True


