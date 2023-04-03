"""
Last updated in April 2023
    Works for Python 3.4 or later.
    The log file is saved in the same working directory by default.
    May not support multi-threading use.
    Available at:
        Website: https://rpglab.github.io/resources/Logging-Python/

@author: Xingpeng Li (xplipower@gmail.com)


An old version of this class was Created in 2016:
    works for Python 2
    available at: https://rpglab.github.io/resources/RT-SCED_Python/


A similar Java version is available at:
    https://github.com/rpglab/Log


Example:

import logpy
logger = logpy.logpy()
logger.hotline("test l")
logger.hotline("test 2")
logger.close()

"""

import time
from enum import Enum


# Define an enumeration class for Message Type
class LogType(Enum):
    NORMAL = 0
    WARNING = 1
    ERROR = 2
    START = 3
    END = 4
    MILESTONE = 5
    SUMMARY = 6
    NOTICE = 7
    CRITICAL = 8
    COMMENT = 9
    TBD = 10
    CHECKPOINT = 11
    OTHER = 97
    DEBUG = 98
    UNKNOWN = 99


class logpy:
    """class used to log messages"""

    def __init__(self):
        self.start_time = time.time()
        # timeMark = str(time.ctime(time.time()))
        # fileName = timeMark[4:].replace(' ', '_').replace(':', '_')  # a different date/time format
        timeMark = time.strftime("%Y-%b-%d %H:%M:%S")
        fileName = timeMark.replace(' ', '_').replace(':', '_')
        # self.logger = open('log\Log_'+fileName+'.txt', 'w') # customize the location of the log file as needed
        self.logger = open('Log_' + fileName + '.txt', 'w')  # customize the log file name as needed
        heading = 'LogItem 1 , t=' + logpy.getElapsedTime(self) + 's , ' \
                  + LogType.START.name + ' , '
        self.logger.write(heading + 'this log file was created @ ' + timeMark + "\n")
        self.logger.flush()
        self.count = 1   # log message index, starting from 1

    def hotline(self, message):
        logpy.hotlineWithLogType(self, LogType.NORMAL, message)

    def hotlineWithLogType(self, mType, message):
        self.count += 1
        heading = "LogItem " + str(self.count) + ' , t=' + logpy.getElapsedTime(self) + 's , ' \
                  + mType.name + ' , '
        self.logger.write(heading + message + '\n')
        self.logger.flush()   # you can flush at the end - might save some time

    def close(self):
        self.count += 1
        # timeMark = str(time.ctime(time.time()))
        timeMark = time.strftime("%Y-%b-%d %H:%M:%S")

        heading = "LogItem " + str(self.count) + ' , t=' + logpy.getElapsedTime(self) + 's , ' \
                  + LogType.END.name + ' , '
        self.logger.write(heading + 'this log file was closed @ ' + timeMark + '\n')
        self.logger.flush()
        self.logger.close()

    def getElapsedTime(self):
        elapsed_time = time.time() - self.start_time
        return format(elapsed_time, '.2f')


"""
    ## Old code removed
    def getLogType(self, num):
        if num == 0:
            return 'Normal'
        elif num == 1:
            return 'Warning'
        elif num == 2:
            return 'Error'
        elif num == 3:
            return 'Start'
        elif num == 4:
            return 'End'
        elif num == 5:
            return 'Milestone'
        elif num == 6:
            return 'Summary'
        elif num == 7:
            return 'Notice'
        else:
            return 'Unknown'
"""


if __name__ == '__main__':
    print("Program starts here...")
    logger = logpy()

    logger.hotline("test l")
    logger.hotlineWithLogType(LogType.MILESTONE, "test 2")

    logger.close()
    print("\nProgram ends here...")
