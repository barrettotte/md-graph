#!/bin/bash

target_dir=example

python3 md-graph/mdgraph.py $target_dir/mdgraph_config.json

mv $target_dir/mdgraph.html docs/mdgraph.html