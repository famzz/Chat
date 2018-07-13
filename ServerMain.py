import Server.Server
import tkinter as tk
import Server.GUI.ServerWindow


if "__main__" in __name__:
    server = Server.Server.Server()

    root = tk.Tk()
    Server.GUI.ServerWindow.ServerWindow(root, server)
    root.mainloop()
