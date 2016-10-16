from PyQt5.QtWidgets import *
from widget.notebook import *
from PyQt5.QtCore import pyqtSlot
import sys


@pyqtSlot()
def itemClicked(itemSelect):
    item = itemSelect.internalPointer()
    print("[id=%d]标题: %s" % (item.data.id, item.data.title))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mainWidget = QWidget(self)
        mainHLayout = QHBoxLayout(mainWidget)

        treeView = QTreeView()
        model = NoteBookTreeModel()
        treeView.setModel(model)
        treeView.clicked.connect(itemClicked)

        mainHLayout.addWidget(treeView)
        mainHLayout.addStretch()

        mainWidget.setLayout(mainHLayout)
        self.setCentralWidget(mainWidget)
        self.resize(800, 600)
        self.setWindowTitle("KnowledgeRay")
        self.show()


app = QApplication(sys.argv)
m = MainWindow()
sys.exit(app.exec_())