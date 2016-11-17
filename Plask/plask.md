= Plask: 白话Flask

模拟Flask。

======
Plask工程将分析Flask源码。

Hello Plask实例：
```python
    from plask import Plask

    app = Plask(__name__)

    @app.route('/')
    def index():
        return 'Hello Plask'

    if __name__ == '__main__':
        app.run()
```



Plask提供了一套网络框架，本身并不实现Web Server/App、模板等底层功能，只提供了路由逻辑控制的功能。

为了实现一套可用的网络框架，需要借助其他底层基础工具提供相应的能力：
    - Werkzeug: Web Server
    - Jinja2: 模板

目前Plask版本使用Werkzeug提供Web Server能力，
还未借助Jinja2等工具实现模板功能。

===源码解析===
```python
    app = Plask(__name__)

    app.run()
```
第一句首先定义一个WSGI app，根据(PEP 333标准)[https://www.python.org/dev/peps/pep-0333/]，一个应用端(Application side)需要满足下列标准，需要传递一个环境变量(environ)和一个回调函数(start_response)。

    [Server/Gateway] ---(invoke)---> [application/Framework]

一个最简单的WSGI Application如下，
```python
def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']
```
在该函数中，我们需要调用回调函数，并且返回。在该函数中，可以处理该app相应的操作。


=====
TODO: 下一步解析Plask类。
