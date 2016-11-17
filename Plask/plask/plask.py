#!/bin/python
# -*- coding: utf8 -*-

from response import Response
from request import Request
from werkzeug.routing import Map, Rule


class Plask(object):

    def __init__(self, package_name):
        self.package_name = package_name

        # url_map: path --> endpoint --> handler
        self.url_map = Map()
        # mapping: func_name --> function()
        self.view_functions = {}

    def run(self, host='localhost', port=6000):
        from werkzeug.serving import run_simple

        return run_simple(host, port, self)

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)

        try:
            endpoint, values = adapter.match()
            return self.view_functions[endpoint](**values)
        except Exception as ex:
            print ex
            return ex

    def make_response(self, rv):
        if isinstance(rv, Response):
            return rv
        if isinstance(rv, basestring):
            return Response(rv)

    def wsgi_app(self, environ, start_response):
        # resp = Response('Hello Plask (by custom response)\n')
        # return resp(environ, start_response)

        req = Request(environ)
        rv = self.dispatch_request(req)

        resp = self.make_response(rv)

        return resp(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def add_url_rule(self, rule, func_name):
        r = Rule(rule, endpoint=func_name)
        self.url_map.add(r)

    def route(self, rule):

        def decorete(func):
            func_name = func.__name__
            self.add_url_rule(rule, func_name)
            self.view_functions[func_name] = func

            return func

        return decorete
