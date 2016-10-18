from db.models import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setWordWrap(True)

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()


class QtTextRender(QObject):
    fragmentClicked = pyqtSignal(Fragment, int)
    fragment = None
    fragmentIndex = None

    def __init__(self, fragment, fragmentIndex, parent=None):
        super().__init__(parent)
        self.widget = ClickableLabel("")
        self.fragment = fragment
        self.fragmentIndex = fragmentIndex

    def render(self, debug=False):
        str = ""
        if debug:
            str += "fragment id = %d\n" % self.fragment.id
        str += self.fragment.content
        self.widget.setText(str)
        self.widget.clicked.connect(lambda: self.onLabelClicked())
        return self.widget

    def update(self):
        self.fragment = Fragment.get(Fragment.id == self.fragment.id)
        self.widget.setText(self.fragment.content)

    @pyqtSlot()
    def onLabelClicked(self):
        self.fragmentClicked.emit(self.fragment, self.fragmentIndex)
