class Document:
    def __init__(self):
        self.content = ""
        self.file_path = None
        self.is_modified = False

    def save(self, file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(self.content)

        self.file_path = file_path
        self.is_modified = False

    def load(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            self.content = file.read()

        self.file_path = file_path
        self.is_modified = False
