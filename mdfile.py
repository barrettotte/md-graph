
class MdFile():

    def __init__(self, file_path, title, mdlinks):
        self.file_path = file_path
        self.title = title
        self.mdlinks = mdlinks

    def __str__(self):
        return f'{self.file_path} => {self.title}, {self.mdlinks}'
