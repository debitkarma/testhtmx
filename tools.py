from loguru import logger
from time import sleep
# from gevent import monkey

# monkey.patch_all()


def do_something(text: str = "hidden_default", number: int = 4):
    for i in range(number):
        sleep(5)
        logger.debug(f"slept #{i} time(s)")
    return "FINISHED"


def just_return(*args, **kwargs):
    logger.debug("just returning from func")
    return "returning"
