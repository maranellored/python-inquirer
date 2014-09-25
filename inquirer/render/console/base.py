# -*- coding: utf-8 -*-

from __future__ import print_function

from blessings import Terminal


class BaseConsoleRender(object):
    title_inline = False

    def __init__(self, question, terminal=None,
                 *args, **kwargs):
        super(BaseConsoleRender, self).__init__(*args, **kwargs)
        self.question = question
        self.terminal = terminal or Terminal()
        self.answers = {}

    def get_header(self):
        return self.question.message

    def get_current_value(self):
        return ''

    def get_options(self):
        return []

    def read_input(self):
        raise NotImplemented('Abstract')
