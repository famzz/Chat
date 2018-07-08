from tkinter import CENTER

from Server.GUI.ServerStop import ServerStop


class ServerWindow:
    def __init__(self, root, server):
        self.root = root

        stop_button = ServerStop(root, server)
        stop_button.get_tkinter_button().place(relx=0.5, rely=0.5, anchor=CENTER)
