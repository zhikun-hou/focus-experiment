#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 九月 18, 2022, at 23:58
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from loader import *
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from variable_init
#创建变量时不需要$，引用时才需要



# TEXT CONFIG
guide_text = "您好，欢迎参加本次实验\n在实验过程中，屏幕中央会呈现一个“＋”\n在“＋”消失后会出现一个数字，请做如下反应：\n若数字为7则单击鼠标左键，若不是“7”则不进行任何操作\n请在保证正确的前提下尽快进行反应\n明白实验后按空格键进入练习。"
practice_confirm_text = "练习已结束\n若您已了解本实验操作请按“Y”键，进入正式实验；\n若您还未熟悉实验操作请按“N”键，重新进行练习。"
experiment_rest_text = "请休息一下，当您觉得状态恢复良好时\n可随时按空格键继续。"
experiment_end_text = "试验结束，感谢参与\n按空格退出"

# CONDITIONAL FLAG
experiment_stage = "before_experiment"

# PRACTICE CONFIG
practice_repeats = 8
practice_positive_examples = 4

# EXPERIMENT CONFIG
experiment_block_nums = 4
experiment_block_trials = 110
experiment_positive_examples = 80


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'cpt'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
# dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
# if dlg.OK == False:
#     core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
# thisExp = data.ExperimentHandler(name=expName, version='',
#     extraInfo=expInfo, runtimeInfo=None,
#     originPath='E:\\Work\\focus-experiment\\src\\tasks\\project\\cpt.py',
#     savePickle=True, saveWideText=True,
#     dataFileName=filename)
# save a log file for detail verbose info
# logFile = logging.LogFile(filename+'.log', level=logging.EXP)
# logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "init" ---
# Run 'Begin Experiment' code from variable_init



# CONDITIONAL FLAG
experiment_stage = "begin_experiment"

