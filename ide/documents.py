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

    def clone(self):
        new_document = self.__class__()
        new_document.content = self.content
        new_document.file_path = None
        new_document.is_modified = True
        return new_document


class TextDocument(Document):
    pass


class MarkdownDocument(Document):
    pass


class DocumentCreator:
    def create_document(self):
        raise NotImplementedError


class TextDocumentCreator(DocumentCreator):
    def create_document(self):
        return TextDocument()


class MarkdownDocumentCreator(DocumentCreator):
    def create_document(self):
        return MarkdownDocument()
