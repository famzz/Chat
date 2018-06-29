import tkinter


class ClientEntry:
    def __init__(self, parent):
        self.parent = parent

        self.entry = tkinter.Entry(parent)

    def get_text(self):
        return self.entry.get()

    def get_tkinter_entry(self):
        return self.entry
