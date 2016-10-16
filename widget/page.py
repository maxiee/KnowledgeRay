from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import json
from parser.page import *
from parser.parser import *
from render.map import *
from dialog.page import *


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
        fragmentList = parsePage(page)
        self.clearMainLayout()
        for fragment in fragmentList:
            widgetRender = qtRenderMap[fragment.type](fragment)
            widget = widgetRender.render()
            widgetRender.fragmentClicked.connect(self.clickTextFragmentToEdit)
            self.mainLayout.addWidget(widget)

    @pyqtSlot(Fragment)
    def clickTextFragmentToEdit(self, fragment: Fragment):
        QTextFragmentEditor(fragment).exec()

    def clearMainLayout(self):
        for i in reversed(range(self.mainLayout.count())):
            widget = self.mainLayout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
