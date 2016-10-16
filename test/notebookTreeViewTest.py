from PyQt5.QtWidgets import *
from widget.notebook import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mainWidget = QWidget(self)
        mainHLayout = QHBoxLayout(mainWidget)

        treeView = QTreeView()
        model = NoteBookTreeModel()
        treeView.setModel(model)

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