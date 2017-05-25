import numpy
import pandas as pd
import matplotlib.pyplot as plt
import calendar
from datetime import datetime

# Functions
# returns datetime.datetime
def parscsv(str_time):
    return datetime.strptime(str_time, '%d %m %H %M')

def cmpTimeE(str_time1, str_time2):
    return parscsv(str_time1) == parscsv(str_time2)

def cmpTimeGE(str_time1, str_time2):
    return parscsv(str_time1) >= parscsv(str_time2)

def cmpTimeLE(str_time1, str_time2):
    return parscsv(str_time1) <= parscsv(str_time2)

def cmpTimeG(str_time1, str_time2):
    return parscsv(str_time1) > parscsv(str_time2)

def cmpTimeL(str_time1, str_time2):
    return parscsv(str_time1) < parscsv(str_time2)

# return "Filter" - pandas.core.series.Series
# dateForCmp - datetime.datetime - date for comparison
def filterTimeCsv(dataFrame, cmpFun, dateForCmp):
    data = [0 for x in range(len(stats))] # TODO: rename var
    for i in range(len(stats)):
        data[i] = cmpFun(stats.date['date'][i], dateForCmp) # TODO
    # print(data)
    return

#### How to create filter from list
# FilterP = pd.Series(data=[True, False, True, True], index=list(range(4)))
# print("FilterP")
# print(FilterP)
# print(type(FilterP))



# TODO - create function that will create filter (pandas.core.series.Series) - use cmp-fun

stats = pd.read_csv('C:\\Users\\glabka\\Dropbox\\Apps\\Plain.txt\\doucovani.txt') # type: dataFrame
stats.columns = ['time', 'money', 'hours', 'subject', 'school', 'name'] # renaming columns
print(stats)
print('-_(((((((((((((((((((((((((0')
stats = stats[1:] # deleting first row (comment in csv file)
print(stats)
print('-_(((((((((((((((((((((((((1')
indexes = list(range(len(stats)))
stats = stats.reindex(indexes)


# Calendar
## itermonthdays2
## monthdays2calendar
cal = calendar.Calendar()
print(cal.monthdays2calendar(2016, 5))
#######

# print(type(datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')))
print(stats)
print('-_(((((((((((((((((((((((((2')
# print(stats[0]['date'])
print(stats['date'][1])
print('-_(((((((((((((((((((((((((3')

# Filter1 = filterTimeCsv(stats, cmpTimeGE, datetime(2017, 2, 5))

# print(Filter1)
# print(datetime(2017, 2, 5))
# print(type(datetime(2017, 2, 5)))
