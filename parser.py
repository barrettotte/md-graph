# parse through markdown files and build link dictionary

import os, re, json, yaml
from mdfile import MdFile

rootdir = 'example'
re_mdlink = r'(?<=\[{2})(.*?)(?=\]{2})'      # + multiline
re_mdtitle = r'(?<=(\-{3}))(.*?)(?=(\-{3}))' # + multiline, case insensitive


# parse markdown front matter (yaml)
def parse_frontmatter(content):
    fm = re.search(re_mdtitle, content, flags=re.MULTILINE+re.IGNORECASE+re.DOTALL).group(0)
    return yaml.safe_load(fm)

# use regex to find markdown links and title (front matter)
def parse_md(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
        links = re.findall(re_mdlink, content, flags=re.MULTILINE)
        title = parse_frontmatter(content)['title']

    md = MdFile(file_name, title, links)
    return md


pages = []
for subdir, dirs, files in os.walk(rootdir):
    for f in files:
        if f.endswith('md'):
            path = os.path.join(subdir, f)
    
            if not any(x for x in pages if x.file_path == path):
                pages.append(parse_md(path))

print(json.dumps(pages, indent=2, default=lambda x: x.__dict__))