#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 十月 19, 2022, at 22:14
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


image_id_from = 1
image_id_to = 10



materials = [
    {
        "id":1,
        "tip_size":(600,400),
        "target_size":(100,60),
        "target_ori":-45,
        "target_pos":(250,-150),
        "background_size":(1000,1000)
    },
    {
        "id":2,
        "tip_size":(600,600),
        "target_size":(150,150),
        "target_ori":0,
        "target_pos":(-400,-250),
        "background_size":(1000,1000)
    },
    {
        "id":3,
        "tip_size":(600,600),
        "target_size":(100,100),
        "target_ori":0,
        "target_pos":(-300,-260),
        "background_size":(1000,1000)
    },
    {
        "id":4,
        "tip_size":(800,400),
        "target_size":(250,250),
        "target_ori":0,
        "target_pos":(260,-100),
        "background_size":(1000,1000)
    },
    {
        "id":5,
        "tip_size":(600,600),
        "target_size":(200,200),
        "target_ori":0,
        "target_pos":(-230,-260),
        "background_size":(1000,1000)
    },
    {
        "id":6,
        "tip_size":(600,600),
        "target_size":(100,100),
        "target_ori":0,
        "target_pos":(250,-200),
        "background_size":(1000,1000)
    },
    {
        "id":7,
        "tip_size":(800,600),
        "target_size":(100,100),
        "target_ori":0,
        "target_pos":(260,-250),
        "background_size":(1000,1000)
    },
    {
        "id":8,
        "tip_size":(800,600),
        "target_size":(170,170),
        "target_ori":0,
        "target_pos":(50,-400),
        "background_size":(1000,1000)
    },
    {
        "id":9,
        "tip_size":(800,600),
        "target_size":(140,100),
        "target_ori":0,
        "target_pos":(330,30),
        "background_size":(1000,1000)
    },
    {
        "id":10,
        "tip_size":(600,800),
        "target_size":(100,100),
        "target_ori":0,
        "target_pos":(-20,200),
        "background_size":(1000,1000)
    }
]


tip_duration = 1
select_duration = 5

image_root = "./assets/image_search"
def get_background(bg_id):
    return image_root+"/backgrounds/bg_"+str(bg_id)+".png"

def get_target(target_id):
    return image_root+"/targets/t_"+str(target_id)+".png"
    

# TEXT CONFIG
guide_text = "您好，欢迎参加本次实验\n每段实验开始时，将会呈现一张目标图像\n随后目标图像将隐藏在背景图像中\n在场景中寻找目标图像、鼠标点击选择\n明白后按空格进入练习"
practice_confirm_text = "练习已结束\n若您已了解本实验操作请按“Y”键，进入正式实验；\n若您还未熟悉实验操作请按“N”键，重新进行练习。"
experiment_rest_text = "下一阶段难度将会提升\n请休息一下，当您觉得状态恢复良好时\n可随时按空格键继续。"
experiment_end_text = "试验结束，感谢参与\n按空格退出"

# CONDITIONAL FLAG
experiment_stage = "before_experiment"

# PRACTICE CONFIG
practice_repeats = 1

# EXPERIMENT CONFIG
experiment_block_nums = 1
experiment_block_trials = 10
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
#     originPath='E:\\Work\\focus-experiment\\src\\tasks\\project\\image_search.py',
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

