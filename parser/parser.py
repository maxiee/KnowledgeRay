import json
from db.models import *

TYPE_PAGE = 'page'
TYPE_TITLE = 'title'


def getItemObject(item):
    if item['type'] == TYPE_PAGE:
        return Page.get(Page.id == item['id'])

    if item['type'] == TYPE_TITLE:
        return Title.get(Title.id == item['id'])


def parsePage(page: Page):
    fragments = json.loads(page.fragments)
    fragmentList = []
    for fragmentId in fragments:
        fragment = Fragment.get(Fragment.id == fragmentId)
        fragmentList.append(fragment)
    return fragmentList


def parseTitle(title: Title):
    return json.loads(title.contains)


def parseNoteBook(notebook: NoteBook):
    return json.loads(notebook.contains)