#!/usr/bin/env python3

'''
Test code for html_render.py

'''

import io

from html_render import Element, Html, Body, P

def test_init():
    e = Element()

    e = Element('this is some text')

def test_content():
    # fixme: this tests internals!!!!
    e = Element('this is some text')

    assert 'this is some text' in e.content

def test_append():
    e = Element('this is some text')

    e.append('some more text')

    assert 'some more text' in e.content

def test_two_instances():
    e = Element('this is some text')
    e2 = Element('this is some other text')

    e.append('some more text')

    assert 'some more text' not in e2.content

def test_render():
    outfile = io.StringIO()
    e = Element('this is some text')
    e.append('some more text')
    e.render(outfile)

    outfile.seek(0)
    file_contents = outfile.read()

    assert('this is some text') in file_contents
    assert('some more text') in file_contents

    assert file_contents.startswith('<html>')
    assert file_contents.strip().endswith('</html>')

def test_attributes():
    p = P("a little text", id="error", name="fred")
    outfile = io.StringIO()
    p.render(outfile)
    result = outfile.getvalue()

    print(result)
    assert 'name="fred"' in result
    assert 'id="error"' in result
    line1 = result.split("\n")[0].strip()
    assert line1.startswith("<")
    assert line1.endswith(">")





# test Html, Body, P