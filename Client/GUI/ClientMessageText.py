import tkinter


class ClientText:
    def __init__(self, parent):
        self.parent = parent

        self.text = tkinter.Text(parent=self.parent)

    def insert(self, message):
        self.text.insert(tkinter.INSERT, "\n" + message)

    def get_tkinter_text(self):
        return self.text