# --- Initialize components for Routine "practice_tip" ---
practice_tip_target = visual.ImageStim(
    win=win,
    name='practice_tip_target', units='pix', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "practice_trial" ---
practice_bg_image = visual.ImageStim(
    win=win,
    name='practice_bg_image', units='pix', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
practice_mouse = event.Mouse(win=win)
x, y = [None, None]
practice_mouse.mouseClock = core.Clock()
practice_target_image = visual.ImageStim(
    win=win,
    name='practice_target_image', units='pix', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "practice_feedback" ---
practice_response_tip = visual.TextStim(win=win, name='practice_response_tip',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
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

# --- Initialize components for Routine "experiment_tip" ---
experiment_tip_target = visual.ImageStim(
    win=win,
    name='experiment_tip_target', units='pix', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "experiment_trial" ---
experiment_bg_image = visual.ImageStim(
    win=win,
    name='experiment_bg_image', units='pix', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
experiment_target_image = visual.ImageStim(
    win=win,
    name='experiment_target_image', units='pix', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
experiment_mouse = event.Mouse(win=win)
x, y = [None, None]
experiment_mouse.mouseClock = core.Clock()

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
    
    practice_tests = random.sample(materials,practice_repeats)
    
    
    
    
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
        
        # --- Prepare to start Routine "practice_tip" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_7
        
        practice_test = practice_tests[experiment_idx]
        
        
        target_image = get_target(practice_test["id"])
        bg_image = get_background(practice_test["id"])
        
        practice_tip_target.image = target_image
        practice_tip_target.size = practice_test["tip_size"]
        # keep track of which components have finished
        practice_tipComponents = [practice_tip_target]
        for thisComponent in practice_tipComponents:
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
        
        # --- Run Routine "practice_tip" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practice_tip_target* updates
            if practice_tip_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_tip_target.frameNStart = frameN  # exact frame index
                practice_tip_target.tStart = t  # local t and not account for scr refresh
                practice_tip_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_tip_target, 'tStartRefresh')  # time at next scr refresh
                practice_tip_target.setAutoDraw(True)
            if practice_tip_target.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_tip_target.tStartRefresh + tip_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_tip_target.tStop = t  # not accounting for scr refresh
                    practice_tip_target.frameNStop = frameN  # exact frame index
                    practice_tip_target.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_tipComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_tip" ---
        for thisComponent in practice_tipComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "practice_tip" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "practice_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        
        # CONDITIONAL FLAG
        experiment_stage = "practice"
        
        react_time = None
        
        practice_bg_image.image = bg_image
        practice_target_image.image = target_image
        
        practice_bg_image.size = practice_test["background_size"]
        practice_target_image.size = practice_test["target_size"]
        practice_target_image.pos = practice_test["target_pos"]
        practice_target_image.ori = practice_test["target_ori"]
        
        # setup some python lists for storing info about the practice_mouse
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        practice_trialComponents = [practice_bg_image, practice_mouse, practice_target_image]
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
            
            
            if(practice_mouse.isPressedIn(practice_target_image)):
                react_time = round(t - practice_mouse.tStart,2)
                continueRoutine = False
            
            
            
                    
            
            
            
            # *practice_bg_image* updates
            if practice_bg_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_bg_image.frameNStart = frameN  # exact frame index
                practice_bg_image.tStart = t  # local t and not account for scr refresh
                practice_bg_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_bg_image, 'tStartRefresh')  # time at next scr refresh
                practice_bg_image.setAutoDraw(True)
            if practice_bg_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_bg_image.tStartRefresh + select_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_bg_image.tStop = t  # not accounting for scr refresh
                    practice_bg_image.frameNStop = frameN  # exact frame index
                    practice_bg_image.setAutoDraw(False)
            # *practice_mouse* updates
            if practice_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_mouse.frameNStart = frameN  # exact frame index
                practice_mouse.tStart = t  # local t and not account for scr refresh
                practice_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_mouse, 'tStartRefresh')  # time at next scr refresh
                practice_mouse.status = STARTED
                practice_mouse.mouseClock.reset()
                prevButtonState = practice_mouse.getPressed()  # if button is down already this ISN'T a new click
            if practice_mouse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_mouse.tStartRefresh + select_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_mouse.tStop = t  # not accounting for scr refresh
                    practice_mouse.frameNStop = frameN  # exact frame index
                    practice_mouse.status = FINISHED
            if practice_mouse.status == STARTED:  # only update if started and not finished!
                buttons = practice_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # *practice_target_image* updates
            if practice_target_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_target_image.frameNStart = frameN  # exact frame index
                practice_target_image.tStart = t  # local t and not account for scr refresh
                practice_target_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_target_image, 'tStartRefresh')  # time at next scr refresh
                practice_target_image.setAutoDraw(True)
            if practice_target_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_target_image.tStartRefresh + select_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_target_image.tStop = t  # not accounting for scr refresh
                    practice_target_image.frameNStop = frameN  # exact frame index
                    practice_target_image.setAutoDraw(False)
            
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
        
        
        if(react_time==None):
            react_time = "???"
        # store data for practice_block (TrialHandler)
        # the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "practice_feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from practice_judge
        
        
        practice_response_tip.text = str(react_time)+" s"
        
        
        
        
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
# Run 'Begin Routine' code from code_6

# CONDITIONAL FLAG
experiment_stage = "experiment_prepare"

# DATA PREPARE
import random


experiment_trial_idx = 1
experiment_block_idx = 1
experiment_idx = 0


experiment_tests = random.sample(materials,experiment_block_nums*experiment_block_trials)


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
        
        # --- Prepare to start Routine "experiment_tip" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_8
        
        experiment_test = experiment_tests[experiment_idx]
        
        
        target_image = get_target(experiment_test["id"])
        bg_image = get_background(experiment_test["id"])
        
        experiment_tip_target.image = target_image
        experiment_tip_target.size = experiment_test["tip_size"]
        
        record(experiment_block_idx,experiment_trial_idx,"Stimulus_Id",react_time)
        
        # keep track of which components have finished
        experiment_tipComponents = [experiment_tip_target]
        for thisComponent in experiment_tipComponents:
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
        
        # --- Run Routine "experiment_tip" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *experiment_tip_target* updates
            if experiment_tip_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                experiment_tip_target.frameNStart = frameN  # exact frame index
                experiment_tip_target.tStart = t  # local t and not account for scr refresh
                experiment_tip_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_tip_target, 'tStartRefresh')  # time at next scr refresh
                experiment_tip_target.setAutoDraw(True)
            if experiment_tip_target.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_tip_target.tStartRefresh + tip_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_tip_target.tStop = t  # not accounting for scr refresh
                    experiment_tip_target.frameNStop = frameN  # exact frame index
                    experiment_tip_target.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in experiment_tipComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "experiment_tip" ---
        for thisComponent in experiment_tipComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "experiment_tip" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "experiment_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_4
        
        
        # CONDITIONAL FLAG
        experiment_stage = "experiment"
        
        react_time = None
        
        experiment_bg_image.image = bg_image
        experiment_target_image.image = target_image
        
        experiment_bg_image.size = experiment_test["background_size"]
        experiment_target_image.size = experiment_test["target_size"]
        experiment_target_image.pos = experiment_test["target_pos"]
        experiment_target_image.ori = experiment_test["target_ori"]
        
        # setup some python lists for storing info about the experiment_mouse
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        experiment_trialComponents = [experiment_bg_image, experiment_target_image, experiment_mouse]
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
            
            
            if(experiment_mouse.isPressedIn(experiment_target_image)):
                react_time = round(t - experiment_mouse.tStart,2)
                record(experiment_block_idx,experiment_trial_idx,"ReactTime",react_time)
                continueRoutine = False
            
            
            
                    
            
            
            
            # *experiment_bg_image* updates
            if experiment_bg_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                experiment_bg_image.frameNStart = frameN  # exact frame index
                experiment_bg_image.tStart = t  # local t and not account for scr refresh
                experiment_bg_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_bg_image, 'tStartRefresh')  # time at next scr refresh
                experiment_bg_image.setAutoDraw(True)
            if experiment_bg_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_bg_image.tStartRefresh + select_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_bg_image.tStop = t  # not accounting for scr refresh
                    experiment_bg_image.frameNStop = frameN  # exact frame index
                    experiment_bg_image.setAutoDraw(False)
            
            # *experiment_target_image* updates
            if experiment_target_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                experiment_target_image.frameNStart = frameN  # exact frame index
                experiment_target_image.tStart = t  # local t and not account for scr refresh
                experiment_target_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_target_image, 'tStartRefresh')  # time at next scr refresh
                experiment_target_image.setAutoDraw(True)
            if experiment_target_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_target_image.tStartRefresh + select_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_target_image.tStop = t  # not accounting for scr refresh
                    experiment_target_image.frameNStop = frameN  # exact frame index
                    experiment_target_image.setAutoDraw(False)
            # *experiment_mouse* updates
            if experiment_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                experiment_mouse.frameNStart = frameN  # exact frame index
                experiment_mouse.tStart = t  # local t and not account for scr refresh
                experiment_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_mouse, 'tStartRefresh')  # time at next scr refresh
                experiment_mouse.status = STARTED
                experiment_mouse.mouseClock.reset()
                prevButtonState = experiment_mouse.getPressed()  # if button is down already this ISN'T a new click
            if experiment_mouse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_mouse.tStartRefresh + select_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_mouse.tStop = t  # not accounting for scr refresh
                    experiment_mouse.frameNStop = frameN  # exact frame index
                    experiment_mouse.status = FINISHED
            if experiment_mouse.status == STARTED:  # only update if started and not finished!
                buttons = experiment_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
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
        
        
        
        
        experiment_trial_idx += 1
        experiment_idx += 1
        # store data for experiment_block (TrialHandler)
        # the Routine "experiment_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
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
# thisExp.saveAsWideText(filename+'.csv', delim='auto')
# thisExp.saveAsPickle(filename)
# logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
# thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
