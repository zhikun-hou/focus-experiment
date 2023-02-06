#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 十月 16, 2022, at 21:37
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


# 逻辑判断
def judge(input_key,current_target,current_order):
    if(input_key=="right"):
        return current_target == current_order[0]
    elif(input_key=="down"):
        return current_target == current_order[1]
    elif(input_key=="left"):
        return current_target == current_order[2]
    elif(input_key=="up"):
        return current_target == current_order[3]
    else:
        return False

pos_mapping = ["right","down","left","up"]

# 全排列，用来保证四张图是随机放置
from itertools import permutations
image_orders = list(permutations(['0','1','2','3'],4))
orders_count = len(image_orders)

image_root = "./assets/image_discrimination"
image_id_min = 1
image_id_max = 15

duration_time = 30

# TEXT CONFIG
guide_text = "您好，欢迎参加本次实验\n在实验过程中，屏幕中央会呈现一个“＋”\n在“＋”消失后会出现五张图片，请做如下反应：\n中央为原始图片，按方向键选择相同图片\n请在保证正确的前提下尽快进行反应\n明白实验后按空格键进入练习。"
practice_confirm_text = "练习已结束\n若您已了解本实验操作请按“Y”键，进入正式实验；\n若您还未熟悉实验操作请按“N”键，重新进行练习。"
experiment_rest_text = "请休息一下，当您觉得状态恢复良好时\n可随时按空格键继续。"
experiment_end_text = "试验结束，感谢参与\n按空格退出"

# CONDITIONAL FLAG
experiment_stage = "before_experiment"

# PRACTICE CONFIG
practice_repeats = 2

# EXPERIMENT CONFIG
experiment_block_nums = 4
experiment_block_trials = 10


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
    originPath='E:\\Work\\focus-experiment\\src\\tasks\\project\\image_discrimination.py',
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

