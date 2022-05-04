# Boston University SPRG2021 EC504 - Advanced Data Structures - Final Project
Team member: Chuwei Chen, Shuhao Hu, Zhaowen Zhou, Zhaozhong Qi

We used python packet OSMnx (Credit to Geoff Boeing) for this project.
Please follow the following instructions to run the project:

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
pip install geopy
pip install scikit-learn
pip install folium
pip install numpy
pip install matplotlib
```

=== Now, run Navigator.py ===

***Note that within this project, all locations has to be located in Back Bay, Boston, USA.***

There are two ways to interact with Navigator.py (Please strictly follow the format examples shown below):

1. Pass departure, destination points by latitude/longitude coordinate

```
python Navigator.py __coordinateOfDeparture__ __coordinateOfDestination__ 
```

Feel free to change __coordinateOfDeparture__ __coordinateOfDestination__ to your desired latitude/longitude coordinate.

For example:
```
python Navigator.py 42.3498704,-71.0804434 42.3512842,-71.0777077
```

2. Pass departure, destination points by name of the location:

```
python Navigator.py "__NameOfDeparture__" "__NameOfDestination__"
```

Again, you can change "__NameOfDeparture__" "__NameOfDestination__" to your desired location's name.

For example:
```
python Navigator.py "lolita back bay" "first church in boston"
```

When the program finished, maps with plotted shortest path are saved in current folder, please open it with your browswer to view the path and distances, etc. Thank you! :)

**Citation info**: Boeing, G. 2017. "[OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks](https://geoffboeing.com/publications/osmnx-complex-street-networks/)." *Computers, Environment and Urban Systems* 65, 126-139. doi:10.1016/j.compenvurbsys.2017.05.004
