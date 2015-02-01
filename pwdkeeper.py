import os
import tkinter as tk
import pydes as pydes


class PwdDocumentItem:

    def __init__(self):
        pass


class PwdDocument:

    def __init__(self):
        self._pwdItems = []


class EditItemDialog(tk.Toplevel):

    def __init__(self, readonly):
        tk.Toplevel.__init__(self)
        self._readonly = readonly
        self._keyValue = tk.StringVar()
        self._userNameValue = tk.StringVar()
        self._pwdValue = tk.StringVar()
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self._keyLabel = tk.Label(self, text="Key")
        self._keyLabel.grid(row=0, column=0)
        self._keyInput = tk.Entry(self, textvariable=self._keyValue)
        self._keyInput.grid(row=0, column=1)

        self._userNameLabel = tk.Label(self, text="User Name")
        self._userNameLabel.grid(row=1, column=0)
        self._userNameInput = tk.Entry(self, textvariable=self._userNameValue)
        self._userNameInput.grid(row=1, column=1)

        self._pwdLabel = tk.Label(self, text="password")
        self._pwdLabel.grid(row=2, column=0)
        self._pwdInput = tk.Entry(self, textvariable=self._pwdValue)
        self._pwdInput.grid(row=2, column=1)

        self._okButton = tk.Button(self, text="Ok", command=self.applyChange)
        self._okButton.grid(row=3, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    def applyChange(self):
        if (not self._readonly):
            pass
        self.destroy()


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self._root = master
        self._document = None
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.createMenu()
        self.createList()

    def createMenu(self):
        self._menu = tk.Menu(self._root)
        self._root["menu"] = self._menu
        self._fileMenu = tk.Menu(self._menu, tearoff=0)
        self._fileMenu.add_command(label="New", command=self.newDocument)
        self._fileMenu.add_command(label="Open", command=self.openDocument)
        self._fileMenu.add_command(label="Save", command=self.saveDocument)
        self._menu.add_cascade(label="File", menu=self._fileMenu)
        self._itemMenu = tk.Menu(self._menu, tearoff=0)
        self._itemMenu.add_command(label="New Item", command=self.newItem)
        self._itemMenu.add_command(label="Open Item", command=self.openItem)
        self._itemMenu.add_command(label="Delete Item", command=self.deleteItem)
        self._menu.add_cascade(label="Item", menu=self._itemMenu)

    def createList(self):
        self._itemList = tk.Listbox(self._root)
        self._itemList.pack()

    def newDocument(self):
        pass

    def openDocument(self):
        pass

    def saveDocument(self):
        pass

    def newItem(self):
        pass

    def deleteItem(self):
        pass

    def openItem(self):
        openItemDialog = EditItemDialog(True)


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
