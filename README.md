# Route Recommendation Application
Team member: Chuwei Chen, Shuhao Hu, Zhaowen Zhou, Zhaozhong Qi

## Boston University SPRG2021 EC504 - Advanced Data Structures - Final Project
With geographical data and shortest pathfinding algorithms, we created an application that can map out the routing paths between two places in real time. For the main idea of this project, diaparte shortest path algorithms has been approached by three different perspectives, they are respectively the classical Dijkstra's, Bell-Ford, and A* algorithms.

We used python packet OSMnx (Credit to Geoff Boeing!) for this project.

Please follow the following instructions (MacOS or Linux) to run the project:

=== Install our project Git repo ===

In terminal, enter:

```
git clone https://github.com/chenchuw/EC504-Final-Project.git
```

=== Install the OSMnx package ===

cd into the osmnx package folder

```
cd EC504-Final-Project/osmnx-main
```

Install the OSMnx package

```
pip install -e .
cd ..
```

=== Install other required packages ===
```
pip install geopy scikit-learn folium numpy matplotlib
```

=== Now, run Navigator.py ===

Enter our folder containing our source codes:

```
cd Navigator
```

***Note that within this project, all locations has to be located in Back Bay, Boston, USA.***

There are two ways to interact with Navigator.py (Please strictly follow the format examples shown below):

1. Pass departure, destination points by latitude/longitude coordinate

```
python Navigator.py __coordinateOfDeparture__ __coordinateOfDestination__ 
```

Feel free to change __coordinateOfDeparture__ __coordinateOfDestination__ to your desired latitude/longitude coordinate.

For example:
```
python Navigator.py 42.3467236,-71.0796355 42.3546324,-71.0764676
```

List of nodes (located in Back Bay, Boston) that you can play around with:

42.351513,-71.086995

42.350897,-71.077742

42.351478,-71.075600	

42.350843,-71.089478	

42.351919,-71.085492	

42.346796,-71.085049	

42.346233,-71.078573	

42.348102,-71.088705

42.347934,-71.078730	

42.347609,-71.079021	

2. Pass departure, destination points by name of the location:

```
python Navigator.py "__NameOfDeparture__" "__NameOfDestination__"
```

Again, you can change "__NameOfDeparture__" "__NameOfDestination__" to your desired location's name.

For example:
```
python Navigator.py "lolita back bay" "first church in boston"
```

When the program finished, maps with plotted shortest path are saved in current folder, please open it with your browswer or enter the following command to view the path and distances, etc. Thank you! :)

```
open astar_map.html | open bellman_map.html| open astar_map.html 
```

Sample output html files (Black mark as departure and Green mark as destination):

![Dijkstra_sampleOutput](https://github.com/chenchuw/EC504-Final-Project/blob/main/OutputSample.png?raw=true)

**Citation info**: Boeing, G. 2017. "[OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks](https://geoffboeing.com/publications/osmnx-complex-street-networks/)." *Computers, Environment and Urban Systems* 65, 126-139. doi:10.1016/j.compenvurbsys.2017.05.004
