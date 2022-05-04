from geopy.distance import geodesic
from queue import PriorityQueue
import queue
import numpy as np

class Graph:
    def __init__(self, num_of_vertices, node_list):
        self.v = num_of_vertices
        self.visited = []
        self.graph = []
        self.node_list = node_list # list of all the nodes
        
    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])
    
    def h(self, lat1, lon1, lat2, lon2):
        '''
        TO DO:
        This is to calculate the heuristic distance
        '''
        distance = geodesic((lat1,lon1), (lat2,lon2)).m
        return distance
    
    def get_neighbors(self, n):
        '''
        TO DO: To get the neighbors and weights of node n
        '''
        neighbors_list = []
        reshape_graph = np.array(self.graph).reshape(-1, 3)
        # if n is at the first column
        for array in reshape_graph:
            if n in array[:-2]:
                array = np.delete(array, np.where(array == n))
                neighbors_list.append(array)
        
        return neighbors_list
    
    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in self.node_list}
        D[start_vertex] = 0
        
        pre_nodes = {}
    
        pq = PriorityQueue()
        pq.put((0, start_vertex))
    
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)
    
            for node in self.node_list:
                for edge in self.graph:
                    if current_vertex == edge[0] and node == edge[1]:
                        distance = edge[2]
                        if node not in self.visited:
                            old_cost = D[node]
                            new_cost = D[current_vertex] + distance
                            if new_cost < old_cost:
                                pq.put((new_cost, node))
                                D[node] = new_cost

                                pre_nodes[node] = current_vertex
        return D, pre_nodes
    
    def bellman_ford(self, src):
        q = queue.Queue()
        
        inqueue = {v:False for v in self.node_list}
        inqueue[src] = True
        
        distance = {v:float('inf') for v in self.node_list}
        distance[src] = 0
        
        q.put(src)
        
        pre_nodes = {}
        
        while(q.empty() != True):
            node = q.get()
            for edge in self.graph:
                if node == edge[0]:
                    end_node = edge[1]
                    weight = edge[2]
                    if distance[end_node] > distance[node] + weight:
                        distance[end_node] = distance[node] + weight
                        pre_nodes[end_node] = node
                        
                        if inqueue[end_node] == False:
                            q.put(end_node)
                            inqueue[end_node] == True
                            
        return distance, pre_nodes
    
    def a_star_algorithm(self, start, stop, graph):
        # In this open_lst is a list of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])
        
        lat1 = graph.nodes[start]['y']
        lon1 = graph.nodes[start]['x']
 
        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                lat2 = graph.nodes[v]['y']
                lon2 = graph.nodes[v]['x']
                if n == None or poo[v] + self.h(lat1, lon1, lat2, lon2) < poo[n] + self.h(lat1, lon1, lat2n, lon2n):
                    n = v
                    lat2n = graph.nodes[v]['y']
                    lon2n = graph.nodes[v]['x']
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                print('Path found: {}'.format(reconst_path))
                return reconst_path
 
            # for all the neighbors of the current node do
            neighbor_list = self.get_neighbors(n)
            for array in neighbor_list:
                m, weight = array[0], array[1]
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None