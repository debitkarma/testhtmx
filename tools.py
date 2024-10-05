from time import sleep
# from gevent import monkey

# monkey.patch_all()


def do_something(text: str = "hidden_default", number: int = 4):
    for i in range(number):
        sleep(5)
    return "FINISHED"
