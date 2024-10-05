from bottle import route, run, static_file, view
from os import path
from time import sleep
from tools import do_something
# from gevent import monkey

# monkey.patch_all()

ROOT = path.abspath(path.dirname(__file__))


@route("/static/<filepath>")
def server_static(filepath):
    return static_file(filepath, root="./static/")
    # return static_file(filepath, root=path.join(ROOT, "static"))


@route("htmx.js")
def serve_htmx():
    return static_file("htmx.js", root="./")


@route("/hello")
@route("/hello/<name>")
@view("templates/form")
def hello(name="Default Name"):
    return dict(name=name)


@route("/hello/<name>/running")
def running(input, number_of_times):
    do_something(text=input, number=number_of_times)


@route("/test")
def test():
    return static_file("README.md", root="./")


@route("/stream")
def stream():
    yield "START"
    sleep(3)
    yield "MIDDLE"
    sleep(5)
    yield "END"


run(host="localhost", port=8080, debug=True, server="gevent")
