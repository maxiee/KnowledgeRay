from db.models import *
from PyQt5.QtWidgets import *


class QtTextRender:
    fragment = None

    def __init__(self, fragment):
        self.fragment = fragment

    def render(self, debug=False):
        str = ""
        if debug:
            str += "fragment id = %d\n" % self.fragment.id
        str += self.fragment.content
        return QLabel(str)