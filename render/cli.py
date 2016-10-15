from db.models import *


class CliTextRender():
    fragment = None

    def __init__(self, fragment):
        self.fragment = fragment

    def render(self, debug=False):
        if debug:
            print("fragment id = %d" % self.fragment.id)
        print(self.fragment.content + '\n')
