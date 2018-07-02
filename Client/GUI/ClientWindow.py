from Client.GUI import ClientEntry, ClientSubmit, ClientMessageText
from tkinter import messagebox
import sys


class ClientWindow:
    def __init__(self, root, client):
        self.root = root
        self.client = client

        root.title(client.username)
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

        text = ClientMessageText.ClientText(root)
        client.set_message_text(text)

        entry = ClientEntry.ClientEntry(root)
        button = ClientSubmit.SubmitButton(root, entry, client, text)

        text.get_tkinter_text().grid(row=0, column=0)
        entry.get_tkinter_entry().grid(row=1, column=0)
        button.get_tkinter_button().grid(row=2, column=0)

        entry.get_tkinter_entry().focus_force()
        entry.get_tkinter_entry().bind("<Return>", lambda e: button.submit())

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.client.close()
            self.root.destroy()
            sys.exit()
