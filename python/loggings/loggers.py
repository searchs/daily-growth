import logging
import sys

root_logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter("%(levelname)s: %(message)s")
handler.setFormatter(formatter)
root_logger.addHandler(handler)
root_logger.setLevel("INFO")

# logging.INFO("Application starting.")
root_logger.info("No error in starting...")
root_logger.error("Funny error", exc_info=True)


# More professional setup
# import logging
from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "formatters": {"short": {"format": "%(levelname)s: %(message)s"}},
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "short",
                "stream": "ext://sys.stdout",
                "level": "DEBUG",
            }
        },
        "loggers": {"": {"handlers": ["console"], "level": "INFO"}},
    }
)

logging.info("Professional shareable config")


# Using BasicConfig
import logging as basic

basic.basicConfig(level="INFO", format="%(levelname)s %(message)s", stream=sys.stdout)
basic.info("Basic Config is good too!")

# Using ini file
import logging
from logging.config import fileConfig

fileConfig("logging-config.ini")
logging.info("INI config speaking into the logs")
