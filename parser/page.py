from db.models import *
from render.map import *
import ast


class PageParser():
    title = ""
    fragmentList = []
    page = None

    def __init__(self, page: Page):
        self.title = page.title
        self.page = page

    def parse(self):
        fragments = ast.literal_eval(self.page.fragments)
        for fragmentId in fragments:
            fragment = Fragment.get(Fragment.id == fragmentId)
            self.fragmentList.append(fragment)

    def render(self):
        print("*" * len(self.title) * 2)
        print(self.title)
        print("*" * len(self.title) * 2)
        print()
        for fragment in self.fragmentList:
            renderClass = cliRenderMap[fragment.type]
            renderInstance = renderClass(fragment)
            renderInstance.render(True)
