
import logging
import os
from logging import basicConfig


class LogGen():
    @staticmethod
    def loggen():
        path=os.path.abspath(os.curdir)+"\\log\\automation.log"
        logging.basicConfig(filename=path,
                            format='%(asctime)s %(levelname)s %(name)s %(message)s',datefmt='%m%d%y %I:%M:%s')
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
