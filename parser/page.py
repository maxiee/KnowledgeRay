import json
from render.map import *


# class PageParser:
#     title = ""
#     fragmentList = []
#     page = None
#
#     def __init__(self, page):
#         self.title = page.title
#         self.page = page
#
#     def parse(self):
#         self.fragmentList.clear()
#         fragments = json.loads(self.page.fragments)
#         for fragmentId in fragments:
#             fragment = Fragment.get(Fragment.id == fragmentId)
#             self.fragmentList.append(fragment)
#         return self.fragmentList
#
#     def cliRender(self):
#         print("*" * len(self.title) * 2)
#         print(self.title)
#         print("*" * len(self.title) * 2)
#         print()
#         for fragment in self.fragmentList:
#             renderClass = cliRenderMap[fragment.type]
#             renderInstance = renderClass(fragment)
#             renderInstance.render(True)

