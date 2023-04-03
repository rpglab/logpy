"""
Created in April 2023

@Author: Xingpeng Li

Website: https://rpglab.github.io/resources/Logging-Python/
"""

from logpy import logpy

myDiary = logpy.logpy()
myDiary.hotline("Test Example 1")

varX = 2.5
myDiary.hotlineWithLogType(logpy.LogType.COMMENT, "Test Point 1: \"varX\" has a value of \"" + str(varX) + "\"")

myDiary.hotline("The program will run the SCED simulation")

myDiary.hotline("Start to read needed data from raw file")
myDiary.hotline("Finish reading needed data from raw file")

myDiary.hotlineWithLogType(logpy.LogType.NOTICE, "The name of the case data file loaded is: ")
myDiary.hotlineWithLogType(logpy.LogType.MILESTONE, "Start to load input data for pyomo simulation")
myDiary.hotlineWithLogType(logpy.LogType.MILESTONE, "Finish loading input data for pyomo simulation"
                                                    " - an instance has been created")

errorFind = True
if errorFind:
    myDiary.hotlineWithLogType(logpy.LogType.ERROR, "An ERROR has been identified: at file \"AAA.py\", related to "
                                                    "variable \"errorFind\" with an unexpected value of \""
                               + str(errorFind) + "\"")

myDiary.close()
print("\nProgram ends here...")
