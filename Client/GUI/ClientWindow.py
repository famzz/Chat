from Client.GUI import ClientEntry, ClientSubmit, ClientMessageText


class ClientWindow:
    def __init__(self, root, client):
        text = ClientMessageText.ClientText(root)
        entry = ClientEntry.ClientEntry(root)
        button = ClientSubmit.SubmitButton(root, entry, client)

        text.get_tkinter_text().grid(row=0, column=0)
        entry.get_tkinter_entry().grid(row=1, column=0)
        button.get_tkinter_button().grid(row=2, column=0)
