import tkinter


class SubmitButton:
    def __init__(self, parent, entry, client, text):
        self.parent = parent
        self.entry = entry
        self.client = client
        self.text = text

        self.submit_button = tkinter.Button(parent, text="Submit", command=self.submit)

    def submit(self):
        self.client.send(self.entry.get_text())
        self.text.insert("Me: " + self.entry.get_text())
        self.entry.get_tkinter_entry().delete(0, 'end')

    def get_tkinter_button(self):
        return self.submit_button
