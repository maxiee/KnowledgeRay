from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import json
from parser.page import *
from parser.parser import *
from render.map import *
from dialog.page import *


class PageView(QWidget):
    fragmentRenderList = []

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
        self.fragmentList = parsePage(page)
        self.clearMainLayout()
        for index, fragment in enumerate(self.fragmentList):
            widgetRender = qtRenderMap[fragment.type](fragment, index)
            widget = widgetRender.render()
            widgetRender.fragmentClicked.connect(self.clickTextFragmentToEdit)
            self.fragmentRenderList.append(widgetRender)
            self.mainLayout.addWidget(widget)

    @pyqtSlot(Fragment, int)
    def clickTextFragmentToEdit(self, fragment: Fragment, index):
        editor = QTextFragmentEditor(fragment, index)
        editor.fragmentUpdated.connect(self.updateFragment)
        editor.exec()

    @pyqtSlot(int)
    def updateFragment(self, index):
        self.fragmentRenderList[index].update()

    def clearMainLayout(self):
        for i in reversed(range(self.mainLayout.count())):
            widget = self.mainLayout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
