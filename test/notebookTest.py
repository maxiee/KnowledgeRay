from db.models import *
import json


def createTextFragment(content):
    return Fragment.create(content=content, type="text")


def createPage(title, fragment):
    return Page.create(title=title, fragments=str([fragment.id]))

fragIntro = createTextFragment("前言")

frag11 = createTextFragment("什么是 Linux 呢?")
page11 = createPage("第一节 什么是 Linux", frag11)

frag12 = createTextFragment("下面我们来介绍 Ubuntu")
page12 = createPage("第二节 Ubuntu", frag12)

frag13 = createTextFragment("安装 Ubuntu")
page13 = createPage("下面我们来学习如何安装 Ubuntu", frag13)

chapter1Pages = [
    NoteBook.addPage(page11),
    NoteBook.addPage(page12),
    NoteBook.addPage(page13)
]

chapter1Title = Title.create(
    title="第一章 Linux",
    contains=NoteBook.addContains(chapter1Pages))

# 第二章

frag21 = createTextFragment("Ubuntu 使用的桌面环境是 Unity 桌面")
page21 = createPage("第一节 初识 Unity", frag21)

frag221 = createTextFragment("我们最常用的功能是文件管理...")
page221 = createPage("1. 文件管理", frag221)

frag222 = createTextFragment("浏览图片也是必需功能之一...")
page222 = createPage("2. 图像浏览", frag222)

chapter22Pages = [
    NoteBook.addPage(frag221),
    NoteBook.addPage(frag222)
]

chapter22 = Title.create(
    title="第二节 常用功能",
    contains=NoteBook.addContains(chapter22Pages)
)

chapter2Pages = [
    NoteBook.addPage(frag21),
    NoteBook.addTitle(chapter22) # 这里面的 contains 已经是 JSON 了
]

chapter2Title = Title.create(
    title="第二章 Unity 桌面",
    contains=NoteBook.addContains(chapter2Pages))

notebookPages = [
    NoteBook.addPage(fragIntro),
    NoteBook.addTitle(chapter1Title),
    NoteBook.addTitle(chapter2Title)
]

notebook = NoteBook.create(
    title="测试笔记本",
    contains=NoteBook.addContains(notebookPages)
)

print(notebook.contains)








