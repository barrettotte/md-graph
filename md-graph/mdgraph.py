# parse through markdown files and build link dictionary

import sys, os, json
from mdparser import MdParser
from netgraph import GraphOptions, GraphBuilder


# if path does not exist, fatal exit
def assert_exists(file_path):
    if not os.path.exists(file_path):
        print(f'{file_path} could not be found.')
        exit(1)

# read config json from file path
def read_config(file_path):
    assert_exists(file_path)
    with open(file_path, 'r') as f:
        return json.load(f)

# output md data to json (debug util)
def mdlinks_json(pages, target_dir):
    assert_exists(target_dir)
    with open(os.path.join(target_dir, 'mdlinks.json'), 'w+') as f:
        f.write(json.dumps(pages, indent=2, default=lambda x: x.__dict__))

# load config into GraphOptions obj
def load_graph_opts(config):
    return GraphOptions(config['width'], config['height'], config['heading'],
                        config['bgcolor'], config['font_color'] )

# load pyvis options from file
def load_pyvis_opts(file_path):
    assert_exists(file_path)
    with open(file_path, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print('usage: mdgraph.py CONFIG_PATH')
        exit(1)

    # load config file
    config_path = sys.argv[1]
    assert_exists(config_path)
    config = read_config(config_path)

    target_dir = os.path.abspath(config['md_dir'])
    assert_exists(target_dir)

    # parse markdown files and build relationships
    parser = MdParser(target_dir)
    pages = parser.parse()

    # load network graph options and build graph
    pyvis_opts = load_pyvis_opts(os.path.join(target_dir, 'pyvis_opts.js'))
    graph_opts = load_graph_opts(config['graph_opts'])
    builder = GraphBuilder(pyvis_opts, graph_opts, os.path.join(target_dir, 'mdgraph.html'))
    builder.build(pages) # saved to config['graph_out']

if __name__ == "__main__": main()