import folium

def print_map(dijkstra_map, bellman_map, astar_map, start_lat, start_long, end_lat, end_long, 
dij_length,bell_length,astar_length, dij_runtime,bell_runtime,astar_runtime):
    maps = [dijkstra_map,bellman_map,astar_map]

    for i in maps:
        folium.TileLayer('openstreetmap').add_to(i)
        folium.TileLayer('Stamen Terrain').add_to(i)
        folium.TileLayer('Stamen Toner').add_to(i)
        folium.TileLayer('Stamen Water Color').add_to(i)
        folium.TileLayer('cartodbpositron').add_to(i)
        folium.TileLayer('cartodbdark_matter').add_to(i)
        folium.LayerControl().add_to(i)

        # Marker class only accepts coordinates in tuple form
        start_marker = folium.Marker(
                    location = (start_lat,start_long),
                    popup = "Departure",
                    icon = folium.Icon(color='black'))
        end_marker = folium.Marker(
                    location = (end_lat,end_long),
                    popup = "Destination",
                    icon = folium.Icon(color='green'))
        # add the circle marker to the map
        start_marker.add_to(i)
        end_marker.add_to(i)

    mapNames = ["Dijkstra","Bellman-Ford","A*"]
    pathLengths = [dij_length,bell_length,astar_length]
    algoruntimes = [dij_runtime,bell_runtime,astar_runtime]

    for i in range(len(mapNames)):
        # Add title
        text = "Shortest path calculated with "+mapNames[i]+" algorithm<br>Total distance = "+str(pathLengths[i])+" meters & Runtime = " + str(algoruntimes[i])+" sec"
        title_html = '''
                    <h3 align="center" style="font-size:28px"><b>{}</b></h3>
                    '''.format(text)  
        maps[i].get_root().html.add_child(folium.Element(title_html))

    # Save the output map as html file
    dijkstra_map.save("./dijkstra_map.html")
    bellman_map.save("./bellman_map.html")
    astar_map.save("./astar_map.html")

    print("\n=========================\nMaps with plotted shortest path are stored \
in current folder as html files, please open it with your browswer to view the path :)\n=== \
Program finished ===")
