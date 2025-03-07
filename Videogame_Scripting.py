import cv2 as cv
import numpy as np
import pyautogui
import time
import random
from pyclick import HumanClicker

hc = HumanClicker()

cwbank =  cv.imread('D:/Users/Austin E/Downloads/needle.jpg', cv.IMREAD_UNCHANGED)
alter = cv.imread('D:/Users/Austin E/Downloads/needle2.jpg', cv.IMREAD_UNCHANGED)
cave = cv.imread('D:/Users/Austin E/Downloads/needle3.jpg', cv.IMREAD_UNCHANGED)

time.sleep(3) #switching screen time

for i in range(0,4):
    upperpouch = ((1699+random.randrange(10),807+random.randrange(10)))
    lowerpouch = ((1699+random.randrange(10),840+random.randrange(10)))
    
    pyautogui.press('f3') #open equip and tele to duel arena
    duelclick = (1818+random.randrange(10),919+random.randrange(10))
    hc.move(duelclick,random.triangular(.2,.33))
    pyautogui.click(button = 'right')
    pyautogui.moveTo(duelclick[0],duelclick[1]+40)
    time.sleep(.5)
    pyautogui.click()
    
    time.sleep(3.5) #tele time
    
    screen = pyautogui.screenshot('D:/Users/Austin E/Downloads/screen.jpg')
    haystack_img = cv.imread('D:/Users/Austin E/Downloads/screen.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, alter, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    
    if max_val < .60:
        hc.move((944+random.randrange(10),461+random.randrange(10)),random.triangular(.2,.33))
        pyautogui.click()
        time.sleep(2)
    screen = pyautogui.screenshot('D:/Users/Austin E/Downloads/screen.jpg')
    haystack_img = cv.imread('D:/Users/Austin E/Downloads/screen.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, alter, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    
    alterloc = max_loc
    
    hc.move((alterloc[0]+40,alterloc[1]+40),random.triangular(.4,.45))
    pyautogui.click()
    time.sleep(8)
    
    
    hc.move((1311+random.randrange(10),883+random.randrange(10)),random.triangular(.4,.45))
    pyautogui.click()
    time.sleep(.5)
    pyautogui.press('f2')
    hc.move((1761+random.randrange(10),887+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.5)
    pyautogui.press('esc')
    time.sleep(2)
    hc.move((1699+random.randrange(10),765+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.3)
    hc.move((982+random.randrange(10),551+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    hc.move((upperpouch),random.triangular(.2,.33))
    pyautogui.click(button = 'right')
    time.sleep(random.triangular(.2,.37))
    pyautogui.moveTo((upperpouch[0],upperpouch[1]+40))
    pyautogui.click()
    time.sleep(random.triangular(.2,.37))
    hc.move((lowerpouch),random.triangular(.2,.33))
    pyautogui.click(button = 'right')
    time.sleep(.2)
    pyautogui.moveTo((lowerpouch[0],lowerpouch[1]+40))
    pyautogui.click()
    time.sleep(.2)
    hc.move((1699+random.randrange(10),765+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.3)
    hc.move((982+random.randrange(10),551+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(1.3)
    
    pyautogui.press('f3')
    castleclick = (1818+random.randrange(10),919+random.randrange(10))
    hc.move(castleclick,random.triangular(.3,.44))
    pyautogui.click(button = 'right')
    pyautogui.moveTo(castleclick[0],castleclick[1]+56)
    time.sleep(.5)
    pyautogui.click()
    
    time.sleep(3.5)
    
    screen = pyautogui.screenshot('D:/Users/Austin E/Downloads/screen.jpg')
    haystack_img = cv.imread('D:/Users/Austin E/Downloads/screen.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, cwbank, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    cwbankloc = max_loc
    
    hc.move((cwbankloc[0]+30,cwbankloc[1]+30),random.triangular(.4,.45))
    pyautogui.click()
    time.sleep(3.5)
    
    hc.move((1742+random.randrange(10),766+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    hc.move((981+random.randrange(10),644+random.randrange(10)),random.triangular(.3,.45))
    pyautogui.click()
    
    hc.move((upperpouch),random.triangular(.3,.38))
    pyautogui.click(button = 'right')
    time.sleep(random.triangular(.2,.37))
    pyautogui.moveTo((upperpouch[0],upperpouch[1]+130))
    pyautogui.click()
    time.sleep(random.triangular(.2,.37))
    hc.move((lowerpouch),random.triangular(.3,.38))
    pyautogui.click(button = 'right')
    time.sleep(.2)
    pyautogui.moveTo((lowerpouch[0],lowerpouch[1]+130))
    pyautogui.click()
    time.sleep(.2)
    hc.move((1742+random.randrange(10),766+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.3)
    hc.move((981+random.randrange(10),644+random.randrange(10)),random.triangular(.3,.45))
    pyautogui.click()
    time.sleep(.5)
    pyautogui.press('esc')
    
    ######################################################################################## RUN 2
    
    upperpouch = ((1699+random.randrange(10),807+random.randrange(10)))
    lowerpouch = ((1699+random.randrange(10),840+random.randrange(10)))
    
    pyautogui.press('f3') #open equip and tele to duel arena
    duelclick = (1818+random.randrange(10),919+random.randrange(10))
    hc.move(duelclick,random.triangular(.2,.33))
    pyautogui.click(button = 'right')
    pyautogui.moveTo(duelclick[0],duelclick[1]+40)
    time.sleep(.5)
    pyautogui.click()
    
    time.sleep(3.5) #tele time
    
    screen = pyautogui.screenshot('D:/Users/Austin E/Downloads/screen.jpg')
    haystack_img = cv.imread('D:/Users/Austin E/Downloads/screen.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, alter, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    
    if max_val < .60:
        hc.move((944+random.randrange(10),461+random.randrange(10)),random.triangular(.2,.33))
        pyautogui.click()
        time.sleep(2)
    screen = pyautogui.screenshot('D:/Users/Austin E/Downloads/screen.jpg')
    haystack_img = cv.imread('D:/Users/Austin E/Downloads/screen.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, alter, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    
    alterloc = max_loc
    
    hc.move((alterloc[0]+40,alterloc[1]+40),random.triangular(.4,.45))
    pyautogui.click()
    time.sleep(8)
    
    
    hc.move((1311+random.randrange(10),883+random.randrange(10)),random.triangular(.4,.45))
    pyautogui.click()
    time.sleep(.5)
    pyautogui.press('f2')
    hc.move((1761+random.randrange(10),887+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.5)
    pyautogui.press('esc')
    time.sleep(2)
    hc.move((1699+random.randrange(10),765+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.3)
    hc.move((982+random.randrange(10),551+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    hc.move((upperpouch),random.triangular(.2,.33))
    pyautogui.click(button = 'right')
    time.sleep(random.triangular(.2,.37))
    pyautogui.moveTo((upperpouch[0],upperpouch[1]+40))
    pyautogui.click()
    time.sleep(random.triangular(.2,.37))
    hc.move((lowerpouch),random.triangular(.2,.33))
    pyautogui.click(button = 'right')
    time.sleep(.2)
    pyautogui.moveTo((lowerpouch[0],lowerpouch[1]+40))
    pyautogui.click()
    time.sleep(.2)
    hc.move((1699+random.randrange(10),765+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.3)
    hc.move((982+random.randrange(10),551+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(1.3)
    
    pyautogui.press('f3')
    castleclick = (1818+random.randrange(10),919+random.randrange(10))
    hc.move(castleclick,random.triangular(.3,.44))
    pyautogui.click(button = 'right')
    pyautogui.moveTo(castleclick[0],castleclick[1]+56)
    time.sleep(.5)
    pyautogui.click()
    
    time.sleep(3.5)
    
    screen = pyautogui.screenshot('D:/Users/Austin E/Downloads/screen.jpg')
    haystack_img = cv.imread('D:/Users/Austin E/Downloads/screen.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, cwbank, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    cwbankloc = max_loc
    
    hc.move((cwbankloc[0]+30,cwbankloc[1]+30),random.triangular(.4,.45))
    pyautogui.click()
    time.sleep(3.5)
    
    hc.move((1742+random.randrange(10),766+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    hc.move((981+random.randrange(10),644+random.randrange(10)),random.triangular(.3,.45))
    pyautogui.click()
    
    hc.move((upperpouch),random.triangular(.3,.38))
    pyautogui.click(button = 'right')
    time.sleep(random.triangular(.2,.37))
    pyautogui.moveTo((upperpouch[0],upperpouch[1]+130))
    pyautogui.click()
    time.sleep(random.triangular(.2,.37))
    hc.move((lowerpouch),random.triangular(.3,.38))
    pyautogui.click(button = 'right')
    time.sleep(.2)
    pyautogui.moveTo((lowerpouch[0],lowerpouch[1]+130))
    pyautogui.click()
    time.sleep(.3)
    hc.move((981+random.randrange(10),644+random.randrange(10)),random.triangular(.3,.45))
    pyautogui.click()
    time.sleep(.5)
    pyautogui.press('esc')
    
    ######################################################################################## RUN 3
    
    upperpouch = ((1699+random.randrange(10),807+random.randrange(10)))
    lowerpouch = ((1699+random.randrange(10),840+random.randrange(10)))
    
    pyautogui.press('f3') #open equip and tele to duel arena
    duelclick = (1818+random.randrange(10),919+random.randrange(10))
    hc.move(duelclick,random.triangular(.2,.33))
    pyautogui.click(button = 'right')
    pyautogui.moveTo(duelclick[0],duelclick[1]+40)
    time.sleep(.5)
    pyautogui.click()
    
    time.sleep(3.5) #tele time
    
    screen = pyautogui.screenshot('D:/Users/Austin E/Downloads/screen.jpg')
    haystack_img = cv.imread('D:/Users/Austin E/Downloads/screen.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, alter, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    
    if max_val < .60:
        hc.move((944+random.randrange(10),461+random.randrange(10)),random.triangular(.2,.33))
        pyautogui.click()
        time.sleep(2)
    screen = pyautogui.screenshot('D:/Users/Austin E/Downloads/screen.jpg')
    haystack_img = cv.imread('D:/Users/Austin E/Downloads/screen.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, alter, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    
    alterloc = max_loc
    
    hc.move((alterloc[0]+40,alterloc[1]+40),random.triangular(.4,.45))
    pyautogui.click()
    time.sleep(8)
    
    
    hc.move((1311+random.randrange(10),883+random.randrange(10)),random.triangular(.4,.45))
    pyautogui.click()
    time.sleep(.5)
    pyautogui.press('f2')
    hc.move((1761+random.randrange(10),887+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.5)
    pyautogui.press('esc')
    time.sleep(2)
    hc.move((1699+random.randrange(10),765+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.3)
    hc.move((982+random.randrange(10),551+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    hc.move((upperpouch),random.triangular(.2,.33))
    pyautogui.click(button = 'right')
    time.sleep(random.triangular(.2,.37))
    pyautogui.moveTo((upperpouch[0],upperpouch[1]+40))
    pyautogui.click()
    time.sleep(random.triangular(.2,.37))
    hc.move((lowerpouch),random.triangular(.2,.33))
    pyautogui.click(button = 'right')
    time.sleep(.2)
    pyautogui.moveTo((lowerpouch[0],lowerpouch[1]+40))
    pyautogui.click()
    time.sleep(.2)
    hc.move((1699+random.randrange(10),765+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.3)
    hc.move((982+random.randrange(10),551+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(1.3)
    
    pyautogui.press('f3')
    castleclick = (1818+random.randrange(10),919+random.randrange(10))
    hc.move(castleclick,random.triangular(.3,.44))
    pyautogui.click(button = 'right')
    pyautogui.moveTo(castleclick[0],castleclick[1]+56)
    time.sleep(.5)
    pyautogui.click()
    
    time.sleep(3.5)
    
    screen = pyautogui.screenshot('D:/Users/Austin E/Downloads/screen.jpg')
    haystack_img = cv.imread('D:/Users/Austin E/Downloads/screen.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, cwbank, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    cwbankloc = max_loc
    
    hc.move((cwbankloc[0]+30,cwbankloc[1]+30),random.triangular(.4,.45))
    pyautogui.click()
    time.sleep(3.5)
    
    hc.move((1742+random.randrange(10),766+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    hc.move((981+random.randrange(10),644+random.randrange(10)),random.triangular(.3,.45))
    pyautogui.click()
    
    hc.move((upperpouch),random.triangular(.3,.38))
    pyautogui.click(button = 'right')
    time.sleep(random.triangular(.2,.37))
    pyautogui.moveTo((upperpouch[0],upperpouch[1]+130))
    pyautogui.click()
    time.sleep(random.triangular(.2,.37))
    hc.move((lowerpouch),random.triangular(.3,.38))
    pyautogui.click(button = 'right')
    time.sleep(.2)
    pyautogui.moveTo((lowerpouch[0],lowerpouch[1]+130))
    pyautogui.click()
    time.sleep(.3)
    hc.move((981+random.randrange(10),644+random.randrange(10)),random.triangular(.3,.45))
    pyautogui.click()
    time.sleep(.5)
    pyautogui.press('esc')
    
    ######################################################################################## RUN 4
    
    upperpouch = ((1699+random.randrange(10),807+random.randrange(10)))
    lowerpouch = ((1699+random.randrange(10),840+random.randrange(10)))
    
    pyautogui.press('f3') #open equip and tele to duel arena
    duelclick = (1818+random.randrange(10),919+random.randrange(10))
    hc.move(duelclick,random.triangular(.2,.33))
    pyautogui.click(button = 'right')
    pyautogui.moveTo(duelclick[0],duelclick[1]+40)
    time.sleep(.5)
    pyautogui.click()
    
    time.sleep(3.5) #tele time
    
    screen = pyautogui.screenshot('D:/Users/Austin E/Downloads/screen.jpg')
    haystack_img = cv.imread('D:/Users/Austin E/Downloads/screen.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, alter, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    
    if max_val < .60:
        hc.move((944+random.randrange(10),461+random.randrange(10)),random.triangular(.2,.33))
        pyautogui.click()
        time.sleep(2)
    screen = pyautogui.screenshot('D:/Users/Austin E/Downloads/screen.jpg')
    haystack_img = cv.imread('D:/Users/Austin E/Downloads/screen.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, alter, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    
    alterloc = max_loc
    
    hc.move((alterloc[0]+40,alterloc[1]+40),random.triangular(.4,.45))
    pyautogui.click()
    time.sleep(8)
    
    
    hc.move((1311+random.randrange(10),883+random.randrange(10)),random.triangular(.4,.45))
    pyautogui.click()
    time.sleep(.5)
    pyautogui.press('f2')
    hc.move((1761+random.randrange(10),887+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.5)
    pyautogui.press('esc')
    time.sleep(2)
    hc.move((1699+random.randrange(10),765+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.3)
    hc.move((982+random.randrange(10),551+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    hc.move((upperpouch),random.triangular(.2,.33))
    pyautogui.click(button = 'right')
    time.sleep(random.triangular(.2,.37))
    pyautogui.moveTo((upperpouch[0],upperpouch[1]+40))
    pyautogui.click()
    time.sleep(random.triangular(.2,.37))
    hc.move((lowerpouch),random.triangular(.2,.33))
    pyautogui.click(button = 'right')
    time.sleep(.2)
    pyautogui.moveTo((lowerpouch[0],lowerpouch[1]+40))
    pyautogui.click()
    time.sleep(.2)
    hc.move((1699+random.randrange(10),765+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.3)
    hc.move((982+random.randrange(10),551+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(1.3)
    
    pyautogui.press('f3')
    castleclick = (1818+random.randrange(10),919+random.randrange(10))
    hc.move(castleclick,random.triangular(.3,.44))
    pyautogui.click(button = 'right')
    pyautogui.moveTo(castleclick[0],castleclick[1]+56)
    time.sleep(.5)
    pyautogui.click()
    
    time.sleep(3.5)
    
    screen = pyautogui.screenshot('D:/Users/Austin E/Downloads/screen.jpg')
    haystack_img = cv.imread('D:/Users/Austin E/Downloads/screen.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, cwbank, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    cwbankloc = max_loc
    
    hc.move((cwbankloc[0]+30,cwbankloc[1]+30),random.triangular(.4,.45))
    pyautogui.click()
    time.sleep(3.5)
    
    hc.move((1742+random.randrange(10),766+random.randrange(10)),random.triangular(.2,.33))
    pyautogui.click()
    time.sleep(.2)
    ringwithdraw = (979+random.randrange(10),611+random.randrange(10))
    hc.move((ringwithdraw),random.triangular(.3,.45))
    pyautogui.click(button = 'right')
    time.sleep(.2)
    pyautogui.moveTo((ringwithdraw[0],ringwithdraw[1]+40))
    time.sleep(.2)
    pyautogui.click()
    time.sleep(.3)
    pyautogui.press('esc')
    time.sleep(.2)
    pyautogui.press('esc')
    hc.move((1741+random.randrange(10),766+random.randrange(10)),random.triangular(.3,.45))
    pyautogui.click()
    time.sleep(.2)
    hc.move((977+random.randrange(10),537+random.randrange(10)),random.triangular(.3,.45))
    pyautogui.click()
    time.sleep(.3)
    
    hc.move((981+random.randrange(10),644+random.randrange(10)),random.triangular(.3,.45))
    pyautogui.click()
    
    hc.move((upperpouch),random.triangular(.3,.38))
    pyautogui.click(button = 'right')
    time.sleep(random.triangular(.2,.37))
    pyautogui.moveTo((upperpouch[0],upperpouch[1]+130))
    pyautogui.click()
    time.sleep(random.triangular(.2,.37))
    hc.move((lowerpouch),random.triangular(.3,.38))
    pyautogui.click(button = 'right')
    time.sleep(.2)
    pyautogui.moveTo((lowerpouch[0],lowerpouch[1]+130))
    pyautogui.click()
    time.sleep(.3)
    hc.move((981+random.randrange(10),644+random.randrange(10)),random.triangular(.3,.45))
    pyautogui.click()
    time.sleep(.5)
    pyautogui.press('esc')
