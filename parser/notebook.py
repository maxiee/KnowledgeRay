from db.models import Page, Title, NoteBook
from parser.page import *
import json

TYPE_PAGE = 'page'
TYPE_TITLE = 'title'


def renderItem(item):
    if item['type'] == TYPE_PAGE:
        page = Page.get(Page.id == item['id'])
        pageParse = PageParser(page)
        pageParse.parse()
        pageParse.render()

    if item['type'] == TYPE_TITLE:
        title = Title.get(Title.id == item['id'])
        titleParse = TitleParser(title)
        titleParse.parse()
        titleParse.render()


class TitleParser:
    titleString = ""
    contains = []
    titleObject = None

    def __init__(self, title):
        self.titleString = title.title
        self.titleObject = title

    def parse(self):
        contains = self.titleObject.contains
        self.contains = json.loads(contains)

    def render(self):
        print("-->" + self.titleString)
        for item in self.contains:
            renderItem(item)


class NoteBookParser:
    title = ""
    contains = []
    notebook = None

    def __init__(self, notebook):
        self.title = notebook.title
        self.notebook = notebook

    def parse(self):
        contains = self.notebook.contains
        self.contains = json.loads(contains)

    def render(self):
        for item in self.contains:
            renderItem(item)