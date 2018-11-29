import folium 
import os
import json

# Create Map Object
m = folium.Map(location=[19.113292, 72.841905], zoom_start=12)

# Global Tooltip
tooltip = 'Click For More Info'

# Create custom marker icon
logoIcon = folium.features.CustomIcon('http://in.bmscdn.com/webin/v3-static/bms-logo.png', icon_size=(50,50))

# Vega data
vis = os.path.join('data', 'vis.json')

# Create Markers
folium.Marker(
    [19.11042355, 72.84443585], 
    popup='<strong>Location One</strong>',
    tooltip=tooltip,
    icon=folium.Icon(icon='cloud', color='purple')).add_to(m),

folium.Marker(
    [19.10761196, 72.84250522], 
    popup='<strong>Location Two</strong>',
    tooltip=tooltip,
    icon=folium.Icon(icon='leaf', color='green')).add_to(m),

folium.Marker(
    [19.113292, 72.841905], 
    popup='<strong>Location Three</strong>',
    tooltip=tooltip,
    icon=logoIcon).add_to(m),

folium.Marker(
    [19.07472172, 72.83828267], 
    popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m)

# Circle Marker
folium.CircleMarker(
    location=[19.06992927, 72.84346019],
    radius=50,
    popup='My birth place',
    color='#428bca',
    fill=True,
    fill_color='428bca'
).add_to(m)

m.save('map.html')