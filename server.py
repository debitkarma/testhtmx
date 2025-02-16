from bottle import get, post, request, route, run, static_file, view
from loguru import logger
from os import path
from rq import Queue
from rq.registry import StartedJobRegistry, FailedJobRegistry, FinishedJobRegistry
from time import sleep
from tools import do_something, just_return, test_generator

import redis

ROOT = path.abspath(path.dirname(__file__))
r = redis.Redis(host="redis", port=6379)
q = Queue(connection=r)
started_registry = StartedJobRegistry(queue=q)
failed_registry = FailedJobRegistry(queue=q)
finished_registry = FinishedJobRegistry(queue=q)


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
    jobs = ""
    for job in q.jobs:
        link = f'<a href="/hello/{name}/job/{job.id}">Status: {job._status}</a>'
        jobs += f"<p>ID: {job.id}<br />Queued at: {job.enqueued_at}<br />{link}</p>"

    return dict(name=name, jobs=jobs)


@post("/hello")
@post("/hello/<name>")
@view("templates/form")
def process(
    name="Default Name Override", input_field="text_form_override", number_of_times=1
):
    # logger.debug(f"{request.forms}")
    logger.debug(f"post {name = }; {input_field = }; {number_of_times = }")
    """ result = do_something(
        text=(name + ": " + request.forms["input_field"]),
        number=int(request.forms["number_of_times"]),
    ) """
    # for line in test_generator(
    #     text=request.forms["input_field"], number=int(request.forms["number_of_times"])
    # ):
    #     yield f'<div id="results" hx-trigger="every 1s" hx-target="this" hx-swap="outerHTML"><p>{line}</p></div>'
    for _ in request.forms["number_of_times"]:
        task = q.enqueue(
            # test_generator, text=f"{request.forms["input_field"]}", number=10
            do_something,
            text=f"{request.forms["input_field"]}",
            number=10,
        )

    for job in q.jobs:
        link = f'<a href="/hello/{name}/job/{job.id}">{job._status}</a>'
        yield f'<div id="results" hx-trigger="every 1s" hx-target="this" hx-swap="outerHTML"><p>{job.id} - {link}</p></div>'


@route("/<name>/jobs")
def jobs(name="Default Name"):
    for job in q.jobs:
        link = f'<a href="/hello/{name}/job/{job.id}">{job._status}</a>'
        yield f'<div id="jobs" hx-trigger="every 1s" hx-target="this" hx-swap="outerHTML"><p>{job.id} - {link}</p></div>'


@route("/hello/<name>/job/<job_id>")
def job(name, job_id):
    job = q.fetch_job(job_id)
    if not job.return_value:
        return f"<center><br /><br /><h3>The job is still pending</h3><br /><br />ID:{job_id}<br />Queued at: {job.enqueued_at}<br />Status: {job._status}</center>"
    else:
        return f'<center><br /><br /><img src="{job.result}" height="200px"><br /><br />ID:{job_id}<br />Queued at: {job.enqueued_at}<br />Finished at: {job.ended_at}</center>'


@route("/<name>/done")
def done(name="Default Name"):
    # failed_jobs = failed_registry.get_job_ids()
    # finished_jobs = finished_registry.get_job_ids()

    for job in failed_registry:
        result = job.latest_result()
        link = f'<a href="/hello/{name}/job/{job.id}">{result.exc_string}</a>'
        yield f'<div id="jobs" hx-trigger="every 1s" hx-target="this" hx-swap="outerHTML"><p>{job.id} - {link}</p></div>'
    for job in finished_registry:
        result = job.latest_result()
        link = f'<a href="/hello/{name}/job/{job.id}">{result.return_value}</a>'
        yield f'<div id="jobs" hx-trigger="every 1s" hx-target="this" hx-swap="outerHTML"><p>{job.id} - {link}</p></div>'


@route("/hello/<name>/running")
def running(input, number_of_times):
    result = do_something(text=input, number=number_of_times)
    # result = just_return(input, number_of_times)
    return result


@get("/readme")
def readme():
    return static_file("README.md", root="./")


@get("/test")
def test():
    result = just_return()
    return result


@route("/stream")
def stream():
    yield "START"
    sleep(3)
    yield "MIDDLE"
    sleep(5)
    yield "END"


run(host="0.0.0.0", port=8080, debug=True)
