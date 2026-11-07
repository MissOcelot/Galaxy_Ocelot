from pyvis.network import Network
import networkx as nx
import os

PLACEHOLDER = "icons/placeholder.png"
raw_connections = {
    "Colorzip": ["Mycil","Siouxwu","Anglais","Sandy","Johnny","Mazy","Mika","Harley","Jacks","Maybell"],
    "Mycil": ["Colorzip","Siouxwu","Smear","Anglais","Duskstep","Hex","Honeydew"],
    "Siouxwu": ["Mycil","Colorzip"],
    "Duskstep": ["Mycil","Mintie","Smear"],
    "Smear": ["Mycil","Duskstep","Mintie"],
    "Mintie": ["Smear","Duskstep"],
    "Hex": ["Mycil","Honeydew"],
    "Honeydew": ["Mycil","Hex"],
    "Lightning": [],
    "Ecosia": ["Evosia"],
    "Evosia": ["Ecosia"],
    "Anglais": ["Colorzip","Mycil"],
    "Celise": ["Damore"],
    "Damore": ["Celise"],
    "Calie": ["Esme","Miyoni"],
    "Esme": ["Calie","Miyoni"],
    "Qiztote": [],
    "Whispersong": ["Mika","Johnny","Hazelmist","Embertail"],
    "Hazelmist": ["Embertail","Whispersong"],
    "Embertail": ["Hazelmist","Whispersong"],
    "Johnny": ["Mazy","Colorzip","Mika","Harley","Whispersong","Maybell"],
    "Mazy": ["Johnny","Colorzip","Mika","Harley","Jacks"],
    "Jacks": ["Mazy","Harley","Mika","Max","Colorzip"],
    "Mika": ["Colorzip","Harley","Mazy","Johnny","Jacks","Whispersong","Max","Maybell"],
    "Harley": ["Colorzip","Mika","Mazy","Johnny","Jacks","Max"],
    "Sandy": ["Colorzip"],
    "Max": ["Jacks","Mika","Harley"],
    "Miyoni": ["Calie","Esme"],
    "Maybell": ["Colorzip","Johnny","Mika"]
}


def normalize(name):
    return name.strip().title()

connections = {}
for char, links in raw_connections.items():
    char = normalize(char)
    connections.setdefault(char, [])
    for link in links:
        link = normalize(link)
        connections[char].append(link)
        connections.setdefault(link, [])
        if char not in connections[link]:
            connections[link].append(char)

G = nx.Graph()
for char in connections.keys():
    icon_path = f"icons/{char.lower()}.png"
    if not os.path.exists(icon_path):
        icon_path = PLACEHOLDER
    G.add_node(
        char,
        label=char,
        shape="image",
        image=icon_path,
        size=45  
    )

for char, links in connections.items():
    for link in links:
        G.add_edge(char, link, color="#c057e6")  
    

net = Network(
    height="900px",
    width="100%",
    bgcolor="#222222",
    font_color="white"
)

net.from_nx(G)
for e in net.edges:
        e['color'] = "#dc92f7"  
        e['width'] = 3  

for node in net.nodes:
    node['size'] = 45  


net.set_options("""
{
  "physics": {
    "barnesHut": {
      "gravitationalConstant": -2000,
      "centralGravity": 0.3,
      "springLength": 180,
      "springConstant": 0.05,
      "damping": 0.3
    },
    "minVelocity": 0.75,
    "stabilization": {"iterations": 300}
  },
  "nodes": {
    "physics": true
  }
}
""")
net.write_html("index.html")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()


with open("htmlstuff.txt", "r", encoding="utf-8") as f:
    extra = f.read()


html = html.replace("</body>", extra + "\n</body>")


with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Graph built with custom HTML injected.")
net.save_graph("character_map.html")
print("Map created: character_map.html")