import numpy
import pandas as pd
import matplotlib.pyplot as plt
import calendar
from datetime import datetime

# Constants
YEAR = 2017

# Functions
# returns datetime.datetime
def parscsv(str_time):
    str_new_time = str(YEAR) + ' ' + str_time
    return datetime.strptime(str_new_time, '%Y %d %m %H %M')

def cmpTimeE(str_time, datetime):
    return parscsv(str_time) == datetime

def cmpTimeGE(str_time, datetime):
    return parscsv(str_time) >= datetime

def cmpTimeLE(str_time, datetime):
    return parscsv(str_time) <= datetime

def cmpTimeG(str_time, datetime):
    return parscsv(str_time) > datetime

def cmpTimeL(str_time, datetime):
    return parscsv(str_time) < datetime

# returns "Filter" - pandas.core.series.Series (True/False)
# timeForCmp - datetime.datetime - time for comparison
def filterTimeCsv(cmpFun, dataFrame, timeForCmp):
    dataLen = len(dataFrame)
    data = [0 for x in range(dataLen)] # TODO: rename var
    for i in range(len(dataFrame)):
        data[i] = cmpFun(dataFrame['time'][i], timeForCmp)
    # return data # this was also working...
    return pd.Series(data, index=list(range(dataLen)))


#### How to create filter from list
# FilterP = pd.Series(data=[True, False, True, True], index=list(range(4)))
# print("FilterP")
# print(FilterP)
# print(type(FilterP))


stats = pd.read_csv('C:\\Users\\glabka\\Dropbox\\Apps\\Plain.txt\\doucovani.txt') # type: dataFrame
stats.columns = ['time', 'money', 'hours', 'subject', 'school', 'name'] # renaming columns

# Filter = filterTimeCsv(cmpTimeG, stats, datetime(2017, 4, 27))
Filter1 = filterTimeCsv(cmpTimeG, stats, datetime(2017, 4, 27))
Filter2 = filterTimeCsv(cmpTimeL, stats, datetime(2017, 5, 12))
Filter = Filter1 & Filter2
print("stats")
print(stats)
print("Filtered stats")
print(stats[Filter])
