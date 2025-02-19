from loguru import logger
from time import sleep


def do_something(text: str = "hidden_default", number: int = 4):
    for i in range(number):
        sleep(5)
        logger.debug(f"slept #{i} time(s)")
    return "FINISHED"


def just_return(*args, **kwargs):
    logger.debug("just returning from func")
    return "returning"


def test_generator(text: str = "hidden_default", number: int = 1):
    logger.debug(f"entered test_gen; {text=}, {number=}")
    for i in range(number):
        sleep(10)
        logger.debug("slept 10")
        # yield f"\n{text} ; {i}\n"
    return "job complete!"
