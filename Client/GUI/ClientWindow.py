from Client.GUI import ClientEntry, ClientSubmit


class ClientWindow:
    def __init__(self, root, client):
        entry = ClientEntry.ClientEntry(root)
        button = ClientSubmit.SubmitButton(root, entry, client)

        entry.get_tkinter_entry().grid(row=0, column=0)
        button.get_tkinter_button().grid(row=1, column=0)
