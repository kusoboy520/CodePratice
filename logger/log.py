# encoding = utf-8

import logging
class Logger():
    def __init__(self, logname="test_log", loglevel=logging.DEBUG, loggername=None):
        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(loglevel)
        fh = logging.FileHandler(logname)
        fh.setLevel(loglevel)
        if not self.logger.hasHandlers():
            ch = logging.StreamHandler()
            ch.setLevel(loglevel)

            formatter = logging.Formatter('[%(levelname)s]%(asctime)s %(filename)s:%(lineno)d: %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

            # self.logger.fatal('Add Handler')
        # self.logger.fatal('set logger')
    def getlog(self):
        self.logger.fatal("get logger")
        return self.logger
