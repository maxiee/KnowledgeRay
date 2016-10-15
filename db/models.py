from peewee import *
from datetime import datetime
from parser.notebook import *
import json

knowledgeDB = SqliteDatabase('../dbfiles/knowledge.sqlite')


class Fragment(Model):

    content = TextField()
    type = CharField()

    class Meta:
        database = knowledgeDB


class Page(Model):

    # 一篇文章的题目
    title = TextField()
    # 页面包含的 Fragments, 是一个由 Fragment id 组成的 Json List
    fragments = TextField()

    class Meta:
        database = knowledgeDB


class Title(Model):

    title = TextField()
    contains = TextField()

    class Meta:
        database = knowledgeDB


class NoteBook(Model):

    # 笔记本的题目
    title = TextField()
    # 笔记本的目录, 是个 JSON, 里面
    contains = TextField()

    @staticmethod
    def addPage(page: Page):
        return {"id": page.id, "type": "page"}

    @staticmethod
    def addTitle(title: Title):
        contains = title.contains
        if isinstance(contains, str):
            contains = json.loads(contains)
        return {"id": title.id, "contains": contains, "type": "title"}

    @staticmethod
    def addContains(contains):
        return json.dumps(contains, indent=4)

    class Meta:
        database = knowledgeDB

knowledgeDB.connect()
Fragment.create_table(True)
Page.create_table(True)
Title.create_table(True)
NoteBook.create_table(True)
