#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.8),
    on 四月 08, 2021, at 15:57
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

import socket
import tkinter.messagebox


host = '127.0.0.1'
goodportary =[]
portstart = 9230
for i in range(0,10):
    fg = True
    c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c.settimeout(1.5)
    try:
        c.connect((host,portstart))
    except:
        print('bad port')
        fg = False
    
    if fg :
        goodportary.append(c)
    portstart = portstart + 1

if len(goodportary) == 0:
    tkinter.messagebox.showinfo('错误','脑电采集设备未连接')
    core.quit()



inputData = bytes([0x55,0x01,0x5a,0x07,0x45,0x56,0x45,0x4e,0x54,0x5f,0x41,0xd9])
mark_up = bytes([0x55,0x01,0x5a,0x01,0x0b,0xbc])
mark_down = bytes([0x55,0x01,0x5a,0x01,0x16,0xc7])
mark_left = bytes([0x55,0x01,0x5a,0x01,0x15,0xc6])
mark_rig = bytes([0x55,0x01,0x5a,0x01,0x0c,0xbd])
mark_resrig = bytes([0x55,0x01,0x5a,0x01,0x9a,0x4b])
mark_reswrg = bytes([0x55,0x01,0x5a,0x01,0x9b,0x4c])
mark_start = bytes([0x55,0x01,0x5a,0x01,0x51,0x02])
mark_end = bytes([0x55,0x01,0x5a,0x01,0x52,0x03])
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.8'
expName = "视觉搜索"
expInfo = {'participant': sys.argv[2], 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
datapath = sys.argv[1]
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = datapath + u"/任务脑电_%s_%s" % (expName, expInfo['date'])#hzk

import random
import itertools
altrails = []
showtype = [1, 2, 3, 4]
alltype = []
for x in  itertools.permutations(showtype,4):
    alltype.append(x)
    
for i in range(0,45):
    x = random.randint(0,23)
    altrails.append(x)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='untitled.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "before"
beforeClock = core.Clock()
text_guide = visual.TextStim(win=win, name='text',
    text='您好，欢迎参加本次实验\n在实验过程中，屏幕中央上会呈现一个“+”\n在“+”的四周会呈现很多的方块和一个圆形\n请注视屏幕中央，用余光寻找圆形图案\n当圆形出现在屏幕上方时按“F”做出反应\n当圆形出现在屏幕下方时按“J”做出反应\n明白实验后按空格键进入练习。',
    font='Arial',
    pos=( 0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_1 = visual.TextStim(win=win, name='text_1',
    text='正确',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
polygon =  visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
    
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(0.15, 0.35),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(0.27, 0.27),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon_4 = visual.Rect(
    win=win, name='polygon_4',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(0.4, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=45, depth=-4.0, interpolate=True)
polygon_5 = visual.Rect(
    win=win, name='polygon_5',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(-0.4, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
polygon_6 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
    
target1 = visual.Circle(
    win = win , name = 'target1',
    size = 0.1,
    ori = 0 , pos =(0.35,0.15),
    fillColor=[1,1,1],fillColorSpace='rgb',
    opacity=1,depth=-7.0,interpolate=True)
    
target2 = visual.Circle(
    win = win , name = 'target2',
    size = 0.1,
    ori = 0 , pos =(0.15,-0.35),
    fillColor=[1,1,1],fillColorSpace='rgb',
    opacity=1,depth=-7.0,interpolate=True)
    
target3 = visual.Circle(
    win = win , name = 'target3',
    size = 0.1,
    ori = 0 , pos =(-0.35,-0.15),
    fillColor=[1,1,1],fillColorSpace='rgb',
    opacity=1,depth=-7.0,interpolate=True)
    
target4 = visual.Circle(
    win = win , name = 'target4',
    size = 0.1,
    ori = 0 , pos =(-0.15,0.35),
    fillColor=[1,1,1],fillColorSpace='rgb',
    opacity=1,depth=-7.0,interpolate=True)
    
polygon_7 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(0.35, 0.15),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
    
polygon_8 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(0.35, -0.15),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
    
polygon_9 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(0.27, -0.27),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
    
polygon_10 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(0.15, -0.35),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)

polygon_11 = visual.Rect(
    win=win, name='polygon_11',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(-0.35, -0.15),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
    
polygon_12 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(-0.15, -0.35),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
    
polygon_13 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(-0.27, -0.27),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
    
polygon_14 = visual.Rect(
    win=win, name='polygon_14',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(-0.15, 0.35),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)

polygon_15 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(-0.27, 0.27),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)

polygon_16 = visual.Rect(
    win=win, name='polygon16',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(0, 0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

polygon_17 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=(-0.35, 0.15),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
    
ling = [ polygon_7, polygon_10, polygon_11, polygon_14]
yuan = [ target1 , target2 , target3 , target4]
weizhi = ["f", "j","j","f"]
mark_weizhi = [mark_rig,mark_down,mark_left,mark_up]

alwaysshow = [polygon ,polygon_2, polygon_3, polygon_4, polygon_5, polygon_6,polygon_8,polygon_9,polygon_12,polygon_13,polygon_15,polygon_16,polygon_17]

# Initialize components for Routine "after"
afterClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


# ------Prepare to start Routine "before"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
beforeComponents = [text_guide]
for thisComponent in beforeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beforeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "before"-------
while continueRoutine:
    # get current time
    t = beforeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beforeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text_guide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_guide.frameNStart = frameN  # exact frame index
        text_guide.tStart = t  # local t and not account for scr refresh
        text_guide.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_guide, 'tStartRefresh')  # time at next scr refresh
        text_guide.setAutoDraw(True)

    if defaultKeyboard.getKeys(keyList=["space"]):
        continueRoutine = False
        text_guide.setAutoDraw(False)
        break

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beforeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "before"-------
for thisComponent in beforeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "before" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#练习
flag = True
while flag :
    trials = data.TrialHandler(nReps= 8, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    cur = 0
    cur1 = 0

    for thisTrial in trials:
        k = altrails[(int)(cur/4)]
        y = alltype[k][cur1] -1 
        cur = (cur + 1)
        cur1 = (cur1+1)%4
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(5.050000)
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [text, text_1,text_2, key_resp, polygon,polygon_2, polygon_3, polygon_4, polygon_5, polygon_6,polygon_7,polygon_8,polygon_9,polygon_10,polygon_11,polygon_12,polygon_13,polygon_14,polygon_15,polygon_16,polygon_17,target1,target2,target3,target4]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 2.8-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)

                    # *text_1* updates
            if text_1.status == NOT_STARTED and tThisFlip >= 4.05-frameTolerance:
                # keep track of start time/frame for later
                text_1.frameNStart = frameN  # exact frame index
                text_1.tStart = t  # local t and not account for scr refresh
                text_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
                text_1.setAutoDraw(True)
            if text_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_1.tStop = t  # not accounting for scr refresh
                    text_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_1, 'tStopRefresh')  # time at next scr refresh
                    text_1.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 2.8-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    if len(_key_resp_allKeys) == 0:
                        text_1.text = "错误"
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['f','j','j','f'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                    if key_resp.keys == weizhi[y] :
                        text_1.text = "正确"
                    else:
                        text_1.text = "错误"
                    
            
            for now in alwaysshow:
                # *polygon* updates
                if now.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                    # keep track of start time/frame for later
                    now.frameNStart = frameN  # exact frame index
                    now.tStart = t  # local t and not account for scr refresh
                    now.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip( now , 'tStartRefresh')  # time at next scr refresh
                    now.setAutoDraw(True)
                if now.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > now.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        now.tStop = t  # not accounting for scr refresh
                        now.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(now, 'tStopRefresh')  # time at next scr refresh
                        now.setAutoDraw(False)
            for x in range(0,4):
                now = yuan [x]
                if x == y:
                    now = yuan[x]
                else:
                    now = ling[x]
                if now.status == NOT_STARTED and tThisFlip >= 1.0 - frameTolerance:
                    now.frameNStart = frameN
                    now.tStart = t
                    now.tStartRefresh = tThisFlipGlobal
                    win.timeOnFlip(now,'tStartRefresh')
                    now.setAutoDraw(True)
                if now.status == STARTED:
                    if tThisFlipGlobal > now.tStartRefresh + 0.25-frameTolerance:
                        now.tStop = t
                        now.frameNStop = frameN
                        win.timeOnFlip(now,'tStopRefresh')
                        now.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    routineTimer.reset()
    #选择是否继续
    continueRoutine = True
    text_guide.text = "练习已结束，\n 若您已了解实验操作请按“Y”键，进入正式实验；\n若您还未熟悉实验操作请按“N”健，重新进行练习。"
    # update component parameters for each repeat
    # keep track of which components have finished
    beforeComponents = [text_guide]
    for thisComponent in beforeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    beforeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "before"-------
    while continueRoutine:
        # get current time
        t = beforeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=beforeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text_guide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_guide.frameNStart = frameN  # exact frame index
            text_guide.tStart = t  # local t and not account for scr refresh
            text_guide.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_guide, 'tStartRefresh')  # time at next scr refresh
            text_guide.setAutoDraw(True)

        if defaultKeyboard.getKeys(keyList=["n"]):
            continueRoutine = False
            text_guide.setAutoDraw(False)
            break
        if defaultKeyboard.getKeys(keyList=["y"]):
            flag = False
            continueRoutine = False
            text_guide.setAutoDraw(False)
            break
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not flag:  # a component has requested a forced-end of Routine
            continueRoutine = False
            break
        for thisComponent in beforeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "before"-------
    for thisComponent in beforeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    routineTimer.reset()



# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=180, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')

thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))
cur = 0
cur1 = 0
trials.nReps = int(sys.argv[3])
for thisTrial in trials:
    if cur == 0 :
        for c in goodportary:
            try:
                c.send(mark_start)
            except:
                tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                core.quit()
    
    k = altrails[(int)(cur/4)]
    y = alltype[k][cur1] -1 
    cur = (cur + 1)
    cur1 = (cur1+1)%4
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(4.050000)
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    first = True
    # keep track of which components have finished
    trialComponents = [text, text_2, key_resp, polygon,polygon_2, polygon_3, polygon_4, polygon_5, polygon_6,polygon_7,polygon_8,polygon_9,polygon_10,polygon_11,polygon_12,polygon_13,polygon_14,polygon_15,polygon_16,polygon_17,target1,target2,target3,target4]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
                if first :
                    for c in goodportary:
                        try:
                            c.send(mark_reswrg)
                        except:
                            tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                            core.quit()
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['f','j','j','f'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys) and first:
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                if key_resp.keys == weizhi[y] :
                    for c in goodportary:
                        try:
                            c.send(mark_resrig)
                        except:
                            tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                            core.quit()
                else:
                    for c in goodportary:
                        try:
                            c.send(mark_reswrg)
                        except:
                            tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                            core.quit()
                key_resp.rt = t - alwaysshow[0].tStart
                # a response ends the routine
                first = False

        for now in alwaysshow:
            # *polygon* updates
            if now.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                now.frameNStart = frameN  # exact frame index
                now.tStart = t  # local t and not account for scr refresh
                now.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip( now , 'tStartRefresh')  # time at next scr refresh
                now.setAutoDraw(True)
            if now.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > now.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    now.tStop = t  # not accounting for scr refresh
                    now.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(now, 'tStopRefresh')  # time at next scr refresh
                    now.setAutoDraw(False)
                    
        for x in range(0,4):
            now = yuan [x]
            if x == y:
                now = yuan[x]
            else:
                now = ling[x]
            if now.status == NOT_STARTED and tThisFlip >= 1.0 - frameTolerance:
                now.frameNStart = frameN
                now.tStart = t
                if x == y :
                    for c in goodportary:
                        try:
                            c.send(mark_weizhi[y])
                        except:
                            tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                            core.quit()
                now.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(now,'tStartRefresh')
                now.setAutoDraw(True)
            if now.status == STARTED:
                if tThisFlipGlobal > now.tStartRefresh + 0.25-frameTolerance:
                    now.tStop = t
                    now.frameNStop = frameN
                    win.timeOnFlip(now,'tStopRefresh')
                    now.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('target.started', polygon.tStartRefresh)
    trials.addData('target.stopped', polygon.tStopRefresh)
    trials.addData('target.type' , weizhi[y])
    if(key_resp.keys==weizhi[y]):#hzk
        trials.addData('correct',1)
    else:
        trials.addData('correct',0)
    trials.thisN+=1#hzk
    trials.thisRepN+=1#hzk
    thisExp.nextEntry()
    
# completed 180 repeats of 'trials'


# ------Prepare to start Routine "after"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
afterComponents = []
for thisComponent in afterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
afterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "after"-------
while continueRoutine:
    # get current time
    t = afterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=afterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        for c in goodportary:
            try:
                c.send(mark_end)
            except:
                tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                core.quit()
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in afterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "after"-------
for thisComponent in afterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "after" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()
for c in goodportary:
    try:
        c.send( mark_end)
    except:
        tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
        core.quit()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
for c in goodportary:
    c.close()
core.quit()
