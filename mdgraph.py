# parse through markdown files and build link dictionary

import os, json
from mdparser import MdParser

target_dir = 'example'

parser = MdParser(target_dir)
pages = parser.parse()

with open(os.path.join(target_dir, 'mdlinks.json'), 'w+') as f:
    f.write(json.dumps(pages, indent=2, default=lambda x: x.__dict__))
