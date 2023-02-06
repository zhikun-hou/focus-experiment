#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 十月 16, 2022, at 22:32
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
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

    
level_total = 6
current_level = 1
level_images = 6
degree_divider = 360 / level_images
tip_duration = 10
image_duration = 5

image_root = "./assets/image_mirror"
def get_img_name(level,idx,is_mirrored):# idx从0开始
    name = str(level).zfill(2)+"-"+str(int(idx*degree_divider))
    if(is_mirrored):
        name += "-m"
    return name
    
# TEXT CONFIG
guide_text = "您好，欢迎参加本次实验\n每段实验开始时，屏幕左侧呈现原图、右侧呈现镜像\n随后会呈现数张旋转后的图片，请做如下反应：\n若由原图旋转所得，请按“F”\n若由镜像旋转所得，请按“J”\n明白后按空格进入练习"
practice_confirm_text = "练习已结束\n若您已了解本实验操作请按“Y”键，进入正式实验；\n若您还未熟悉实验操作请按“N”键，重新进行练习。"
experiment_rest_text = "下一阶段难度将会提升\n请休息一下，当您觉得状态恢复良好时\n可随时按空格键继续。"
experiment_end_text = "试验结束，感谢参与\n按空格退出"

# CONDITIONAL FLAG
experiment_stage = "before_experiment"

# PRACTICE CONFIG
practice_repeats = 4

