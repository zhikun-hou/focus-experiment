#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 九月 18, 2022, at 23:57
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

# 参数接收模块  #bnu
# 在PsychoPy Builder中测试时注释掉sys.argv并手动输入参数
RECORD_NAME = sys.argv[1]
DATA_ROOT = sys.argv[2]
SUBJECT_NAME = sys.argv[3]
BLOCK_NUMS = int(sys.argv[4])
BLOCK_TRIALS = int(sys.argv[5])

# TEXT CONFIG
guide_text = "您好，欢迎参加本次实验\n在实验过程中，屏幕中央会出现一个注视点“＋”\n请保持注意集中，随后屏幕上将快速呈现一系列数字\n请您记住其中的红色数字和绿色数字\n之后按照问题输入对应数字\n按空格开始练习。"
practice_confirm_text = "练习已结束\n若您已了解本实验操作请按“Y”键，进入正式实验；\n若您还未熟悉实验操作请按“N”键，重新进行练习。"
experiment_rest_text = "请休息一下，当您觉得状态恢复良好时\n可随时按空格键继续。"
experiment_end_text = "试验结束，感谢参与\n按空格退出"


# 脑电连接模块 bnu
import socket
import tkinter.messagebox
host = '127.0.0.1'
port = 9237
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(30)
try :
    client.connect((host,port))
except socket.error:
    tkinter.messagebox.showinfo('错误','脑电采集设备未连接')
    core.quit()
inputData = bytes([0x55,0x01,0x5a,0x07,0x45,0x56,0x45,0x4e,0x54,0x5f,0x41,0xd9])
mark_resrig = bytes([0x55,0x01,0x5a,0x01,0x9a,0x4b])
mark_reswrg = bytes([0x55,0x01,0x5a,0x01,0x9b,0x4c])
mark_firsttarget = bytes([0x55,0x01,0x5a,0x01,0x01,0xB2])
mark_secondtarget = bytes([0x55,0x01,0x5a,0x01,0x02,0xb3])


# CONDITIONAL FLAG
experiment_stage = "before_experiment"
experiment_block_idx = 1

# PRACTICE CONFIG
practice_repeats = 8

# EXPERIMENT CONFIG
experiment_block_nums = BLOCK_NUMS#bnu
experiment_block_trials = BLOCK_TRIALS#bnu
experiment_idx = 0


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
    originPath='E:\\Work\\focus-experiment\\src\\tasks\\project\\oct_eeg.py',
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

