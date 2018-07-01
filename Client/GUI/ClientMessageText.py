import tkinter


class ClientText:
    def __init__(self, parent):
        self.parent = parent

        self.text = tkinter.Text(self.parent)

    def insert(self, message):
        self.text.insert(tkinter.END, message + "\n")

    def get_tkinter_text(self):
        return self.text
