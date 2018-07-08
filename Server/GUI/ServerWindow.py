from tkinter import CENTER
from Server.GUI.ServerStop import ServerStop


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


class ServerWindow:
    def __init__(self, root, server):
        self.root = root
        root.protocol("WM_DELETE_WINDOW", self.on_closing)
        root.title("Server")
        center(root)

        self.stop_button = ServerStop(root, server)
        self.stop_button.get_tkinter_button().place(relx=0.5, rely=0.5, anchor=CENTER)

    def on_closing(self):
        self.stop_button.stop()
