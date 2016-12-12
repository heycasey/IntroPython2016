#!/usr/bin/env python

"""
Python class example.
"""

class Element:
	def __init__(self, content=None):
		self.content = []
		if content:
			self.content.append(content)

	def append(self, content):
		self.content.append(content)

	def render (self, out_file):
		out_file.write('<html>\n')
		for stuff in self.content:
			out_file.write(stuff)
		out_file.write('</html>\n')




