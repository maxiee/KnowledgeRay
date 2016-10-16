from PyQt5.QtWidgets import *
from db.models import *


class QTextFragmentEditor(QDialog):
    def __init__(self, fragment: Fragment, parent=None):
        super().__init__(parent)
        self.fragment = fragment

        mainLayout = QVBoxLayout()

        edit = QTextEdit()
        edit.setText(self.fragment.content)

        mainLayout.addWidget(edit)

        btnOK = QPushButton("保存")
        btnCancel = QPushButton("取消")

        endLayout = QHBoxLayout()
        endLayout.addStretch()
        endLayout.addWidget(btnCancel)
        endLayout.addWidget(btnOK)

        mainLayout.addLayout(endLayout)
        self.setWindowTitle("编辑文字片段")
        self.setLayout(mainLayout)
        self.resize(600, 400)