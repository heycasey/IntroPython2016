#!/usr/env/python3

from html_render import Element, Html, Body, P
import io


def test_init():
    e = Element()

    e = Element("This is text")


def test_content():
    e = Element("this is also text")

    assert "this is also text" in e.content


def test_append():
    e = Element("this is also text")
    e.append("some more text")

    assert "some more text" in e.content


def test_two_instances():
    e = Element("this is also text")
    e2 = Element("this is also text")

    e.append("some more text")

    assert "some more text" in e.content


def test_render():
    outfile = io.StringIO()

    # e = Element.Html("this is also text")
    e = Html("this is also text")
    e.append("let's add even more text")

    e.render(outfile, "")

    outfile.seek(0)
    file_contents = outfile.read()

    assert("this is also text") in file_contents
    assert("let's add even more text") in file_contents

    # assert("<html>") in file_contents
    assert file_contents.startswith("<html>")
    # assert("</html>") in file_contents
    assert file_contents.strip().endswith("</html>")

    # print(file_contents)
    # assert False
