#!/usr/bin/env python3

"""
Python class example.
"""


# The start of it all:
# Fill it all in here.

class Element:
    tag = "html"

    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, tag=""):
        file_out.write("<{}>\n".format(self.tag))
        for stuff in self.content:
            file_out.write(stuff+"\n")
        file_out.write("</{}>\n".format(self.tag))

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

# class Element(object):

#     def __init__(self, content=None):
#         self.content = content
#         pass
#     def append(self, new_content):
#         pass
#     def render(self, file_out, ind=""):
#         file_out.write("just something as a place holder...")
