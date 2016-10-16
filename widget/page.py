from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import json
from parser.page import *
from render.map import *


class PageView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setAlignment(Qt.AlignTop)

    @pyqtSlot('QModelIndex')
    def onPageSelected(self, pageIndex):
        index = pageIndex.internalPointer()
        if index.data._meta.db_table != 'page':
            return
        page = index.data
        pageParser = PageParser(page)
        fragmentList = pageParser.parse()
        self.clearMainLayout()
        for fragment in fragmentList:
            widget = qtRenderMap[fragment.type](fragment).render()
            self.mainLayout.addWidget(widget)

    def clearMainLayout(self):
        for i in reversed(range(self.mainLayout.count())):
            widget = self.mainLayout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
