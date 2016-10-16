from db.models import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setText(text)

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()


class QtTextRender(QObject):
    fragmentClicked = pyqtSignal(Fragment)
    fragment = None

    def __init__(self, fragment, parent=None):
        super().__init__(parent)
        self.fragment = fragment

    def render(self, debug=False):
        str = ""
        if debug:
            str += "fragment id = %d\n" % self.fragment.id
        str += self.fragment.content
        widget = ClickableLabel(str)
        widget.clicked.connect(lambda: self.onLabelClicked())
        return widget

    @pyqtSlot()
    def onLabelClicked(self):
        self.fragmentClicked.emit(self.fragment)
