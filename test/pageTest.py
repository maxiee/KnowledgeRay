from db.models import *
from parser.page import *
import json

fragment1 = Fragment.create(
    content="比起上学, 上了班以后, 时间明显减少了.",
    type="text")

fragment2 = Fragment.create(
    content="但是在工作中能力提升地比较快.",
    type="text")

fragment3 = Fragment.create(
    content="想写的程序更多了, 卒.",
    type="text")

fragmentList = [fragment1.id, fragment2.id, fragment3.id]

page = Page.create(
    title="工作感悟",
    fragments=json.dumps(fragmentList))

pageParser = PageParser(page)
pageParser.parse()
pageParser.cliRender()
