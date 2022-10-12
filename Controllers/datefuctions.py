#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:13:57 2021

@author: keshav
"""

import datetime
from datetime import timedelta, date
import calendar
def today():
    if calendar.day_name[date.today().weekday()] == 'Saturday':
        return date.today() + timedelta(days=-1)
    if calendar.day_name[date.today().weekday()] == 'Sunday':
        return date.today() + timedelta(days=-2)
    return date.today()

def week():
    return date.today() + timedelta(days=-7)
def month():
    r = date.today() + timedelta(days=-30)
    if calendar.day_name[r.weekday()] == 'Saturday':
        return r + timedelta(days=-1)
    if calendar.day_name[r.weekday()] == 'Sunday':
        return r + timedelta(days=-2)
    return r

def threemonth():
    r = date.today() + timedelta(days=-90)
    if calendar.day_name[r.weekday()] == 'Saturday':
        return r + timedelta(days=-1)
    if calendar.day_name[r.weekday()] == 'Sunday':
        return r + timedelta(days=-2)
    return r

def sixmonth():
    r = date.today() + timedelta(days=-180)
    if calendar.day_name[r.weekday()] == 'Saturday':
        return r + timedelta(days=-1)
    if calendar.day_name[r.weekday()] == 'Sunday':
        return r + timedelta(days=-2)
    return r

def year():
    r = date.today() + timedelta(days=-360)
    if calendar.day_name[r.weekday()] == 'Saturday':
        return r + timedelta(days=-1)
    if calendar.day_name[r.weekday()] == 'Sunday':
        return r + timedelta(days=-2)
    return r

def genraldate(k):
    r = date.today() + timedelta(days=-k)
    if calendar.day_name[r.weekday()] == 'Saturday':
        return r + timedelta(days=-1)
    if calendar.day_name[r.weekday()] == 'Sunday':
        return r + timedelta(days=-2)
    return r

# print(today())
# print(week())
# print(month())
# print(threemonth())
# print(sixmonth())
# print(year())
#print(datetime.datetime.today().weekday())

