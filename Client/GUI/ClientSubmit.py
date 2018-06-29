import tkinter


class SubmitButton:
    def __init__(self, parent, entry, client):
        self.parent = parent
        self.entry = entry
        self.client = client

        self.submit_button = tkinter.Button(parent, text="Submit", command=self.submit)

    def submit(self):
        self.client.send(self.entry.get_text())

    def get_tkinter_button(self):
        return self.submit_button
