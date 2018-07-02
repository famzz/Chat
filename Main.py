import tkinter
import Client.GUI.ClientWindow
import Client.Client

if "__main__" in __name__:
    client = Client.Client.Client()
    client.start()

    client_window = tkinter.Tk()
    Client.GUI.ClientWindow.ClientWindow(client_window, client)
    client.get_pending_messages()
    client_window.mainloop()
