#!/usr/bin/env python3

def getActiveCookie(lines, date):
    '''Given lines read from cookie file, find the most active cookie(s).'''
    cookieCounts = {}
    for line in lines:
        line = line.strip()
        cookie, timestamp = line.split(",")
        timestamp = timestamp[:10]
        if date == timestamp:
            if cookie not in cookieCounts:
                cookieCounts[cookie] = 0
            cookieCounts[cookie] += 1
    
    maxActivity = max(list(cookieCounts.values())) if cookieCounts else 0

    return [key for key, value in cookieCounts.items() if value == maxActivity]

def getActiveCookieFile(filepath, date):
    '''Given filepath as a string, find the most active cookie(s).'''
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
        
        assert lines[0] == "cookie,timestamp\n"
        
        bestCookies = getActiveCookie(lines, date)

        return "\n".join(bestCookies)
    except AssertionError:
        print("Input file header is not cookie,timestamp")        
    except FileNotFoundError:
        print("File not found at", filepath)