# EXPERIMENT CONFIG
experiment_block_nums = level_total
experiment_block_trials = 12
# Run 'Before Experiment' code from code_6




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
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\Work\\focus-experiment\\src\\tasks\\project\\image_mirror.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

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
image_raw = visual.ImageStim(
    win=win,
    name='image_raw', units='pix', 
    image=None, mask=None, anchor='top-right',
    ori=0.0, pos=(-10, 20), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_mirror = visual.ImageStim(
    win=win,
    name='image_mirror', units='pix', 
    image=None, mask=None, anchor='top-left',
    ori=0.0, pos=(10, 20), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
tip_skipper = keyboard.Keyboard()
tip_normal = visual.TextStim(win=win, name='tip_normal',
    text='原始图片',
    font='Open Sans',
    pos=(-0.25, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
tip_mirror = visual.TextStim(win=win, name='tip_mirror',
    text='镜像图片',
    font='Open Sans',
    pos=(0.25, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "practice_trial" ---
practice_image = visual.ImageStim(
    win=win,
    name='practice_image', units='pix', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
practice_response = keyboard.Keyboard()

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

# --- Initialize components for Routine "level_prepare" ---
experiment_image_raw = visual.ImageStim(
    win=win,
    name='experiment_image_raw', units='pix', 
    image=None, mask=None, anchor='top-right',
    ori=0.0, pos=(-10, 20), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
experiment_image_mirror = visual.ImageStim(
    win=win,
    name='experiment_image_mirror', units='pix', 
    image=None, mask=None, anchor='top-left',
    ori=0.0, pos=(10, 20), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
experiment_tip_skipper = keyboard.Keyboard()
experiment_tip_normal = visual.TextStim(win=win, name='experiment_tip_normal',
    text='原始图片',
    font='Open Sans',
    pos=(-0.25, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
experiment_tip_mirror = visual.TextStim(win=win, name='experiment_tip_mirror',
    text='镜像图片',
    font='Open Sans',
    pos=(0.25,0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "experiment_trial" ---
experiment_image = visual.ImageStim(
    win=win,
    name='experiment_image', units='pix', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
experiment_response = keyboard.Keyboard()

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
thisExp.addLoop(practice_loop)  # add the loop to the experiment
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
    
    is_mirror = []
    shownum = []
    for i in range(practice_repeats):
        is_mirror.append(
            random.randint(0,1)
        )
        shownum.append(
            random.randint(0,level_images-1)
        )
    
    image_raw.image = image_root+"/"+get_img_name(current_level,0,False)+".jpg"
    image_mirror.image = image_root+"/"+get_img_name(current_level,0,True)+".jpg"
    tip_skipper.keys = []
    tip_skipper.rt = []
    _tip_skipper_allKeys = []
    # keep track of which components have finished
    practice_prepareComponents = [image_raw, image_mirror, tip_skipper, tip_normal, tip_mirror]
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
        
        # *image_raw* updates
        if image_raw.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_raw.frameNStart = frameN  # exact frame index
            image_raw.tStart = t  # local t and not account for scr refresh
            image_raw.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_raw, 'tStartRefresh')  # time at next scr refresh
            image_raw.setAutoDraw(True)
        if image_raw.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_raw.tStartRefresh + tip_duration-frameTolerance:
                # keep track of stop time/frame for later
                image_raw.tStop = t  # not accounting for scr refresh
                image_raw.frameNStop = frameN  # exact frame index
                image_raw.setAutoDraw(False)
        
        # *image_mirror* updates
        if image_mirror.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_mirror.frameNStart = frameN  # exact frame index
            image_mirror.tStart = t  # local t and not account for scr refresh
            image_mirror.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_mirror, 'tStartRefresh')  # time at next scr refresh
            image_mirror.setAutoDraw(True)
        if image_mirror.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_mirror.tStartRefresh + tip_duration-frameTolerance:
                # keep track of stop time/frame for later
                image_mirror.tStop = t  # not accounting for scr refresh
                image_mirror.frameNStop = frameN  # exact frame index
                image_mirror.setAutoDraw(False)
        
        # *tip_skipper* updates
        waitOnFlip = False
        if tip_skipper.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tip_skipper.frameNStart = frameN  # exact frame index
            tip_skipper.tStart = t  # local t and not account for scr refresh
            tip_skipper.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tip_skipper, 'tStartRefresh')  # time at next scr refresh
            tip_skipper.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(tip_skipper.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(tip_skipper.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if tip_skipper.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tip_skipper.tStartRefresh + tip_duration-frameTolerance:
                # keep track of stop time/frame for later
                tip_skipper.tStop = t  # not accounting for scr refresh
                tip_skipper.frameNStop = frameN  # exact frame index
                tip_skipper.status = FINISHED
        if tip_skipper.status == STARTED and not waitOnFlip:
            theseKeys = tip_skipper.getKeys(keyList=['space'], waitRelease=False)
            _tip_skipper_allKeys.extend(theseKeys)
            if len(_tip_skipper_allKeys):
                tip_skipper.keys = _tip_skipper_allKeys[-1].name  # just the last key pressed
                tip_skipper.rt = _tip_skipper_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *tip_normal* updates
        if tip_normal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tip_normal.frameNStart = frameN  # exact frame index
            tip_normal.tStart = t  # local t and not account for scr refresh
            tip_normal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tip_normal, 'tStartRefresh')  # time at next scr refresh
            tip_normal.setAutoDraw(True)
        if tip_normal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tip_normal.tStartRefresh + tip_duration-frameTolerance:
                # keep track of stop time/frame for later
                tip_normal.tStop = t  # not accounting for scr refresh
                tip_normal.frameNStop = frameN  # exact frame index
                tip_normal.setAutoDraw(False)
        
        # *tip_mirror* updates
        if tip_mirror.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tip_mirror.frameNStart = frameN  # exact frame index
            tip_mirror.tStart = t  # local t and not account for scr refresh
            tip_mirror.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tip_mirror, 'tStartRefresh')  # time at next scr refresh
            tip_mirror.setAutoDraw(True)
        if tip_mirror.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tip_mirror.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                tip_mirror.tStop = t  # not accounting for scr refresh
                tip_mirror.frameNStop = frameN  # exact frame index
                tip_mirror.setAutoDraw(False)
        
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
    thisExp.addLoop(practice_block)  # add the loop to the experiment
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
        practice_answer = None
            
        # UPDATE TEXT
        current_num = shownum[experiment_idx]
        current_mirror = is_mirror[experiment_idx]
        
        practice_image.image = image_root+"/"+get_img_name(current_level,current_num,current_mirror)+".jpg"
        practice_response.keys = []
        practice_response.rt = []
        _practice_response_allKeys = []
        # keep track of which components have finished
        practice_trialComponents = [practice_image, practice_response]
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_2
            
            
            if(practice_pressed==False and practice_response.status==STARTED and len(practice_response.keys)>0):
                practice_pressed = True
                practice_answer = practice_response.keys[0]
                continueRoutine = False
            
            # *practice_image* updates
            if practice_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_image.frameNStart = frameN  # exact frame index
                practice_image.tStart = t  # local t and not account for scr refresh
                practice_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_image, 'tStartRefresh')  # time at next scr refresh
                practice_image.setAutoDraw(True)
            if practice_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_image.tStartRefresh + image_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_image.tStop = t  # not accounting for scr refresh
                    practice_image.frameNStop = frameN  # exact frame index
                    practice_image.setAutoDraw(False)
            
            # *practice_response* updates
            waitOnFlip = False
            if practice_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_response.frameNStart = frameN  # exact frame index
                practice_response.tStart = t  # local t and not account for scr refresh
                practice_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_response, 'tStartRefresh')  # time at next scr refresh
                practice_response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(practice_response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(practice_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if practice_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_response.tStartRefresh + image_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_response.tStop = t  # not accounting for scr refresh
                    practice_response.frameNStop = frameN  # exact frame index
                    practice_response.status = FINISHED
            if practice_response.status == STARTED and not waitOnFlip:
                theseKeys = practice_response.getKeys(keyList=['f','j'], waitRelease=False)
                _practice_response_allKeys.extend(theseKeys)
                if len(_practice_response_allKeys):
                    practice_response.keys = _practice_response_allKeys[-1].name  # just the last key pressed
                    practice_response.rt = _practice_response_allKeys[-1].rt
            
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
        
        
        # the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "practice_feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from practice_judge
        
        correct = practice_pressed and (current_mirror==0 and practice_answer=='f' or current_mirror==1 and practice_answer=='j')
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
        thisExp.nextEntry()
        
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
# Run 'Begin Routine' code from code_6

# CONDITIONAL FLAG
experiment_stage = "experiment_prepare"

# DATA PREPARE
import random


current_level = 1
experiment_trial_idx = 1
experiment_block_idx = 1
experiment_idx = 0


is_mirror = []
shownum = []
for l in range(experiment_block_nums):
    for j in range(experiment_block_trials):
        shownum.append(
            random.randint(0,level_images-1)
        )
        is_mirror.append(
            random.randint(0,1)
        )
        
    
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
thisExp.addLoop(experiment_loop)  # add the loop to the experiment
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
    
    # --- Prepare to start Routine "level_prepare" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from init_experiment
    # CONDITIONAL FLAG
    experiment_stage = "experiment_prepare"
    
    experiment_image_raw.image = image_root+"/"+get_img_name(current_level,0,False)+".jpg"
    experiment_image_mirror.image = image_root+"/"+get_img_name(current_level,0,True)+".jpg"
    experiment_tip_skipper.keys = []
    experiment_tip_skipper.rt = []
    _experiment_tip_skipper_allKeys = []
    # keep track of which components have finished
    level_prepareComponents = [experiment_image_raw, experiment_image_mirror, experiment_tip_skipper, experiment_tip_normal, experiment_tip_mirror]
    for thisComponent in level_prepareComponents:
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
    
    # --- Run Routine "level_prepare" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *experiment_image_raw* updates
        if experiment_image_raw.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            experiment_image_raw.frameNStart = frameN  # exact frame index
            experiment_image_raw.tStart = t  # local t and not account for scr refresh
            experiment_image_raw.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_image_raw, 'tStartRefresh')  # time at next scr refresh
            experiment_image_raw.setAutoDraw(True)
        if experiment_image_raw.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > experiment_image_raw.tStartRefresh + tip_duration-frameTolerance:
                # keep track of stop time/frame for later
                experiment_image_raw.tStop = t  # not accounting for scr refresh
                experiment_image_raw.frameNStop = frameN  # exact frame index
                experiment_image_raw.setAutoDraw(False)
        
        # *experiment_image_mirror* updates
        if experiment_image_mirror.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            experiment_image_mirror.frameNStart = frameN  # exact frame index
            experiment_image_mirror.tStart = t  # local t and not account for scr refresh
            experiment_image_mirror.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_image_mirror, 'tStartRefresh')  # time at next scr refresh
            experiment_image_mirror.setAutoDraw(True)
        if experiment_image_mirror.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > experiment_image_mirror.tStartRefresh + tip_duration-frameTolerance:
                # keep track of stop time/frame for later
                experiment_image_mirror.tStop = t  # not accounting for scr refresh
                experiment_image_mirror.frameNStop = frameN  # exact frame index
                experiment_image_mirror.setAutoDraw(False)
        
        # *experiment_tip_skipper* updates
        waitOnFlip = False
        if experiment_tip_skipper.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            experiment_tip_skipper.frameNStart = frameN  # exact frame index
            experiment_tip_skipper.tStart = t  # local t and not account for scr refresh
            experiment_tip_skipper.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_tip_skipper, 'tStartRefresh')  # time at next scr refresh
            experiment_tip_skipper.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(experiment_tip_skipper.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(experiment_tip_skipper.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if experiment_tip_skipper.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > experiment_tip_skipper.tStartRefresh + tip_duration-frameTolerance:
                # keep track of stop time/frame for later
                experiment_tip_skipper.tStop = t  # not accounting for scr refresh
                experiment_tip_skipper.frameNStop = frameN  # exact frame index
                experiment_tip_skipper.status = FINISHED
        if experiment_tip_skipper.status == STARTED and not waitOnFlip:
            theseKeys = experiment_tip_skipper.getKeys(keyList=['space'], waitRelease=False)
            _experiment_tip_skipper_allKeys.extend(theseKeys)
            if len(_experiment_tip_skipper_allKeys):
                experiment_tip_skipper.keys = _experiment_tip_skipper_allKeys[-1].name  # just the last key pressed
                experiment_tip_skipper.rt = _experiment_tip_skipper_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *experiment_tip_normal* updates
        if experiment_tip_normal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            experiment_tip_normal.frameNStart = frameN  # exact frame index
            experiment_tip_normal.tStart = t  # local t and not account for scr refresh
            experiment_tip_normal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_tip_normal, 'tStartRefresh')  # time at next scr refresh
            experiment_tip_normal.setAutoDraw(True)
        if experiment_tip_normal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > experiment_tip_normal.tStartRefresh + tip_duration-frameTolerance:
                # keep track of stop time/frame for later
                experiment_tip_normal.tStop = t  # not accounting for scr refresh
                experiment_tip_normal.frameNStop = frameN  # exact frame index
                experiment_tip_normal.setAutoDraw(False)
        
        # *experiment_tip_mirror* updates
        if experiment_tip_mirror.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            experiment_tip_mirror.frameNStart = frameN  # exact frame index
            experiment_tip_mirror.tStart = t  # local t and not account for scr refresh
            experiment_tip_mirror.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_tip_mirror, 'tStartRefresh')  # time at next scr refresh
            experiment_tip_mirror.setAutoDraw(True)
        if experiment_tip_mirror.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > experiment_tip_mirror.tStartRefresh + tip_duration-frameTolerance:
                # keep track of stop time/frame for later
                experiment_tip_mirror.tStop = t  # not accounting for scr refresh
                experiment_tip_mirror.frameNStop = frameN  # exact frame index
                experiment_tip_mirror.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in level_prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "level_prepare" ---
    for thisComponent in level_prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "level_prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    experiment_block = data.TrialHandler(nReps=experiment_block_trials, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='experiment_block')
    thisExp.addLoop(experiment_block)  # add the loop to the experiment
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
        experiment_answer = None
        
        # UPDATE TEXT
        current_num = shownum[experiment_idx]
        current_mirror = is_mirror[experiment_idx]
        
        
        
        experiment_image.image = image_root+"/"+get_img_name(current_level,current_num,current_mirror)+".jpg"
        
        record(experiment_block_idx,experiment_trial_idx,"Level_Id",current_level)
        record(experiment_block_idx,experiment_trial_idx,"CurrentImage",current_num)
        record(experiment_block_idx,experiment_trial_idx,"IsMirror",current_mirror)
        experiment_response.keys = []
        experiment_response.rt = []
        _experiment_response_allKeys = []
        # keep track of which components have finished
        experiment_trialComponents = [experiment_image, experiment_response]
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_4
            
            
            if(experiment_pressed==False and experiment_response.status==STARTED and len(experiment_response.keys)>0):
                experiment_pressed = True
                experiment_answer = practice_response.keys[0]
                record(experiment_block_idx,experiment_trial_idx,"ReactTime",t-experiment_response.tStart)
                continueRoutine = False
                
            
            
            # *experiment_image* updates
            if experiment_image.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_image.frameNStart = frameN  # exact frame index
                experiment_image.tStart = t  # local t and not account for scr refresh
                experiment_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_image, 'tStartRefresh')  # time at next scr refresh
                experiment_image.setAutoDraw(True)
            if experiment_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_image.tStartRefresh + image_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_image.tStop = t  # not accounting for scr refresh
                    experiment_image.frameNStop = frameN  # exact frame index
                    experiment_image.setAutoDraw(False)
            
            # *experiment_response* updates
            waitOnFlip = False
            if experiment_response.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_response.frameNStart = frameN  # exact frame index
                experiment_response.tStart = t  # local t and not account for scr refresh
                experiment_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_response, 'tStartRefresh')  # time at next scr refresh
                experiment_response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(experiment_response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(experiment_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if experiment_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_response.tStartRefresh + image_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_response.tStop = t  # not accounting for scr refresh
                    experiment_response.frameNStop = frameN  # exact frame index
                    experiment_response.status = FINISHED
            if experiment_response.status == STARTED and not waitOnFlip:
                theseKeys = experiment_response.getKeys(keyList=['f','j'], waitRelease=False)
                _experiment_response_allKeys.extend(theseKeys)
                if len(_experiment_response_allKeys):
                    experiment_response.keys = _experiment_response_allKeys[-1].name  # just the last key pressed
                    experiment_response.rt = _experiment_response_allKeys[-1].rt
            
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
        
        
        correct = experiment_pressed and (current_mirror==0 and experiment_answer=='f' or current_mirror==1 and experiment_answer=='j')
        
        record(experiment_block_idx,experiment_trial_idx,"Answer",experiment_response.keys[0])
        record(experiment_block_idx,experiment_trial_idx,"Correct",correct)
        
        
        
        experiment_trial_idx += 1
        experiment_idx += 1
        # the Routine "experiment_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
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
        if experiment_rest_tip.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            experiment_rest_tip.frameNStart = frameN  # exact frame index
            experiment_rest_tip.tStart = t  # local t and not account for scr refresh
            experiment_rest_tip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_rest_tip, 'tStartRefresh')  # time at next scr refresh
            experiment_rest_tip.setAutoDraw(True)
        
        # *experiment_rest_skip_trigger* updates
        waitOnFlip = False
        if experiment_rest_skip_trigger.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
    current_level += 1
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
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