# --- Initialize components for Routine "practice_trial" ---
practice_cross = visual.TextStim(win=win, name='practice_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
practice_number1 = visual.TextStim(win=win, name='practice_number1',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
practice_number_red = visual.TextStim(win=win, name='practice_number_red',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
practice_number2 = visual.TextStim(win=win, name='practice_number2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
practice_number_green = visual.TextStim(win=win, name='practice_number_green',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
practice_number3 = visual.TextStim(win=win, name='practice_number3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
practice_question_red = visual.TextStim(win=win, name='practice_question_red',
    text='红色数字是几？',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
practice_question_green = visual.TextStim(win=win, name='practice_question_green',
    text='绿色数字是几？',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
practice_response_red = keyboard.Keyboard()
practice_response_green = keyboard.Keyboard()

# --- Initialize components for Routine "practice_confirm" ---
practice_confirm_tip = visual.TextStim(win=win, name='practice_confirm_tip',
    text=practice_confirm_text,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practice_confirm_trigger = keyboard.Keyboard()

# --- Initialize components for Routine "experiment_trial" ---
# Run 'Begin Experiment' code from code_4
experiment_idx = 0
experiment_block_idx = 1
experiment_trial_idx = 1
experiment_cross = visual.TextStim(win=win, name='experiment_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
experiment_number1 = visual.TextStim(win=win, name='experiment_number1',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
experiment_number_red = visual.TextStim(win=win, name='experiment_number_red',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
experiment_number2 = visual.TextStim(win=win, name='experiment_number2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
experiment_number_green = visual.TextStim(win=win, name='experiment_number_green',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
experiment_number3 = visual.TextStim(win=win, name='experiment_number3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
experiment_question_red = visual.TextStim(win=win, name='experiment_question_red',
    text='红色数字是几？',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
experiment_question_green = visual.TextStim(win=win, name='experiment_question_green',
    text='绿色数字是几？',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
experiment_response_red = keyboard.Keyboard()
experiment_response_green = keyboard.Keyboard()

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
        answer_red = None
        answer_green = None
        
        # UPDATE TEXT
        import random
        practice_number1.text = str(random.randint(0,9))
        practice_number2.text = str(random.randint(0,9))
        practice_number3.text = str(random.randint(0,9))
        
        number_red = str(random.randint(0,9))
        number_green = str(random.randint(0,9))
        practice_number_red.text = number_red
        practice_number_green.text = number_green
        
        
        thisExp.addData("shownum_red",number_red)
        thisExp.addData("shownum_green",number_green)
        practice_response_red.keys = []
        practice_response_red.rt = []
        _practice_response_red_allKeys = []
        practice_response_green.keys = []
        practice_response_green.rt = []
        _practice_response_green_allKeys = []
        # keep track of which components have finished
        practice_trialComponents = [practice_cross, practice_number1, practice_number_red, practice_number2, practice_number_green, practice_number3, practice_question_red, practice_question_green, practice_response_red, practice_response_green]
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
            
            if(practice_response_red.status==STARTED):
                if(answer_red==None and len(practice_response_red.keys)>0):
                    answer_red = practice_response_red.keys[-1]
            
            if(practice_response_green.status==STARTED):
                if(answer_green==None and len(practice_response_green.keys)>0):
                    answer_green = practice_response_green.keys[-1]
            
            #bnu
            if practice_number_red.status == NOT_STARTED and tThisFlip >= 1.08-frameTolerance:
                client.send(mark_firsttarget)
                
            #bnu
            if practice_number_green.status == NOT_STARTED and tThisFlip >= 1.24-frameTolerance:
                client.send(mark_secondtarget)
            
            
            
            # *practice_cross* updates
            if practice_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_cross.frameNStart = frameN  # exact frame index
                practice_cross.tStart = t  # local t and not account for scr refresh
                practice_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_cross, 'tStartRefresh')  # time at next scr refresh
                practice_cross.setAutoDraw(True)
            if practice_cross.status == STARTED:
                if bool(practice_number1.status==STARTED):
                    # keep track of stop time/frame for later
                    practice_cross.tStop = t  # not accounting for scr refresh
                    practice_cross.frameNStop = frameN  # exact frame index
                    practice_cross.setAutoDraw(False)
            
            # *practice_number1* updates
            if practice_number1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                practice_number1.frameNStart = frameN  # exact frame index
                practice_number1.tStart = t  # local t and not account for scr refresh
                practice_number1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_number1, 'tStartRefresh')  # time at next scr refresh
                practice_number1.setAutoDraw(True)
            if practice_number1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_number1.tStartRefresh + 0.08-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_number1.tStop = t  # not accounting for scr refresh
                    practice_number1.frameNStop = frameN  # exact frame index
                    practice_number1.setAutoDraw(False)
            
            # *practice_number_red* updates
            if practice_number_red.status == NOT_STARTED and tThisFlip >= 1.08-frameTolerance:
                # keep track of start time/frame for later
                practice_number_red.frameNStart = frameN  # exact frame index
                practice_number_red.tStart = t  # local t and not account for scr refresh
                practice_number_red.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_number_red, 'tStartRefresh')  # time at next scr refresh
                practice_number_red.setAutoDraw(True)
            if practice_number_red.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_number_red.tStartRefresh + 0.08-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_number_red.tStop = t  # not accounting for scr refresh
                    practice_number_red.frameNStop = frameN  # exact frame index
                    practice_number_red.setAutoDraw(False)
            
            # *practice_number2* updates
            if practice_number2.status == NOT_STARTED and tThisFlip >= 1.16-frameTolerance:
                # keep track of start time/frame for later
                practice_number2.frameNStart = frameN  # exact frame index
                practice_number2.tStart = t  # local t and not account for scr refresh
                practice_number2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_number2, 'tStartRefresh')  # time at next scr refresh
                practice_number2.setAutoDraw(True)
            if practice_number2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_number2.tStartRefresh + 0.08-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_number2.tStop = t  # not accounting for scr refresh
                    practice_number2.frameNStop = frameN  # exact frame index
                    practice_number2.setAutoDraw(False)
            
            # *practice_number_green* updates
            if practice_number_green.status == NOT_STARTED and tThisFlip >= 1.24-frameTolerance:
                # keep track of start time/frame for later
                practice_number_green.frameNStart = frameN  # exact frame index
                practice_number_green.tStart = t  # local t and not account for scr refresh
                practice_number_green.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_number_green, 'tStartRefresh')  # time at next scr refresh
                practice_number_green.setAutoDraw(True)
            if practice_number_green.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_number_green.tStartRefresh + 0.08-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_number_green.tStop = t  # not accounting for scr refresh
                    practice_number_green.frameNStop = frameN  # exact frame index
                    practice_number_green.setAutoDraw(False)
            
            # *practice_number3* updates
            if practice_number3.status == NOT_STARTED and tThisFlip >= 1.32-frameTolerance:
                # keep track of start time/frame for later
                practice_number3.frameNStart = frameN  # exact frame index
                practice_number3.tStart = t  # local t and not account for scr refresh
                practice_number3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_number3, 'tStartRefresh')  # time at next scr refresh
                practice_number3.setAutoDraw(True)
            if practice_number3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_number3.tStartRefresh + 0.08-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_number3.tStop = t  # not accounting for scr refresh
                    practice_number3.frameNStop = frameN  # exact frame index
                    practice_number3.setAutoDraw(False)
            
            # *practice_question_red* updates
            if practice_question_red.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
                # keep track of start time/frame for later
                practice_question_red.frameNStart = frameN  # exact frame index
                practice_question_red.tStart = t  # local t and not account for scr refresh
                practice_question_red.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_question_red, 'tStartRefresh')  # time at next scr refresh
                practice_question_red.setAutoDraw(True)
            if practice_question_red.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_question_red.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_question_red.tStop = t  # not accounting for scr refresh
                    practice_question_red.frameNStop = frameN  # exact frame index
                    practice_question_red.setAutoDraw(False)
            
            # *practice_question_green* updates
            if practice_question_green.status == NOT_STARTED and tThisFlip >= 3.8-frameTolerance:
                # keep track of start time/frame for later
                practice_question_green.frameNStart = frameN  # exact frame index
                practice_question_green.tStart = t  # local t and not account for scr refresh
                practice_question_green.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_question_green, 'tStartRefresh')  # time at next scr refresh
                practice_question_green.setAutoDraw(True)
            if practice_question_green.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_question_green.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_question_green.tStop = t  # not accounting for scr refresh
                    practice_question_green.frameNStop = frameN  # exact frame index
                    practice_question_green.setAutoDraw(False)
            
            # *practice_response_red* updates
            waitOnFlip = False
            if practice_response_red.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
                # keep track of start time/frame for later
                practice_response_red.frameNStart = frameN  # exact frame index
                practice_response_red.tStart = t  # local t and not account for scr refresh
                practice_response_red.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_response_red, 'tStartRefresh')  # time at next scr refresh
                practice_response_red.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(practice_response_red.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(practice_response_red.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if practice_response_red.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_response_red.tStartRefresh + 2.2-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_response_red.tStop = t  # not accounting for scr refresh
                    practice_response_red.frameNStop = frameN  # exact frame index
                    practice_response_red.status = FINISHED
            if practice_response_red.status == STARTED and not waitOnFlip:
                theseKeys = practice_response_red.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0','num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9','num_0'], waitRelease=False)
                _practice_response_red_allKeys.extend(theseKeys)
                if len(_practice_response_red_allKeys):
                    practice_response_red.keys = _practice_response_red_allKeys[-1].name  # just the last key pressed
                    practice_response_red.rt = _practice_response_red_allKeys[-1].rt
            
            # *practice_response_green* updates
            waitOnFlip = False
            if practice_response_green.status == NOT_STARTED and tThisFlip >= 3.8-frameTolerance:
                # keep track of start time/frame for later
                practice_response_green.frameNStart = frameN  # exact frame index
                practice_response_green.tStart = t  # local t and not account for scr refresh
                practice_response_green.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_response_green, 'tStartRefresh')  # time at next scr refresh
                practice_response_green.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(practice_response_green.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(practice_response_green.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if practice_response_green.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_response_green.tStartRefresh + 2.2-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_response_green.tStop = t  # not accounting for scr refresh
                    practice_response_green.frameNStop = frameN  # exact frame index
                    practice_response_green.status = FINISHED
            if practice_response_green.status == STARTED and not waitOnFlip:
                theseKeys = practice_response_green.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0','num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9','num_0''1','2','3','4''5','6','7','8','9','0','num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9','num_0'], waitRelease=False)
                _practice_response_green_allKeys.extend(theseKeys)
                if len(_practice_response_green_allKeys):
                    practice_response_green.keys = _practice_response_green_allKeys[-1].name  # just the last key pressed
                    practice_response_green.rt = _practice_response_green_allKeys[-1].rt
            
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
        
        thisExp.addData('answer_red', answer_red)
        thisExp.addData('answer_green', answer_green)
           
        
        thisExp.addData('correct_red', answer_red==number_red)
        thisExp.addData('correct_green', answer_green==number_green)
        
        
        #bnu
        if(answer_red==number_red):
            client.send(mark_resrig)
        else:
            client.send(mark_reswrg)
        if(answer_green==number_green):
            client.send(mark_resrig)
        else:
            client.send(mark_reswrg)
        # the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
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
        answer_red = None
        answer_green = None
        
        # UPDATE TEXT
        import random
        experiment_number1.text = str(random.randint(0,9))
        experiment_number2.text = str(random.randint(0,9))
        experiment_number3.text = str(random.randint(0,9))
        
        number_red = str(random.randint(0,9))
        number_green = str(random.randint(0,9))
        experiment_number_red.text = number_red
        experiment_number_green.text = number_green
        
        
        experiment_idx+=1
        
        record(experiment_block_idx,experiment_trial_idx,"ShowNum_Red",number_red)
        record(experiment_block_idx,experiment_trial_idx,"ShowNum_Green",number_green)
        experiment_response_red.keys = []
        experiment_response_red.rt = []
        _experiment_response_red_allKeys = []
        experiment_response_green.keys = []
        experiment_response_green.rt = []
        _experiment_response_green_allKeys = []
        # keep track of which components have finished
        experiment_trialComponents = [experiment_cross, experiment_number1, experiment_number_red, experiment_number2, experiment_number_green, experiment_number3, experiment_question_red, experiment_question_green, experiment_response_red, experiment_response_green]
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
            
            if(experiment_response_red.status==STARTED):
                if(answer_red==None and len(experiment_response_red.keys)>0):
                    answer_red = experiment_response_red.keys[-1]
            
            if(experiment_response_green.status==STARTED):
                if(answer_green==None and len(experiment_response_green.keys)>0):
                    answer_green = experiment_response_green.keys[-1]
            
            # bnu
            if experiment_number_red.status == NOT_STARTED and tThisFlip >= 1.08-frameTolerance:
                client.send(mark_firsttarget)
            
            # bnu
            if experiment_number_green.status == NOT_STARTED and tThisFlip >= 1.24-frameTolerance:
                client.send(mark_secondtarget)
                
            
            
            
            
            # *experiment_cross* updates
            if experiment_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                experiment_cross.frameNStart = frameN  # exact frame index
                experiment_cross.tStart = t  # local t and not account for scr refresh
                experiment_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_cross, 'tStartRefresh')  # time at next scr refresh
                experiment_cross.setAutoDraw(True)
            if experiment_cross.status == STARTED:
                if bool(experiment_number1.status==STARTED):
                    # keep track of stop time/frame for later
                    experiment_cross.tStop = t  # not accounting for scr refresh
                    experiment_cross.frameNStop = frameN  # exact frame index
                    experiment_cross.setAutoDraw(False)
            
            # *experiment_number1* updates
            if experiment_number1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_number1.frameNStart = frameN  # exact frame index
                experiment_number1.tStart = t  # local t and not account for scr refresh
                experiment_number1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_number1, 'tStartRefresh')  # time at next scr refresh
                experiment_number1.setAutoDraw(True)
            if experiment_number1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_number1.tStartRefresh + 0.08-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_number1.tStop = t  # not accounting for scr refresh
                    experiment_number1.frameNStop = frameN  # exact frame index
                    experiment_number1.setAutoDraw(False)
            
            # *experiment_number_red* updates
            if experiment_number_red.status == NOT_STARTED and tThisFlip >= 1.08-frameTolerance:
                # keep track of start time/frame for later
                experiment_number_red.frameNStart = frameN  # exact frame index
                experiment_number_red.tStart = t  # local t and not account for scr refresh
                experiment_number_red.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_number_red, 'tStartRefresh')  # time at next scr refresh
                experiment_number_red.setAutoDraw(True)
            if experiment_number_red.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_number_red.tStartRefresh + 0.08-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_number_red.tStop = t  # not accounting for scr refresh
                    experiment_number_red.frameNStop = frameN  # exact frame index
                    experiment_number_red.setAutoDraw(False)
            
            # *experiment_number2* updates
            if experiment_number2.status == NOT_STARTED and tThisFlip >= 1.16-frameTolerance:
                # keep track of start time/frame for later
                experiment_number2.frameNStart = frameN  # exact frame index
                experiment_number2.tStart = t  # local t and not account for scr refresh
                experiment_number2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_number2, 'tStartRefresh')  # time at next scr refresh
                experiment_number2.setAutoDraw(True)
            if experiment_number2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_number2.tStartRefresh + 0.08-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_number2.tStop = t  # not accounting for scr refresh
                    experiment_number2.frameNStop = frameN  # exact frame index
                    experiment_number2.setAutoDraw(False)
            
            # *experiment_number_green* updates
            if experiment_number_green.status == NOT_STARTED and tThisFlip >= 1.24-frameTolerance:
                # keep track of start time/frame for later
                experiment_number_green.frameNStart = frameN  # exact frame index
                experiment_number_green.tStart = t  # local t and not account for scr refresh
                experiment_number_green.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_number_green, 'tStartRefresh')  # time at next scr refresh
                experiment_number_green.setAutoDraw(True)
            if experiment_number_green.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_number_green.tStartRefresh + 0.08-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_number_green.tStop = t  # not accounting for scr refresh
                    experiment_number_green.frameNStop = frameN  # exact frame index
                    experiment_number_green.setAutoDraw(False)
            
            # *experiment_number3* updates
            if experiment_number3.status == NOT_STARTED and tThisFlip >= 1.32-frameTolerance:
                # keep track of start time/frame for later
                experiment_number3.frameNStart = frameN  # exact frame index
                experiment_number3.tStart = t  # local t and not account for scr refresh
                experiment_number3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_number3, 'tStartRefresh')  # time at next scr refresh
                experiment_number3.setAutoDraw(True)
            if experiment_number3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_number3.tStartRefresh + 0.08-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_number3.tStop = t  # not accounting for scr refresh
                    experiment_number3.frameNStop = frameN  # exact frame index
                    experiment_number3.setAutoDraw(False)
            
            # *experiment_question_red* updates
            if experiment_question_red.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
                # keep track of start time/frame for later
                experiment_question_red.frameNStart = frameN  # exact frame index
                experiment_question_red.tStart = t  # local t and not account for scr refresh
                experiment_question_red.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_question_red, 'tStartRefresh')  # time at next scr refresh
                experiment_question_red.setAutoDraw(True)
            if experiment_question_red.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_question_red.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_question_red.tStop = t  # not accounting for scr refresh
                    experiment_question_red.frameNStop = frameN  # exact frame index
                    experiment_question_red.setAutoDraw(False)
            
            # *experiment_question_green* updates
            if experiment_question_green.status == NOT_STARTED and tThisFlip >= 3.8-frameTolerance:
                # keep track of start time/frame for later
                experiment_question_green.frameNStart = frameN  # exact frame index
                experiment_question_green.tStart = t  # local t and not account for scr refresh
                experiment_question_green.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_question_green, 'tStartRefresh')  # time at next scr refresh
                experiment_question_green.setAutoDraw(True)
            if experiment_question_green.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_question_green.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_question_green.tStop = t  # not accounting for scr refresh
                    experiment_question_green.frameNStop = frameN  # exact frame index
                    experiment_question_green.setAutoDraw(False)
            
            # *experiment_response_red* updates
            waitOnFlip = False
            if experiment_response_red.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
                # keep track of start time/frame for later
                experiment_response_red.frameNStart = frameN  # exact frame index
                experiment_response_red.tStart = t  # local t and not account for scr refresh
                experiment_response_red.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_response_red, 'tStartRefresh')  # time at next scr refresh
                experiment_response_red.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(experiment_response_red.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(experiment_response_red.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if experiment_response_red.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_response_red.tStartRefresh + 2.2-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_response_red.tStop = t  # not accounting for scr refresh
                    experiment_response_red.frameNStop = frameN  # exact frame index
                    experiment_response_red.status = FINISHED
            if experiment_response_red.status == STARTED and not waitOnFlip:
                theseKeys = experiment_response_red.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0','num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9','num_0'], waitRelease=False)
                _experiment_response_red_allKeys.extend(theseKeys)
                if len(_experiment_response_red_allKeys):
                    experiment_response_red.keys = _experiment_response_red_allKeys[-1].name  # just the last key pressed
                    experiment_response_red.rt = _experiment_response_red_allKeys[-1].rt
            
            # *experiment_response_green* updates
            waitOnFlip = False
            if experiment_response_green.status == NOT_STARTED and tThisFlip >= 3.8-frameTolerance:
                # keep track of start time/frame for later
                experiment_response_green.frameNStart = frameN  # exact frame index
                experiment_response_green.tStart = t  # local t and not account for scr refresh
                experiment_response_green.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_response_green, 'tStartRefresh')  # time at next scr refresh
                experiment_response_green.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(experiment_response_green.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(experiment_response_green.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if experiment_response_green.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_response_green.tStartRefresh + 2.2-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_response_green.tStop = t  # not accounting for scr refresh
                    experiment_response_green.frameNStop = frameN  # exact frame index
                    experiment_response_green.status = FINISHED
            if experiment_response_green.status == STARTED and not waitOnFlip:
                theseKeys = experiment_response_green.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0','num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9','num_0''1','2','3','4''5','6','7','8','9','0','num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9','num_0'], waitRelease=False)
                _experiment_response_green_allKeys.extend(theseKeys)
                if len(_experiment_response_green_allKeys):
                    experiment_response_green.keys = _experiment_response_green_allKeys[-1].name  # just the last key pressed
                    experiment_response_green.rt = _experiment_response_green_allKeys[-1].rt
            
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
        
        
        record(experiment_block_idx,experiment_trial_idx,"Answer_Red",answer_red)
        record(experiment_block_idx,experiment_trial_idx,"Answer_Green",answer_green)
        
        record(experiment_block_idx,experiment_trial_idx,"Correct_Red",answer_red==number_red)
        record(experiment_block_idx,experiment_trial_idx,"Correct_Green",answer_green==number_green)
        
        
        #bnu
        if(answer_red==number_red):
            client.send(mark_resrig)
        else:
            client.send(mark_reswrg)
        if(answer_green==number_green):
            client.send(mark_resrig)
        else:
            client.send(mark_reswrg)
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
