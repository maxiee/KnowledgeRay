from peewee import *
from datetime import datetime

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


class NoteBook(Model):

    # 笔记本的题目
    title = TextField()
    # 笔记本的目录, 是个 JSON, 里面

    class Meta:
        database = knowledgeDB

knowledgeDB.connect()
Fragment.create_table(True)
Page.create_table(True)
NoteBook.create_table(True)