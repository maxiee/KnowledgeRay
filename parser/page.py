from db.models import *
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
            print(fragment.content)

