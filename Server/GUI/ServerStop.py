import tkinter as tk
from tkinter import messagebox
import sys


class ServerStop:
    def __init__(self, parent, server):
        self.parent = parent
        self.server = server

        self.stop_button = tk.Button(parent, text="Terminate", command=self.stop)

    def stop(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.server.close()
            self.server.s.close()
            self.parent.destroy()
            sys.exit()

    def get_tkinter_button(self):
        return self.stop_button
