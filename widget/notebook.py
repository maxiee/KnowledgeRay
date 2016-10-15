from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class NoteBookCategoryWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        notebookLabel = QLabel("我的笔记本:")

        # layout
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(notebookLabel)
        mainLayout.addStretch()

        self.setLayout(mainLayout)
