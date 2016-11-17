# -*- coding: utf8 -*-

from werkzeug.wrappers import Request as RequestBase


class Request(RequestBase):

    def __init__(self, environ):
        super(Request, self).__init__(environ)
