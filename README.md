# testhtmx

This is a toy project to get to learn how HTMX works. Working with `bottle` as a web server, though I may eventually switch to flask/asgi to see how that could work after this is up and running.

Also, I'm learning `uv` with this project. It's _fast_! Gotta get back on the Rust train eventually! 

## Resources

- [uv venv](https://docs.astral.sh/uv/pip/environments/#creating-a-virtual-environment)

- [Bottle docs for ASGI/async](https://bottlepy.org/docs/dev/async.html)
- [htmx triggers](https://htmx.org/docs/#triggers)
- [htmx progress bars](https://htmx.org/examples/progress-bar/)
- [pyHAT stack site (project showcase for htmx/asgi/tailwind)](https://github.com/PyHAT-stack/awesome-python-htmx?tab=readme-ov-file)
- [tailwind css docs](https://tailwindcss.com/docs/installation)

- [Flask megatutorial, Ch22, Background Jobs](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs)
- [Fullstack Python guide on background jobs/task queues](https://www.fullstackpython.com/task-queues.html)
- [Reddit thread on RESTful (semantic) polling for job status (seems reasonable and fairly clean)](https://www.reddit.com/r/FastAPI/comments/11677me/how_to_get_progress_of_long_running_api_call/)
- [RQ, simple job queue for python, using Redis](https://python-rq.org/docs/job_registries/)
- [Redis alpine image on Dockerhub](https://hub.docker.com/layers/library/redis/alpine/images/sha256-c516894338a5330979fdaa939f0cca770031d79a43dc0d6553748430130525ac?context=explore)