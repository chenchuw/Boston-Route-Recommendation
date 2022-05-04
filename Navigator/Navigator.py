#!/usr/bin/python
import sys
import osmnx as ox
from geopy.geocoders import Nominatim
import time
from Graph import Graph
from print_result import print_result
from print_map import print_map

ox.config(log_console=True, use_cache=True)
# Get the ROADS and NODES of Back bay, Boston
# NODES(white dots) and EDGES(grey lines) are stored in Digraph
place_name = "Back Bay, Massachusetts, USA"
mode = 'drive'
optimizer = 'length'
graph = ox.graph_from_place(place_name,network_type=mode)

# Extract NODES and EDGES
nodes, edges = ox.graph_to_gdfs(graph, nodes=True, edges=True)

# Feed nodes and lengths to algorithms, algo returns bunch of nodes, iterate through the nodes 2 by 2
NodesAndLength = list(graph.edges(data='length'))

EdgeAndLength = {}

for i in NodesAndLength:
    EdgeAndLength[(i[0],i[1])] = i[2]

# === Takes USER INPUTS and Find the nearest nodes on current map ===
print("Thank you for using our Navigator (Back Bay, Boston, USA)!\n\
Please enter your starting location and destination location (in Back Bay, Boston)\n\
You can either enter a place's name or the place's coordinate in this format: latitude, longitude \n\
*Note that only places that could be found on OpenStreetMap can be used*\n\
Recommendations: first church in boston --> Atlantic fish back bay\n\
                 boston architectural college --> gibson house back bay")
startPoint = sys.argv[1]
destPoint = sys.argv[2]
# startPoint = input("Your starting location: ")
# destPoint = input("Your destination: ")
# startPoint = "first church in boston"
# destPoint = "Atlantic fish back bay"
# ===================================================================

if startPoint[0].isdigit():
    # Enter by HAND
    (start_lat,start_long) = tuple(float(x) for x in startPoint.split(",")) # (latitude, longitude)
    (end_lat,end_long) = tuple(float(x) for x in destPoint.split(",")) # (latitude, longitude)

    orig_node = ox.distance.nearest_nodes(graph, start_long, start_lat)
    dest_node = ox.distance.nearest_nodes(graph, end_long, end_lat)

else:
    # Enter by GEOCODE
    try:
        locator = Nominatim(user_agent = "myapp")
        startPoint = locator.geocode(startPoint)
        print(startPoint.latitude, startPoint.longitude)
    except:
        raise ValueError("Cannot find the place entered for departure.. \nPlease enter a place that exists in OpenStreetMap\n")
    try:
        destPoint = locator.geocode(destPoint)
        print(destPoint.latitude, destPoint.longitude)
    except:
        raise ValueError("Cannot find the place entered for destination.. \nPlease enter a place that exists in OpenStreetMap\n")
        
    (start_long, start_lat) = (startPoint.longitude, startPoint.latitude)
    (end_long, end_lat) = (destPoint.longitude, destPoint.latitude)

    orig_node = ox.distance.nearest_nodes(graph, startPoint.longitude, startPoint.latitude)
    dest_node = ox.distance.nearest_nodes(graph, destPoint.longitude, destPoint.latitude)

print(orig_node)
print(dest_node)


dij_start_time = time.time()

g = Graph(nodes.shape[0], list(nodes.index))
for t in NodesAndLength:
    g.add_edge(t[0], t[1], t[2])
    
D, pre_nodes1 = g.dijkstra(orig_node)
dij_path, dij_length = print_result(pre_nodes1, D, start_node=orig_node, target_node=dest_node)

dij_path.reverse()
dij_length

dij_end_time = time.time()

dij_runtime = dij_end_time - dij_start_time

# Bellman-Ford Algorithm

bell_start_time = time.time()

g = Graph(nodes.shape[0], list(nodes.index))
for t in NodesAndLength:
    g.add_edge(t[0], t[1], t[2])

D, pre_nodes2 = g.bellman_ford(orig_node)
bell_path, bell_length = print_result(pre_nodes2, D, start_node=orig_node, target_node=dest_node)

bell_path.reverse()
bell_length

bell_end_time = time.time()

bell_runtime = bell_end_time - bell_start_time

# Astar Algorithm

astar_start_time = time.time()

g = Graph(nodes.shape[0], list(nodes.index))
for t in NodesAndLength:
    g.add_edge(t[0], t[1], t[2])
    
astar_path = g.a_star_algorithm(orig_node, dest_node, graph)
astar_path.reverse()
# Convert float to integer
for i in range(0,len(astar_path)):
    astar_path[i] = int(astar_path[i])
astar_path

# Computer length of Astar's path

astar_length = 0

for i in range(len(astar_path)-1):
    subEdge = (astar_path[i],astar_path[i+1])
    astar_length += EdgeAndLength[subEdge]
    
astar_length = "{:.2f}".format(astar_length)

astar_end_time = time.time()

astar_runtime = astar_end_time - astar_start_time

# Plot the shortest route on Openstreet Map

dijkstra_map = ox.plot_route_folium(graph, dij_path, popup_attribute="length", weight=10, color='lightblue')
bellman_map = ox.plot_route_folium(graph, bell_path, popup_attribute="length", weight=10, color='purple')
astar_map = ox.plot_route_folium(graph, astar_path, popup_attribute="length", weight=10, color='grey')

print_map(dijkstra_map, bellman_map, astar_map, start_lat, start_long, end_lat, end_long, 
dij_length,bell_length,astar_length, dij_runtime,bell_runtime,astar_runtime)


