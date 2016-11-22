#!/usr/bin/env python3

class Element:
    def __init__(self, content=None):
        self.content = []
        self.tag = "html"
        if content is not None:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, out_file, indent=""):
        out_file.write("<{}>\n".format(self.tag))
        for stuff in self.content:
            try:
                new_ind = indent + "    "
                stuff.render(out_file, indent=new_ind)
                out_file.write("\n")
            except AttributeError:
                out_file.write(new_ind + str(stuff) + "\n")
        out_file.write("</{}>\n".format(self.tag))

    # def render(self, out_file, indent=""):
    #     out_file.write("<{}>\n".format(self.tag))
    #     for stuff in self.content:
    #         new_ind = indent + "    "
    #         if self.tag == "p":
    #             stuff.render(out_file, indent=new_ind)
    #             out_file.write("\n")
    #         if self.tag == "body":
    #             new_ind = indent + "    "
    #             stuff.render(out_file, indent=new_ind)
    #             out_file.write("\n")
    #         if self.tag == "html":
    #             out_file.write(new_ind + str(stuff) + "\n")
    #     out_file.write("</{}>\n".format(self.tag))

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    