# --- Initialize components for Routine "practice_trial" ---
practice_cross = visual.TextStim(win=win, name='practice_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
practice_center = visual.ImageStim(
    win=win,
    name='practice_center', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
practice_up = visual.ImageStim(
    win=win,
    name='practice_up', 
    image=None, mask=None, anchor='bottom-center',
    ori=0.0, pos=(0, 0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
practice_down = visual.ImageStim(
    win=win,
    name='practice_down', 
    image=None, mask=None, anchor='top-center',
    ori=0.0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
practice_left = visual.ImageStim(
    win=win,
    name='practice_left', 
    image=None, mask=None, anchor='center-right',
    ori=0.0, pos=(-0.2, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
practice_right = visual.ImageStim(
    win=win,
    name='practice_right', 
    image=None, mask=None, anchor='center-left',
    ori=0.0, pos=(0.2, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
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

# --- Initialize components for Routine "experiment_trial" ---
experiment_cross = visual.TextStim(win=win, name='experiment_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
experiment_response = keyboard.Keyboard()
experiment_up = visual.ImageStim(
    win=win,
    name='experiment_up', 
    image=None, mask=None, anchor='bottom-center',
    ori=0.0, pos=(0, 0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
experiment_down = visual.ImageStim(
    win=win,
    name='experiment_down', 
    image=None, mask=None, anchor='top-center',
    ori=0.0, pos=(0, -0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
experiment_left = visual.ImageStim(
    win=win,
    name='experiment_left', 
    image=None, mask=None, anchor='center-right',
    ori=0.0, pos=(-0.2, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
experiment_right = visual.ImageStim(
    win=win,
    name='experiment_right', 
    image=None, mask=None, anchor='center-left',
    ori=0.0, pos=(0.2, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
experiment_center = visual.ImageStim(
    win=win,
    name='experiment_center', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)

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
    
    practice_group_id = []
    practice_target_id = []
    practice_order_id = []
    for i in range(practice_repeats):
        practice_group_id.append(
            random.randint(image_id_min,image_id_max)
        )
        practice_target_id.append(
            random.randint(0,3)
        )
        practice_order_id.append(
            random.randint(0,orders_count-1)
        )
        
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
            
        # UPDATE IMAGE
        group_name = str(practice_group_id[experiment_idx])
        current_target = str(practice_target_id[experiment_idx])
        current_order = image_orders[practice_order_id[experiment_idx]]
        
        
        practice_right.image = image_root+"/"+group_name+"-"+current_order[0]+".png"
        practice_down.image = image_root+"/"+group_name+"-"+current_order[1]+".png"
        practice_left.image = image_root+"/"+group_name+"-"+current_order[2]+".png"
        practice_up.image = image_root+"/"+group_name+"-"+current_order[3]+".png"
        
        practice_center.image = image_root+"/"+group_name+"-"+current_target+".png"
        practice_response.keys = []
        practice_response.rt = []
        _practice_response_allKeys = []
        # keep track of which components have finished
        practice_trialComponents = [practice_cross, practice_center, practice_up, practice_down, practice_left, practice_right, practice_response]
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
                practice_answer = practice_response.keys
                continueRoutine = False
            
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
            
            # *practice_center* updates
            if practice_center.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                practice_center.frameNStart = frameN  # exact frame index
                practice_center.tStart = t  # local t and not account for scr refresh
                practice_center.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_center, 'tStartRefresh')  # time at next scr refresh
                practice_center.setAutoDraw(True)
            if practice_center.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_center.tStartRefresh + duration_time-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_center.tStop = t  # not accounting for scr refresh
                    practice_center.frameNStop = frameN  # exact frame index
                    practice_center.setAutoDraw(False)
            
            # *practice_up* updates
            if practice_up.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                practice_up.frameNStart = frameN  # exact frame index
                practice_up.tStart = t  # local t and not account for scr refresh
                practice_up.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_up, 'tStartRefresh')  # time at next scr refresh
                practice_up.setAutoDraw(True)
            if practice_up.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_up.tStartRefresh + duration_time-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_up.tStop = t  # not accounting for scr refresh
                    practice_up.frameNStop = frameN  # exact frame index
                    practice_up.setAutoDraw(False)
            
            # *practice_down* updates
            if practice_down.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                practice_down.frameNStart = frameN  # exact frame index
                practice_down.tStart = t  # local t and not account for scr refresh
                practice_down.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_down, 'tStartRefresh')  # time at next scr refresh
                practice_down.setAutoDraw(True)
            if practice_down.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_down.tStartRefresh + duration_time-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_down.tStop = t  # not accounting for scr refresh
                    practice_down.frameNStop = frameN  # exact frame index
                    practice_down.setAutoDraw(False)
            
            # *practice_left* updates
            if practice_left.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                practice_left.frameNStart = frameN  # exact frame index
                practice_left.tStart = t  # local t and not account for scr refresh
                practice_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_left, 'tStartRefresh')  # time at next scr refresh
                practice_left.setAutoDraw(True)
            if practice_left.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_left.tStartRefresh + duration_time-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_left.tStop = t  # not accounting for scr refresh
                    practice_left.frameNStop = frameN  # exact frame index
                    practice_left.setAutoDraw(False)
            
            # *practice_right* updates
            if practice_right.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                practice_right.frameNStart = frameN  # exact frame index
                practice_right.tStart = t  # local t and not account for scr refresh
                practice_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_right, 'tStartRefresh')  # time at next scr refresh
                practice_right.setAutoDraw(True)
            if practice_right.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_right.tStartRefresh + duration_time-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_right.tStop = t  # not accounting for scr refresh
                    practice_right.frameNStop = frameN  # exact frame index
                    practice_right.setAutoDraw(False)
            
            # *practice_response* updates
            waitOnFlip = False
            if practice_response.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
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
                if tThisFlipGlobal > practice_response.tStartRefresh + duration_time-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_response.tStop = t  # not accounting for scr refresh
                    practice_response.frameNStop = frameN  # exact frame index
                    practice_response.status = FINISHED
            if practice_response.status == STARTED and not waitOnFlip:
                theseKeys = practice_response.getKeys(keyList=['up','down','left','right'], waitRelease=False)
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
        
        correct = judge(practice_answer,current_target,current_order)
        
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
# Run 'Begin Routine' code from init_experiment
# CONDITIONAL FLAG
experiment_stage = "experiment_prepare"

# DATA PREPARE
import random

experiment_trial_idx = 1
experiment_block_idx = 1
experiment_idx = 0

experiment_group_id = []
experiment_target_id = []
experiment_order_id = []
for i in range(experiment_block_nums*experiment_block_trials):
    experiment_group_id.append(
        random.randint(image_id_min,image_id_max)
    )
    experiment_target_id.append(
        random.randint(0,3)
    )
    experiment_order_id.append(
        random.randint(0,orders_count-1)
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
        
        # CONDITIONAL FLAG
        experiment_stage = "experiment"
        experiment_pressed = False
        experiment_answer = None
            
        # UPDATE IMAGE
        group_name = str(experiment_group_id[experiment_idx])
        current_target = str(experiment_target_id[experiment_idx])
        current_order = image_orders[experiment_order_id[experiment_idx]]
        
        
        experiment_right.image = image_root+"/"+group_name+"-"+current_order[0]+".png"
        experiment_down.image = image_root+"/"+group_name+"-"+current_order[1]+".png"
        experiment_left.image = image_root+"/"+group_name+"-"+current_order[2]+".png"
        experiment_up.image = image_root+"/"+group_name+"-"+current_order[3]+".png"
        
        experiment_center.image = image_root+"/"+group_name+"-"+current_target+".png"
        
        record(experiment_block_idx,experiment_trial_idx,"ImageGroup",group_name)
        record(experiment_block_idx,experiment_trial_idx,"CenterImage",current_target)
        for i in range(0,4):
            if(current_order[i]==current_target):
                record(experiment_block_idx,experiment_trial_idx,"CorrectPos",pos_mapping[i])
        experiment_response.keys = []
        experiment_response.rt = []
        _experiment_response_allKeys = []
        # keep track of which components have finished
        experiment_trialComponents = [experiment_cross, experiment_response, experiment_up, experiment_down, experiment_left, experiment_right, experiment_center]
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
                experiment_answer = experiment_response.keys
                
                record(experiment_block_idx,experiment_trial_idx,"ReactTime",t-experiment_response.tStart)
                record(experiment_block_idx,experiment_trial_idx,"AnswerPos",experiment_answer)
                
                continueRoutine = False
            
            
            
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
                if tThisFlipGlobal > experiment_response.tStartRefresh + duration_time-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_response.tStop = t  # not accounting for scr refresh
                    experiment_response.frameNStop = frameN  # exact frame index
                    experiment_response.status = FINISHED
            if experiment_response.status == STARTED and not waitOnFlip:
                theseKeys = experiment_response.getKeys(keyList=['up','down','left','right'], waitRelease=False)
                _experiment_response_allKeys.extend(theseKeys)
                if len(_experiment_response_allKeys):
                    experiment_response.keys = _experiment_response_allKeys[-1].name  # just the last key pressed
                    experiment_response.rt = _experiment_response_allKeys[-1].rt
            
            # *experiment_up* updates
            if experiment_up.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_up.frameNStart = frameN  # exact frame index
                experiment_up.tStart = t  # local t and not account for scr refresh
                experiment_up.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_up, 'tStartRefresh')  # time at next scr refresh
                experiment_up.setAutoDraw(True)
            if experiment_up.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_up.tStartRefresh + duration_time-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_up.tStop = t  # not accounting for scr refresh
                    experiment_up.frameNStop = frameN  # exact frame index
                    experiment_up.setAutoDraw(False)
            
            # *experiment_down* updates
            if experiment_down.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_down.frameNStart = frameN  # exact frame index
                experiment_down.tStart = t  # local t and not account for scr refresh
                experiment_down.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_down, 'tStartRefresh')  # time at next scr refresh
                experiment_down.setAutoDraw(True)
            if experiment_down.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_down.tStartRefresh + duration_time-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_down.tStop = t  # not accounting for scr refresh
                    experiment_down.frameNStop = frameN  # exact frame index
                    experiment_down.setAutoDraw(False)
            
            # *experiment_left* updates
            if experiment_left.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_left.frameNStart = frameN  # exact frame index
                experiment_left.tStart = t  # local t and not account for scr refresh
                experiment_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_left, 'tStartRefresh')  # time at next scr refresh
                experiment_left.setAutoDraw(True)
            if experiment_left.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_left.tStartRefresh + duration_time-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_left.tStop = t  # not accounting for scr refresh
                    experiment_left.frameNStop = frameN  # exact frame index
                    experiment_left.setAutoDraw(False)
            
            # *experiment_right* updates
            if experiment_right.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_right.frameNStart = frameN  # exact frame index
                experiment_right.tStart = t  # local t and not account for scr refresh
                experiment_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_right, 'tStartRefresh')  # time at next scr refresh
                experiment_right.setAutoDraw(True)
            if experiment_right.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_right.tStartRefresh + duration_time-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_right.tStop = t  # not accounting for scr refresh
                    experiment_right.frameNStop = frameN  # exact frame index
                    experiment_right.setAutoDraw(False)
            
            # *experiment_center* updates
            if experiment_center.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_center.frameNStart = frameN  # exact frame index
                experiment_center.tStart = t  # local t and not account for scr refresh
                experiment_center.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_center, 'tStartRefresh')  # time at next scr refresh
                experiment_center.setAutoDraw(True)
            if experiment_center.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_center.tStartRefresh + duration_time-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_center.tStop = t  # not accounting for scr refresh
                    experiment_center.frameNStop = frameN  # exact frame index
                    experiment_center.setAutoDraw(False)
            
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
        
        
        correct = judge(experiment_answer,current_target,current_order)
        
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
