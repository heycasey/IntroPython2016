#!/usr/bin/env python

"""
args-kwargs lab:

Experimenting with various ways to call and define functions
"""


def colors(fore_color='red',
           back_color='blue',
           link_color='green',
           visited_color='cyan',
           ):
    output = ("The colors are:\n"
              "  foreground: {fore_color}\n"
              "  background: {back_color}\n"
              "  link: {link_color}\n"
              "  visited: {visited_color}")
    output = output.format(fore_color=fore_color,
                           back_color=back_color,
                           link_color=link_color,
                           visited_color=visited_color)

    return output