# --- Initialize components for Routine "guide" ---
guide_tip = visual.TextStim(win=win, name='guide_tip',
    text=guide_text,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
guide_skip_trigger = keyboard.Keyboard()

# --- Initialize components for Routine "practice_prepare" ---

# --- Initialize components for Routine "practice_trial" ---
practice_cross = visual.TextStim(win=win, name='practice_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
practice_number = visual.TextStim(win=win, name='practice_number',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
practice_response = event.Mouse(win=win)
x, y = [None, None]
practice_response.mouseClock = core.Clock()

# --- Initialize components for Routine "practice_feedback" ---
practice_response_tip = visual.TextStim(win=win, name='practice_response_tip',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "practice_confirm" ---
practice_confirm_tip = visual.TextStim(win=win, name='practice_confirm_tip',
    text=practice_confirm_text,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practice_confirm_trigger = keyboard.Keyboard()

# --- Initialize components for Routine "experiment_prepare" ---

# --- Initialize components for Routine "experiment_trial" ---
experiment_cross = visual.TextStim(win=win, name='experiment_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
experiment_number = visual.TextStim(win=win, name='experiment_number',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
experiment_response = event.Mouse(win=win)
x, y = [None, None]
experiment_response.mouseClock = core.Clock()

# --- Initialize components for Routine "experiment_rest" ---
experiment_rest_tip = visual.TextStim(win=win, name='experiment_rest_tip',
    text=experiment_rest_text,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
experiment_rest_skip_trigger = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "init" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from variable_init

# CONDITIONAL FLAG
experiment_stage = "init"
# keep track of which components have finished
initComponents = []
for thisComponent in initComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "init" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "init" ---
for thisComponent in initComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from variable_init



# CONDITIONAL FLAG
experiment_stage = "init.end"
# the Routine "init" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop = data.TrialHandler(nReps=65535.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice_loop')
# thisExp.addLoop(practice_loop)  # add the loop to the experiment
thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop:
        exec('{} = thisPractice_loop[paramName]'.format(paramName))

for thisPractice_loop in practice_loop:
    currentLoop = practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            exec('{} = thisPractice_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "guide" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    guide_skip_trigger.keys = []
    guide_skip_trigger.rt = []
    _guide_skip_trigger_allKeys = []
    # Run 'Begin Routine' code from code
    
    # CONDITIONAL FLAG
    experiment_stage = "guide"
    # keep track of which components have finished
    guideComponents = [guide_tip, guide_skip_trigger]
    for thisComponent in guideComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "guide" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *guide_tip* updates
        if guide_tip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            guide_tip.frameNStart = frameN  # exact frame index
            guide_tip.tStart = t  # local t and not account for scr refresh
            guide_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(guide_tip, 'tStartRefresh')  # time at next scr refresh
            guide_tip.setAutoDraw(True)
        
        # *guide_skip_trigger* updates
        waitOnFlip = False
        if guide_skip_trigger.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            guide_skip_trigger.frameNStart = frameN  # exact frame index
            guide_skip_trigger.tStart = t  # local t and not account for scr refresh
            guide_skip_trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(guide_skip_trigger, 'tStartRefresh')  # time at next scr refresh
            guide_skip_trigger.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(guide_skip_trigger.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(guide_skip_trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if guide_skip_trigger.status == STARTED and not waitOnFlip:
            theseKeys = guide_skip_trigger.getKeys(keyList=['space'], waitRelease=False)
            _guide_skip_trigger_allKeys.extend(theseKeys)
            if len(_guide_skip_trigger_allKeys):
                guide_skip_trigger.keys = _guide_skip_trigger_allKeys[-1].name  # just the last key pressed
                guide_skip_trigger.rt = _guide_skip_trigger_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in guideComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "guide" ---
    for thisComponent in guideComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    
    # CONDITIONAL FLAG
    experiment_stage = "guide.end"
    # the Routine "guide" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_prepare" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from init_practice
    # CONDITIONAL FLAG
    experiment_stage = "practice_prepare"
    
    # DATA PREPARE
    import random
    experiment_idx = 0
    
    shownum = []
    for i in range(practice_repeats):
        shownum.append(0)
        
    # ratio of all should be seven
    positive_count = int(practice_positive_examples)
    
    for i in range(positive_count):
        x = random.randint(0 , practice_repeats-1)
        if shownum[x]== 1 :
            i = i -1;
        else :
            shownum[x] = 1
            
    for i in range(practice_repeats):
        if shownum[i]==1:
            shownum[i] = "7"
        else:
            num = random.randint(0,9)
            if(num==7):
                num-=3
            shownum[i] = str(num)
    # keep track of which components have finished
    practice_prepareComponents = []
    for thisComponent in practice_prepareComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice_prepare" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_prepare" ---
    for thisComponent in practice_prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practice_prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_block = data.TrialHandler(nReps=practice_repeats, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practice_block')
#     thisExp.addLoop(practice_block)  # add the loop to the experiment
    thisPractice_block = practice_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_block.rgb)
    if thisPractice_block != None:
        for paramName in thisPractice_block:
            exec('{} = thisPractice_block[paramName]'.format(paramName))
    
    for thisPractice_block in practice_block:
        currentLoop = practice_block
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_block.rgb)
        if thisPractice_block != None:
            for paramName in thisPractice_block:
                exec('{} = thisPractice_block[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "practice_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        
        # CONDITIONAL FLAG
        experiment_stage = "practice"
        practice_pressed = False
            
        # UPDATE TEXT
        current_num = shownum[experiment_idx]
        practice_number.text = current_num
        
        # setup some python lists for storing info about the practice_response
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        practice_trialComponents = [practice_cross, practice_number, practice_response]
        for thisComponent in practice_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_trial" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_2
            
            
            if(practice_pressed==False and practice_response.status==STARTED and practice_response.getPressed()[0]==1):
                practice_pressed = True
            
            # *practice_cross* updates
            if practice_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_cross.frameNStart = frameN  # exact frame index
                practice_cross.tStart = t  # local t and not account for scr refresh
                practice_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_cross, 'tStartRefresh')  # time at next scr refresh
                practice_cross.setAutoDraw(True)
            if practice_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_cross.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_cross.tStop = t  # not accounting for scr refresh
                    practice_cross.frameNStop = frameN  # exact frame index
                    practice_cross.setAutoDraw(False)
            
            # *practice_number* updates
            if practice_number.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                # keep track of start time/frame for later
                practice_number.frameNStart = frameN  # exact frame index
                practice_number.tStart = t  # local t and not account for scr refresh
                practice_number.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_number, 'tStartRefresh')  # time at next scr refresh
                practice_number.setAutoDraw(True)
            if practice_number.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_number.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_number.tStop = t  # not accounting for scr refresh
                    practice_number.frameNStop = frameN  # exact frame index
                    practice_number.setAutoDraw(False)
            # *practice_response* updates
            if practice_response.status == NOT_STARTED and t >= 0.8-frameTolerance:
                # keep track of start time/frame for later
                practice_response.frameNStart = frameN  # exact frame index
                practice_response.tStart = t  # local t and not account for scr refresh
                practice_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_response, 'tStartRefresh')  # time at next scr refresh
                practice_response.status = STARTED
                practice_response.mouseClock.reset()
                prevButtonState = practice_response.getPressed()  # if button is down already this ISN'T a new click
            if practice_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_response.tStartRefresh + 1.2-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_response.tStop = t  # not accounting for scr refresh
                    practice_response.frameNStop = frameN  # exact frame index
                    practice_response.status = FINISHED
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_trial" ---
        for thisComponent in practice_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_2
        
        
        # store data for practice_block (TrialHandler)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "practice_feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from practice_judge
        
        correct = practice_pressed and current_num=="7" or not practice_pressed and current_num!="7"
        if(correct):
            practice_response_tip.text = "正确"
        else:
            practice_response_tip.text = "错误"
        
        experiment_idx += 1
        # keep track of which components have finished
        practice_feedbackComponents = [practice_response_tip]
        for thisComponent in practice_feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_feedback" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practice_response_tip* updates
            if practice_response_tip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_response_tip.frameNStart = frameN  # exact frame index
                practice_response_tip.tStart = t  # local t and not account for scr refresh
                practice_response_tip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_response_tip, 'tStartRefresh')  # time at next scr refresh
                practice_response_tip.setAutoDraw(True)
            if practice_response_tip.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_response_tip.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_response_tip.tStop = t  # not accounting for scr refresh
                    practice_response_tip.frameNStop = frameN  # exact frame index
                    practice_response_tip.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_feedback" ---
        for thisComponent in practice_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
#         thisExp.nextEntry()
        
    # completed practice_repeats repeats of 'practice_block'
    
    
    # --- Prepare to start Routine "practice_confirm" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    practice_confirm_trigger.keys = []
    practice_confirm_trigger.rt = []
    _practice_confirm_trigger_allKeys = []
    # Run 'Begin Routine' code from code_3
    
    # CONDITIONAL FLAG
    experiment_stage = "practice_confirm"
    # keep track of which components have finished
    practice_confirmComponents = [practice_confirm_tip, practice_confirm_trigger]
    for thisComponent in practice_confirmComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice_confirm" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_confirm_tip* updates
        if practice_confirm_tip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_confirm_tip.frameNStart = frameN  # exact frame index
            practice_confirm_tip.tStart = t  # local t and not account for scr refresh
            practice_confirm_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_confirm_tip, 'tStartRefresh')  # time at next scr refresh
            practice_confirm_tip.setAutoDraw(True)
        
        # *practice_confirm_trigger* updates
        waitOnFlip = False
        if practice_confirm_trigger.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            practice_confirm_trigger.frameNStart = frameN  # exact frame index
            practice_confirm_trigger.tStart = t  # local t and not account for scr refresh
            practice_confirm_trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_confirm_trigger, 'tStartRefresh')  # time at next scr refresh
            practice_confirm_trigger.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(practice_confirm_trigger.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(practice_confirm_trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practice_confirm_trigger.status == STARTED and not waitOnFlip:
            theseKeys = practice_confirm_trigger.getKeys(keyList=['y','n'], waitRelease=False)
            _practice_confirm_trigger_allKeys.extend(theseKeys)
            if len(_practice_confirm_trigger_allKeys):
                practice_confirm_trigger.keys = _practice_confirm_trigger_allKeys[-1].name  # just the last key pressed
                practice_confirm_trigger.rt = _practice_confirm_trigger_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_confirmComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_confirm" ---
    for thisComponent in practice_confirmComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_3
    
    if(practice_confirm_trigger.keys[0]=='y'):
        practice_loop.finished = True
    
    # the Routine "practice_confirm" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 65535.0 repeats of 'practice_loop'


# --- Prepare to start Routine "experiment_prepare" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from init_experiment
# CONDITIONAL FLAG
experiment_stage = "experiment_prepare"

experiment_trial_idx = 1
experiment_block_idx = 1
experiment_idx = 0
# DATA PREPARE
import random

shownum = []
experiment_examples = experiment_block_nums*experiment_block_trials
for i in range(experiment_examples):
    shownum.append(0)
    
# ratio of all should be seven
for i in range(experiment_positive_examples):
    x = random.randint(0 , experiment_examples-1)
    if shownum[x]== 1 :
        i = i -1;
    else :
        shownum[x] = 1
        
for i in range(experiment_examples):
    if shownum[i]==1:
        shownum[i] = "7"
    else:
        num = random.randint(0,9)
        if(num==7):
            num-=3
        shownum[i] = str(num)
# keep track of which components have finished
experiment_prepareComponents = []
for thisComponent in experiment_prepareComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "experiment_prepare" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in experiment_prepareComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "experiment_prepare" ---
for thisComponent in experiment_prepareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "experiment_prepare" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
experiment_loop = data.TrialHandler(nReps=experiment_block_nums, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='experiment_loop')
# thisExp.addLoop(experiment_loop)  # add the loop to the experiment
thisExperiment_loop = experiment_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExperiment_loop.rgb)
if thisExperiment_loop != None:
    for paramName in thisExperiment_loop:
        exec('{} = thisExperiment_loop[paramName]'.format(paramName))

for thisExperiment_loop in experiment_loop:
    currentLoop = experiment_loop
    # abbreviate parameter names if possible (e.g. rgb = thisExperiment_loop.rgb)
    if thisExperiment_loop != None:
        for paramName in thisExperiment_loop:
            exec('{} = thisExperiment_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    experiment_block = data.TrialHandler(nReps=experiment_block_trials, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='experiment_block')
#     thisExp.addLoop(experiment_block)  # add the loop to the experiment
    thisExperiment_block = experiment_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExperiment_block.rgb)
    if thisExperiment_block != None:
        for paramName in thisExperiment_block:
            exec('{} = thisExperiment_block[paramName]'.format(paramName))
    
    for thisExperiment_block in experiment_block:
        currentLoop = experiment_block
        # abbreviate parameter names if possible (e.g. rgb = thisExperiment_block.rgb)
        if thisExperiment_block != None:
            for paramName in thisExperiment_block:
                exec('{} = thisExperiment_block[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "experiment_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_4
        
        #CONDITIONAL FLAG
        experiment_stage = "experiment"
        experiment_pressed = False
        
        # UPDATE TEXT
        current_num = shownum[experiment_idx]
        experiment_number.text = current_num
        
        
        
        record(experiment_block_idx,experiment_trial_idx,"ShowNum",current_num)
        # setup some python lists for storing info about the experiment_response
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        experiment_trialComponents = [experiment_cross, experiment_number, experiment_response]
        for thisComponent in experiment_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "experiment_trial" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_4
            
            
            if(experiment_pressed==False and experiment_response.status==STARTED and experiment_response.getPressed()[0]==1):
                experiment_pressed = True
                record(experiment_block_idx,experiment_trial_idx,"ReactTime",t-experiment_response.tStart)
                record(experiment_block_idx,experiment_trial_idx,"Pressed",True)
            
            
            # *experiment_cross* updates
            if experiment_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                experiment_cross.frameNStart = frameN  # exact frame index
                experiment_cross.tStart = t  # local t and not account for scr refresh
                experiment_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_cross, 'tStartRefresh')  # time at next scr refresh
                experiment_cross.setAutoDraw(True)
            if experiment_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_cross.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_cross.tStop = t  # not accounting for scr refresh
                    experiment_cross.frameNStop = frameN  # exact frame index
                    experiment_cross.setAutoDraw(False)
            
            # *experiment_number* updates
            if experiment_number.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                # keep track of start time/frame for later
                experiment_number.frameNStart = frameN  # exact frame index
                experiment_number.tStart = t  # local t and not account for scr refresh
                experiment_number.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_number, 'tStartRefresh')  # time at next scr refresh
                experiment_number.setAutoDraw(True)
            if experiment_number.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_number.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_number.tStop = t  # not accounting for scr refresh
                    experiment_number.frameNStop = frameN  # exact frame index
                    experiment_number.setAutoDraw(False)
            # *experiment_response* updates
            if experiment_response.status == NOT_STARTED and t >= 0.8-frameTolerance:
                # keep track of start time/frame for later
                experiment_response.frameNStart = frameN  # exact frame index
                experiment_response.tStart = t  # local t and not account for scr refresh
                experiment_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_response, 'tStartRefresh')  # time at next scr refresh
                experiment_response.status = STARTED
                experiment_response.mouseClock.reset()
                prevButtonState = experiment_response.getPressed()  # if button is down already this ISN'T a new click
            if experiment_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_response.tStartRefresh + 1.2-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_response.tStop = t  # not accounting for scr refresh
                    experiment_response.frameNStop = frameN  # exact frame index
                    experiment_response.status = FINISHED
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in experiment_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "experiment_trial" ---
        for thisComponent in experiment_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_4
        
        
        correct = experiment_pressed and current_num=="7" or not experiment_pressed and current_num!="7"
        record(experiment_block_idx,experiment_trial_idx,"Correct",correct)
        
        if(not experiment_pressed):
            record(experiment_block_idx,experiment_trial_idx,"Pressed",False)
            
        
        
        
        
        
        experiment_trial_idx += 1
        experiment_idx += 1
        # store data for experiment_block (TrialHandler)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
#         thisExp.nextEntry()
        
    # completed experiment_block_trials repeats of 'experiment_block'
    
    
    # --- Prepare to start Routine "experiment_rest" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_5
    
    #UPDATE TEXT
    if(experiment_block_idx==experiment_block_nums):
        experiment_rest_tip.text = experiment_end_text
    experiment_rest_skip_trigger.keys = []
    experiment_rest_skip_trigger.rt = []
    _experiment_rest_skip_trigger_allKeys = []
    # keep track of which components have finished
    experiment_restComponents = [experiment_rest_tip, experiment_rest_skip_trigger]
    for thisComponent in experiment_restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "experiment_rest" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *experiment_rest_tip* updates
        if experiment_rest_tip.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            experiment_rest_tip.frameNStart = frameN  # exact frame index
            experiment_rest_tip.tStart = t  # local t and not account for scr refresh
            experiment_rest_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_rest_tip, 'tStartRefresh')  # time at next scr refresh
            experiment_rest_tip.setAutoDraw(True)
        
        # *experiment_rest_skip_trigger* updates
        waitOnFlip = False
        if experiment_rest_skip_trigger.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            experiment_rest_skip_trigger.frameNStart = frameN  # exact frame index
            experiment_rest_skip_trigger.tStart = t  # local t and not account for scr refresh
            experiment_rest_skip_trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_rest_skip_trigger, 'tStartRefresh')  # time at next scr refresh
            experiment_rest_skip_trigger.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(experiment_rest_skip_trigger.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(experiment_rest_skip_trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if experiment_rest_skip_trigger.status == STARTED and not waitOnFlip:
            theseKeys = experiment_rest_skip_trigger.getKeys(keyList=['space'], waitRelease=False)
            _experiment_rest_skip_trigger_allKeys.extend(theseKeys)
            if len(_experiment_rest_skip_trigger_allKeys):
                experiment_rest_skip_trigger.keys = _experiment_rest_skip_trigger_allKeys[-1].name  # just the last key pressed
                experiment_rest_skip_trigger.rt = _experiment_rest_skip_trigger_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experiment_restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "experiment_rest" ---
    for thisComponent in experiment_restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_5
    
    #CONDITIONAL FLAG
    experiment_stage = "experiment_rest.end"
    experiment_block_idx += 1
    experiment_trial_idx = 1
    # the Routine "experiment_rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed experiment_block_nums repeats of 'experiment_loop'

# Run 'End Experiment' code from variable_init




# CONDITIONAL FLAG
experiment_stage = "end_experiment"

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
# thisExp.saveAsWideText(filename+'.csv', delim='auto')
# thisExp.saveAsPickle(filename)
# logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
# thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
