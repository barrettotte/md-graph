# parse through markdown files and build link dictionary

import os, json
import networkx as nx
from pyvis.network import Network
from mdparser import MdParser

target_dir = '/home/barrett/Programming/Repos/Notes/notes' #'example'

parser = MdParser(target_dir)
pages = parser.parse()

with open(os.path.join(target_dir, 'mdlinks.json'), 'w+') as f:
    f.write(json.dumps(pages, indent=2, default=lambda x: x.__dict__))

# nx_graph = nx.cycle_graph(10)

# nx_graph.nodes[1]['title'] = 'Number 1'
# nx_graph.nodes[1]['group'] = 1

# nx_graph.nodes[3]['title'] = 'I belong to a different group!'
# nx_graph.nodes[3]['group'] = 10


# nx_graph.add_node(20, size=20, title='couple', group=2)
# nx_graph.add_node(21, size=15, title='couple', group=2)
# nx_graph.add_edge(20, 21, weight=5)

# nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)

nx_graph = nx.Graph()

for page in pages:
    nx_graph.add_node(page.uid, label=page.title)
    for link_uid in page.mdlinks:
        nx_graph.add_edge(page.uid, link_uid)


net = Network(width="100%", height="80%", heading='md-graph', 
                bgcolor='#2e2e2e', font_color='#ffffff')


# net.show_buttons()

with open('pyviz.js', 'r') as f:
    net.set_options(f.read())


net.from_nx(nx_graph)

net.show("nx.html")
