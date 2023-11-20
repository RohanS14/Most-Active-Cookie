#!/usr/bin/env python3

import os, sys

# add current working directory to path
sys.path.insert(0, os.getcwd())

import pytest
from cookie_logic import *

def testEmpty():
    '''Check that nothing is returned for no cookies'''
    assert getActiveCookieFile("data/empty.csv", "2018-12-09") == ""

def testOneCookie():
    '''Check that the only cookie is returned for a single cookie'''
    assert getActiveCookieFile("data/one.csv", "2018-12-08") == "4sMM2LxV07bPJzwf"

def testNoCookie():
    '''Check that nothing is returned if no cookie active on the specified day.'''
    assert getActiveCookieFile("data/example.csv", "2018-12-10") == ""

def testAllOneCookie():
    '''Check that the only cookie is returned for a single repeated cookie'''
    assert getActiveCookieFile("data/allone.csv", "2018-12-09") == "AtY0laUfhglK3lC7"

def testUniqueCookie():
    '''Find unique most active cookie (first provided example)'''
    assert getActiveCookieFile("data/example.csv", "2018-12-09") == "AtY0laUfhglK3lC7"

def testTiedCookie():
    '''Find multiple cookies tied for most active (second provided example)'''
    output = ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
    assert getActiveCookieFile("data/example.csv", "2018-12-08") == "\n".join(output)

def testAllTiedCookie():
    '''All cookies tied for most active'''
    output = ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA", "5UAVanZf6UtGyKVS"]
    assert getActiveCookieFile("data/alltied.csv", "2018-12-09") == "\n".join(output)

def testLong():
    '''Large dataset example'''
    output = ["4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
    assert getActiveCookieFile("data/large.csv", "2018-12-08") == "\n".join(output)
