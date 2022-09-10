#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.8),
    on 六月 27, 2021, at 18:47
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

from psychopy.hardware import keyboard
import random
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
mark_fenxin = bytes([0x55,0x01,0x5a,0x01,0x01,0xb2])
mark_mubiao = bytes([0x55,0x01,0x5a,0x01,0x02,0xb3])
mark_resrig = bytes([0x55,0x01,0x5a,0x01,0x9a,0x4b])
mark_reswrg = bytes([0x55,0x01,0x5a,0x01,0x9b,0x4c])
mark_start = bytes([0x55,0x01,0x5a,0x01,0x51,0x02])
mark_end = bytes([0x55,0x01,0x5a,0x01,0x52,0x03])

expName = '持续性注意 - 脑电'  # from the Builder filename that created this script
datapath = sys.argv[1]
alt = int(sys.argv[3]) 
try_num = [0,1,2,7,4,5,6,7,8,9,7,5,6,7,3,2]
shownum = []
cnt = 0 
pre = -1
while cnt < alt:
    x = random.randint(0,9)
    if x == pre or x == 7:
        continue
    else:
        shownum.append(x)
    cnt = cnt+1
    pre = x

cnt = 0
while cnt < int(alt/4):
    x = random.randint(0 ,alt-1)
    if shownum[x] == 7:
        continue
    if x > 1 and shownum[x-1] == 7:
        continue
    shownum[x] = 7
    cnt = cnt + 1


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.8'
expInfo = {'participant': sys.argv[2], 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = datapath + u"/任务脑电_%s_%s" % (expName, expInfo['date'])#hzk

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\26633\\Desktop\\cpt.py',
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
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
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

# Initialize components for Routine "实验指导"
实验指导Clock = core.Clock()
beforeClock = core.Clock()
text_guide = visual.TextStim(win=win, name='text',
    text='您好，欢迎参加本次实验\n在实验过程中，屏幕中央会呈现一个“＋”\n在“＋”消失后会出现一张图片，请做如下反应：\n若图片上的动物不是狮子时则单击空格键\n若是狮子则不进行任何操作\n请在保证正确的前提下尽快进行反应\n明白实验后按空格键进行练习。',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "训练模式"
训练模式Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='img/5.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

text_2 = visual.TextStim(win=win, name='text_2',
    text="正确",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "实验内容"
实验内容Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='img/2.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='img/3.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='img/4.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='img/5.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='img/6.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='img/7.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='img/8.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='img/9.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='img/1.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

text_4 = visual.TextStim(win=win, name='text_4',
    text= '+',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "实验指导"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
实验指导Components = [text_guide]
for thisComponent in 实验指导Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
实验指导Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "实验指导"-------
while continueRoutine:
    # get current time
    t = 实验指导Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=实验指导Clock)
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
    for thisComponent in 实验指导Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "实验指导"-------
for thisComponent in 实验指导Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "实验指导" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

flag = True
while flag:
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=16, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    i = -1;
    for thisTrial in trials:
        i=i+1
        
        image.image = "img/"+str(try_num[i])+".png"
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "训练模式"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        first = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        训练模式Components = [text, image, key_resp, text_2]
        for thisComponent in 训练模式Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        训练模式Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "训练模式"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = 训练模式Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=训练模式Clock)
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
                if tThisFlipGlobal > text.tStartRefresh + 1.4-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
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
                if tThisFlipGlobal > key_resp.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    if first:
                        if try_num[i] == 7:
                            text_2.text = "正确"
                        else:
                            text_2.text = "错误"
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys) and first :
                    if try_num[i] != 7:
                        text_2.text = "正确"
                    else:
                        text_2.text = "错误"
                    first = False
            

            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 0.6-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in 训练模式Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "训练模式"-------
        for thisComponent in 训练模式Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
    routineTimer.reset()
    
    continueRoutine = True
    text_guide.text = "练习已结束，\n若您已了解本实验操作请按“Y”键，进入正式实验；\n若您还未熟悉实验操作请按“N”键，重新进行练习。"
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

# completed 10 repeats of 'trials'

i = -1;

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=300, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

trials_2.nReps = int(sys.argv[3])        

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    correct = 0#hzk
    i = i+1;
    if i == 1 :
        for c in goodportary:
            try:
                c.send(mark_start)
            except:
                tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                core.quit()
    react = 1.0
    image_2.image = "img/"+str(shownum[i])+".png"
    rantime = random.randint(2,6)
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "实验内容"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    first = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_2
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    实验内容Components = [text_3, image_2, key_resp,  text_4]
    for thisComponent in 实验内容Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    实验内容Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "实验内容"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = 实验内容Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=实验内容Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)

                # *text_3* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + rantime*1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh

            if shownum[i] != 7 :
                for c in goodportary:
                    try:
                        c.send(mark_mubiao)
                    except:
                        tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                        core.quit()
            else:
                for c in goodportary:
                    try:
                        c.send(mark_fenxin)
                    except:
                        tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                        core.quit()

            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)

       # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
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
            if tThisFlipGlobal > key_resp.tStartRefresh + 1.2 -frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
                if first :
                    if shownum[i] != 7:
                        for c in goodportary:
                            try:
                                c.send(mark_reswrg)
                            except:
                                tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                                core.quit()
                    else:
                        for c in goodportary:
                            try:
                                c.send(mark_resrig)
                            except:
                                tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                                core.quit()
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys) and first:
                react  = t - key_resp.tStart
                if shownum[i] != 7 :
                    correct = 1#hzk
                    for c in goodportary:
                        try:
                            c.send(mark_resrig)
                        except:
                            tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                            core.quit()
                else :
                    for c in goodportary:
                        try:
                            c.send(mark_reswrg)
                        except:
                            tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                            core.quit()
                first = False
                
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            for c in goodportary:
                try:
                    c.send( mark_end)
                except:
                    tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in 实验内容Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "实验内容"-------
    for thisComponent in 实验内容Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    trials_2.addData('imagenum', shownum[i])
    # store data for trials_2 (TrialHandler)
    trials_2.addData('reacttiem',react)
    trials_2.addData('correct',correct)#hzk
    trials_2.thisN+=1#hzk
    trials_2.thisRepN+=1#hzks
    thisExp.nextEntry()

for c in goodportary:
    try:
        c.send( mark_end)
    except:
        tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
        core.quit()
# completed 5 repeats of 'trials_2'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

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
