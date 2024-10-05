from bottle import get, post, request, route, run, static_file, view
from loguru import logger
from os import path
from time import sleep
from tools import do_something, just_return, test_generator
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


@get("/hello")
@get("/hello/<name>")
@view("templates/form")
def hello(name="Default Name"):
    logger.debug(f"get hello {name}")
    return dict(name=name)


@post("/hello")
@post("/hello/<name>")
@view("templates/form")
def process(
    name="Default Name Override", input_field="text_form_override", number_of_times=1
):
    logger.debug(f"{request.forms}")
    logger.debug(f"post {name = }; {input_field = }; {number_of_times = }")
    """ result = do_something(
        text=(name + ": " + request.forms["input_field"]),
        number=int(request.forms["number_of_times"]),
    ) """
    for line in test_generator(
        text=request.forms["input_field"], number=int(request.forms["number_of_times"])
    ):
        yield f'<div id="results" hx-trigger="every 1s" hx-target="this" hx-swap="outerHTML"><p>{line}</p></div>'
    # result = just_return(input, number_of_times)
    # return result


@route("/hello/<name>/running")
def running(input, number_of_times):
    # result = do_something(text=input, number=number_of_times)
    result = just_return(input, number_of_times)
    return result


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


run(host="localhost", port=8080, debug=True)  # server="gevent" <- for asgi
