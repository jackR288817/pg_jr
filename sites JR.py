import webbrowser
import pyautogui as pg


videos = ["https://www.youtube.com/watch?v=hITRkroHGgI", "https://www.youtube.com/watch?v=y43FolFlY78", "https://www.youtube.com/watch?v=tTMk_Uljn_g"]

movies = [""]


answer = pg.prompt (
    """
what would you like to do?

a) watch videos
b) watch movies

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)




elif answer == "b":
    for i in music:
        webbrowser.open(i) 
