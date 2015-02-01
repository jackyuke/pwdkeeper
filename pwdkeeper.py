import os
import tkinter as tk
import tkinter.filedialog as tkFileDialog
import pydes as pydes


class PwdDocumentItem:

    def __init__(self):
        self._userName = ""
        self._key = ""
        self._password = ""

    def getUserName(self):
        return self._userName

    def setUserName(self, userName):
        self._userName = userName

    def getKey(self):
        return self._key

    def setKey(self, key):
        self._key = key

    def getPassword(self):
        return self._password

    def setPassword(self, password):
        self._password = password


class PwdDocument:

    def __init__(self):
        self._pwdItems = []
        self._fileName = ""
        self._dirty = True

    def addItem(self, item):
        self._pwdItems.append(item)

    def readFile(self):
        self._dirty = False

    def saveFile(self):
        self._dirty = False

    def setFileName(self, fileName):
        self._fileName = fileName

    def getFileName(self):
        return self._fileName

    def isDirty(self):
        return self._dirty

    def getItems(self):
        return self._pwdItems


class EditItemDialog(tk.Toplevel):

    def __init__(self, readonly, pwdItem):
        tk.Toplevel.__init__(self)
        self._readonly = readonly
        self._keyValue = tk.StringVar(pwdItem.getKey())
        self._userNameValue = tk.StringVar(pwdItem.getUserName())
        self._pwdValue = tk.StringVar(pwdItem.getPassword())
        self._pwdItem = pwdItem
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
            self._pwdItem.setKey(self._keyValue.get())
        self.destroy()


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self._root = master
        self._document = PwdDocument()
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
        # TODO check whether this document is dirty
        self._document = PwdDocument()

    def openDocument(self):
        # TODO check whether this document is dirty
        options = {}
        options['defaultextension'] = '.pwd'
        options['filetypes'] = [('password files', '.pwd')]
        options['initialdir'] = 'C:\\'
        options['parent'] = self._root
        options['title'] = 'Open File'
        fileName = tkFileDialog.askopenfile(mode='r', **options)
        if fileName is not None and fileName != "":
            self._document = PwdDocument()
            self._document.setFileName(fileName)
            self._document.readFile()
            self.UpdateList()

    def UpdateList(self):
        pwdItems = self._document.getItems()
        self._itemList.delete(0, tk.END)
        for item in pwdItems:
            self._itemList.insert(tk.END, item.getKey())

    def saveDocument(self):
        self._document.saveFile()

    def newItem(self):
        pwdItem = PwdDocumentItem()
        EditItemDialog(False, pwdItem)
        self._document.addItem(pwdItem)
        self.UpdateList()

    def deleteItem(self):
        self.UpdateList()

    def openItem(self):
        # get this item
        pwdItem = None
        if pwdItem is None:
            return
        EditItemDialog(True, pwdItem)


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
