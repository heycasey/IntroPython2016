#!/usr/bin/env python3


def p_wrapper(function):
    def func(*args, **kwargs):
        string = function(*args, **kwargs)
        # string = "<p> " + string + " </p>"
        string = "<p> {} </p>".format(string)
        return(string)
    return(func)


class tag_wrapper:
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, orig_func):
        def func(*args, **kwargs):
            string = orig_func(*args, **kwargs)
            # string = "<{}> {} </{}>".format(self.tag, string, self.tag)
            string = "<{tag}> {s} </{tag}>".format(tag=self.tag, s=string)
            return(string)
        return(func)
