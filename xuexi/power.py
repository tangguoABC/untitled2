# encoding:utf-8
import csv
import os
import time

# class Controller(object):
#     def __init__(self,count):
#         pass
#
#     def testprocess(self):
#
#         result = os.popen("adb shell dumpsys battery")
#
#         for line in result:
#             if "level" in line:
#                 power = line.split(":")[1]
#
#         a = time.strftime('%Y-%m-%d %H:%M:%S')
#
#


a = os.popen("adb shell dumpsys battery")
# print(a.read())
print(type(a))
for line in a:
    print(type(line))
    if 'level' in line:
        power = line.split(':')[1]
        print(power)


