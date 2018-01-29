import pyautogui as pg
import time
import webbrowser

points = 0

answer = pg.prompt(
"""
Whats your faviorote city
a)los angelas 
b)chicago 
c)boston 


"""
    )

if answer == "a" :
    points += 1
if answer == "b" :
    points += 2
if answer == "c" :
    points += 3

answer = pg.prompt(
"""
Whats your faviorote baseball team
a)dogeres  
b)cuba
c)red sox



"""
    )

if answer == "a" :
    points += 1
if answer == "b" :
    points += 2
if answer == "c" :    
    points += 3

answer = pg.prompt(
"""
Whats your favirot plannet 
a)mars 
b)jupiter 
c)uranus 


"""
    )

if answer == "a" :
    points += 1
if answer == "b" :
    points += 2
if answer == "c" :
    points += 3




#wnding
if points <5:
    pg.alert("yuo are the LA Rams")
    webbrowser.open ("https://www.youtube.com/watch?v=I1y0L06pcwg")

elif points >= 5 and points < 7:
    pg.alert ("you are the are the chicogo bears")
    webbrowser.open ("https://www.youtube.com/watch?v=wkXzJZ-bV_g")

elif points >= 7:
    pg.alert ("you are the new england patriots")
    webbrowser.open ("https://www.youtube.com/watch?v=016LXFHpFCk")



    
