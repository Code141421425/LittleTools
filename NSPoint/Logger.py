import logging
import os
from logging.handlers import TimedRotatingFileHandler
from Base import singleton


class MyLogger:
    notice = None
    logger = None
    LOG_PATH = os.path.abspath(__file__) + '/../Log/'

    def __init__(self):
        self.logger = logging.getLogger("MyLogger")
        self.logger.setLevel(logging.INFO)

        self.streamHandler = logging.StreamHandler()
        self.streamHandler.setLevel(logging.INFO)
        self.fileHandler = TimedRotatingFileHandler(self.LOG_PATH+"NSP_Report",
                                                    when="D")

        self.fileHandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
        self.fileHandler.setLevel(logging.INFO)

        self.formatter = logging.Formatter("[%(levelname)-8s]%(asctime)s "
                                           "| %(message)s",
                                           datefmt="%Y-%m-%d %H:%M:%S")

        self.logger.addHandler(self.streamHandler)
        self.logger.addHandler(self.fileHandler)
        self.streamHandler.setFormatter(self.formatter)
        self.fileHandler.setFormatter(self.formatter)


class Handler(logging.Handler):
    def __init__(self, **kwargs):
        super(Handler, self).__init__(**kwargs)

    def emit(self, record):
        msg = self.format(record)
        print(msg)


if __name__ == "__main__":
    lg = MyLogger().logger

    #
    # lg.debug("000")
    # lg.info("111")
    # lg.warning("222")
    # lg.error("333")
    lg.info("Start Use")


