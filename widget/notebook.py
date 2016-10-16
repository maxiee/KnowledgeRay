from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from db.models import *
from parser.notebook import *
import json


class NoteBookTreeItem:

    def __init__(self, data, parent=None):
        self.parent = parent
        self.children = []
        self.data = data
        self.setParent(parent)

    def setParent(self, parent):
        if parent is not None:
            self.parent = parent
            self.parent.appendChild(self)
        else:
            self.parent = None

    def appendChild(self, child):
        self.children.append(child)

    def childAtRow(self, row):
        return self.children[row]

    def rowOfChild(self, child):
        for i, item in enumerate(self.children):
            if item == child:
                return i
        return -1

    def __len__(self):
        return len(self.children)


class NoteBookTreeModel(QAbstractItemModel):
    root = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.loadNoteBook()

    def columnCount(self, parent=None, *args, **kwargs):
        return 1

    def rowCount(self, parent):
        node = self.nodeFromIndex(parent)
        if node is None:
            return 0
        print('rowCount -> ' + str(len(node)))
        return len(node)

    def data(self, QModelIndex, role=None):
        if not QModelIndex.isValid() or role != Qt.DisplayRole:
            return QVariant()
        noteBookTreeItem = self.nodeFromIndex(QModelIndex)
        return noteBookTreeItem.data.title

    def flags(self, QModelIndex):
        if not QModelIndex.isValid():
            return 0
        return QAbstractItemModel.flags(self, QModelIndex)

    def headerData(self, p_int, Qt_Orientation, role=None):
        return QVariant()

    def index(self, row, column, parent=None, *args, **kwargs):
        node = self.nodeFromIndex(parent)
        return self.createIndex(row, column, node.childAtRow(row))

    def parent(self, child=None):
        if not child.isValid():
            return QModelIndex()
        node = self.nodeFromIndex(child)

        if node is None:
            return QModelIndex()

        parent = node.parent

        if parent is None:
            return QModelIndex()

        grandparent = parent.parent
        if grandparent is None:
            return QModelIndex()
        row = grandparent.rowOfChild(parent)
        assert row != -1
        return self.createIndex(row, 0, parent)

    def nodeFromIndex(self, index):
        return index.internalPointer() if index.isValid() else self.root

    def loadNoteBook(self):
        self.root = NoteBookTreeItem(None, None)
        notebook = NoteBook.select().get()
        notebookItem = NoteBookTreeItem(notebook, self.root)
        items = json.loads(notebook.contains)
        for item in items:
            modelObject = getItemObject(item)
            treeItem = NoteBookTreeItem(modelObject, notebookItem)

class NoteBookCategoryWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        notebookLabel = QLabel("我的笔记本:")

        # layout
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(notebookLabel)
        mainLayout.addStretch()

        self.setLayout(mainLayout)