import os, re, yaml
from mdfile import MdFile

RE_MDLINK = r'(?<=\[{2})(.*?)(?=\]{2})'   # [[link]]
RE_MDFM = r'(?<=(\-{3}))(.*?)(?=(\-{3}))' # front matter yaml

class MdParser():

    def __init__(self, target_dir):
        self.pages = []
        self.target_dir = target_dir

    # parse markdown front matter (yaml)
    def parse_frontmatter(self, content):
        flags = re.MULTILINE + re.IGNORECASE + re.DOTALL
        fm = re.search(RE_MDFM, content, flags=flags).group(0)
        return yaml.safe_load(fm)

    # grab all the information needed from the markdown file
    def parse_md(self, file_name):
        base_name = os.path.splitext(os.path.basename(file_name))[0]

        with open(file_name, 'r') as f:
            content = f.read()
            title = self.parse_frontmatter(content)['title']
            links = re.findall(RE_MDLINK, content, flags=re.MULTILINE)
        return MdFile(file_name, base_name, title, links)

    # parse all markdown files in directory
    def parse(self):

        # parse each markdown file
        for subdir, dirs, files in os.walk(self.target_dir):
            for f in files:
                if f.endswith('md'):
                    path = os.path.join(subdir, f)

                    if not any(x for x in self.pages if x.file_path == path):
                        self.pages.append(self.parse_md(path))

        # replace mdlinks with full paths (since now all markdown files are known)
        for page in self.pages:
            full_links = []

            for link in page.mdlinks:
                full_link = list(filter(lambda x: x.base_name == link, self.pages))
                if len(full_link) > 0:
                    full_links.append(full_link[0].file_path)
            page.mdlinks = full_links

        return self.pages
