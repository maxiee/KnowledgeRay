from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from db.models import *


class QTextFragmentEditor(QDialog):
    fragmentUpdated = pyqtSignal(int)

    def __init__(self, fragment: Fragment, fragmentIndex, parent=None):
        super().__init__(parent)
        self.fragment = fragment
        self.fragmentIndex = fragmentIndex

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)

        self.edit = QTextEdit()
        self.edit.setText(self.fragment.content)

        mainLayout.addWidget(self.edit)

        btnSave = QPushButton("保存")
        btnCancel = QPushButton("取消")
        btnCancel.clicked.connect(lambda: self.close())
        btnSave.clicked.connect(self.onBtnSaveClicked)

        endLayout = QHBoxLayout()
        endLayout.addStretch()
        endLayout.addWidget(btnCancel)
        endLayout.addWidget(btnSave)

        mainLayout.addLayout(endLayout)
        self.setWindowTitle("编辑文字片段")
        self.setLayout(mainLayout)
        self.resize(600, 400)

    @pyqtSlot()
    def onBtnSaveClicked(self):
        text = self.edit.toPlainText()
        self.fragment.content = text
        self.fragment.save()
        self.fragmentUpdated.emit(self.fragmentIndex)
        self.close()