import logging
import os
from logging.handlers import TimedRotatingFileHandler
from Base import singleton


class MyLogger:
    notice = None
    logger = None
    LOG_PATH = os.path.abspath(__file__) + '/../Log/'

    def __init__(self, app=None):
        self.logger = logging.getLogger("MyLogger")
        self.logger.setLevel(logging.INFO)

        self.streamHandler = logging.StreamHandler()
        self.streamHandler.setLevel(logging.INFO)
        self.fileHandler = TimedRotatingFileHandler(self.LOG_PATH+"NSP_Report",
                                                    when="D",interval=365)

        self.fileHandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
        self.fileHandler.setLevel(logging.INFO)

        self.formatter = logging.Formatter("[%(levelname)-8s]%(asctime)s "
                                           "| %(message)s",
                                           datefmt="%Y-%m-%d %H:%M:%S")

        self.logger.addHandler(self.streamHandler)
        self.logger.addHandler(self.fileHandler)
        self.streamHandler.setFormatter(self.formatter)
        self.fileHandler.setFormatter(self.formatter)

        if app:
            self.appHandler = APPHandler(app)
            self.appHandler.setLevel(logging.INFO)
            self.logger.addHandler(self.appHandler)
            self.appHandler.setFormatter(self.formatter)


class APPHandler(logging.Handler):
    def __init__(self, app, **kwargs):
        super(APPHandler, self).__init__(**kwargs)
        self.app = app

    def emit(self, record):
        msg = self.format(record)
        print(msg)
        self.app.AddLog(msg)


if __name__ == "__main__":
    lg = MyLogger().logger

    #
    # lg.debug("000")
    # lg.info("111")
    # lg.warning("222")
    # lg.error("333")
    lg.info("End Debugg")


