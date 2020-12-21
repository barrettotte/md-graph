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
            try:
                title = self.parse_frontmatter(content)['title']
            except AttributeError:
                title = base_name
            links = re.findall(RE_MDLINK, content, flags=re.MULTILINE)
        return MdFile(file_name, base_name, title, links)

    # parse all markdown files in directory
    def parse(self):
        uid = 1

        # parse each markdown file
        for subdir, dirs, files in os.walk(self.target_dir):
            for f in files:
                if f.endswith('md'):
                    path = os.path.join(subdir, f)

                    if not any(x for x in self.pages if x.file_path == path):
                        md = self.parse_md(path)
                        md.uid = uid
                        uid += 1
                        self.pages.append(md)

        # replace mdlinks with uids for future lookup
        for page in self.pages:
            uids = []

            for link in page.mdlinks:
                uid = list(filter(lambda x: x.base_name == link, self.pages))
                if len(uid) > 0:
                    uids.append(uid[0].uid)
            page.mdlinks = uids
        return self.pages
