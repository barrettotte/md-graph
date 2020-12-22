import os
import networkx as nx
from pyvis.network import Network
from mdfile import MdFile


class GraphOptions():
    
    def __init__(self, width, height, heading, bgcolor, font_color):
        self.width = width
        self.height = height
        self.heading = heading
        self.bgcolor = bgcolor
        self.font_color = font_color


class GraphBuilder():

    def __init__(self, pyvis_opts, graph_opts, graph_out):
        self.pyvis_opts = pyvis_opts  # js variable as raw string
        self.graph_opts = graph_opts  # GraphOptions obj
        self.graph_out = graph_out    # output path for graph as HTML

        self.net = Network( width=graph_opts.width, height=graph_opts.height, 
                            heading=graph_opts.heading, bgcolor=graph_opts.bgcolor, 
                            font_color=graph_opts.font_color )
        self.net.set_options(self.pyvis_opts)


    # build graph from parsed markdown pages
    def build(self, pages):
        nx_graph = nx.Graph()

        for page in pages:
            nx_graph.add_node(page.uid, label=page.title)
            for link_uid in page.mdlinks:
                nx_graph.add_edge(page.uid, link_uid)

        self.net.from_nx(nx_graph)
        # self.net.show(graph_out) # show graph in browser

        # save network graph as HTML
        self.net.save_graph(self.graph_out)
