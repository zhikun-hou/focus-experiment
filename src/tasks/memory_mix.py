#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 十月 16, 2022, at 22:33
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
guide_text = "您好，欢迎参加本次实验\n在实验过程中，屏幕中央会出现一个注视点“+”\n随后屏幕上将快速呈现一系列数字与字母\n请记住其出现顺序，随后逐个输入并按空格提交\n明白后按空格开始练习。"
practice_confirm_text = "练习已结束\n若您已了解本实验操作请按“Y”键，进入正式实验；\n若您还未熟悉实验操作请按“N”键，重新进行练习。"
experiment_rest_text = "请休息一下，当您觉得状态恢复良好时\n可随时按空格键继续。"
experiment_end_text = "试验结束，感谢参与\n按空格退出"

practice_answer_tip_text = "请按键作答(退格删除 空格提交)"
experiment_answer_tip_text = "请按键作答"

# CONDITIONAL FLAG
experiment_stage = "before_experiment"

# PRACTICE CONFIG
practice_repeats = 3

# EXPERIMENT CONFIG
experiment_block_nums = 3
experiment_block_trials = 8


sequence_length = 6
char_duration = 0.5
blank_duration = 0.2

import random
charset = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
charset_length = len(charset)

def generate_sequence(length):
    seq = []
    for i in range(length):
        seq.append(
            charset[random.randint(0,charset_length-1)]# python的randint不是左闭右开
        )
    return seq
    



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
#     originPath='E:\\Work\\focus-experiment\\src\\tasks\\project\\memory_mix.py',
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

# --- Initialize components for Routine "practice_trial" ---
practice_cross = visual.TextStim(win=win, name='practice_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
practice_char = visual.TextStim(win=win, name='practice_char',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "practice_answer" ---
practice_input = visual.TextStim(win=win, name='practice_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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
experiment_char = visual.TextStim(win=win, name='experiment_char',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "experiment_answer" ---
experiment_input = visual.TextStim(win=win, name='experiment_input',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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
        
        # UPDATE TEXT
        practice_seq = generate_sequence(sequence_length)
        
        
        
        last_char = -1
        last_blank = -1
        # keep track of which components have finished
        practice_trialComponents = [practice_cross, practice_char]
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
            
            if practice_char.status == STARTED:
            
                period_t = (t - practice_char.tStart)%(char_duration+blank_duration)
                period_i = int((t - practice_char.tStart)/(char_duration+blank_duration))
            
                if( period_i >= sequence_length):
                    continueRoutine = False
                elif( period_i!=last_char and period_t < char_duration ):
                    practice_char.text = practice_seq[period_i]
                    last_char = period_i
                elif( period_i!=last_blank and period_t >=char_duration ):
                    practice_char.text = ""
                    last_blank = period_i
            
            
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
                if tThisFlipGlobal > practice_cross.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_cross.tStop = t  # not accounting for scr refresh
                    practice_cross.frameNStop = frameN  # exact frame index
                    practice_cross.setAutoDraw(False)
            
            # *practice_char* updates
            if practice_char.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                practice_char.frameNStart = frameN  # exact frame index
                practice_char.tStart = t  # local t and not account for scr refresh
                practice_char.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_char, 'tStartRefresh')  # time at next scr refresh
                practice_char.setAutoDraw(True)
            
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
        # the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "practice_answer" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_6
        
        # 必须要空格提交才算有效回答
        confirmed = False
        
        answer = []
        
        inputset = ['backspace','space',*charset]
        
        event.clearEvents()
        
        practice_input.text = practice_answer_tip_text
        # keep track of which components have finished
        practice_answerComponents = [practice_input]
        for thisComponent in practice_answerComponents:
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
        
        # --- Run Routine "practice_answer" ---
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practice_input* updates
            if practice_input.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_input.frameNStart = frameN  # exact frame index
                practice_input.tStart = t  # local t and not account for scr refresh
                practice_input.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_input, 'tStartRefresh')  # time at next scr refresh
                practice_input.setAutoDraw(True)
            if practice_input.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_input.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_input.tStop = t  # not accounting for scr refresh
                    practice_input.frameNStop = frameN  # exact frame index
                    practice_input.setAutoDraw(False)
            # Run 'Each Frame' code from code_6
            
            
            inputs = event.getKeys(inputset)
            if(len(inputs)>0):
                
                if(inputs[0]=="backspace"):
                    if(len(answer)>0):
                        answer.pop()
                    practice_input.text = ''.join(answer)
                elif(inputs[0]=="space"):
                    confirmed = True
                    continueRoutine = False
                else:
                    answer.append(inputs[0])
                    practice_input.text = ''.join(answer)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_answerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_answer" ---
        for thisComponent in practice_answerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "practice_feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from practice_judge
        
        corrent = confirmed and answer==practice_seq
        if(corrent):
            practice_response_tip.text = "正确"
        else:
            practice_response_tip.text = "错误"
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
        # CONDITIONAL FLAG
        experiment_stage = "experiment"
        
        # UPDATE TEXT
        experiment_seq = generate_sequence(sequence_length)
        
        record(experiment_block_idx,experiment_trial_idx,"Sequence",experiment_seq)
        
        last_char = -1
        last_blank = -1
        # keep track of which components have finished
        experiment_trialComponents = [experiment_cross, experiment_char]
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
            
            if experiment_char.status == STARTED:
            
                period_t = (t - experiment_char.tStart)%(char_duration+blank_duration)
                period_i = int((t - experiment_char.tStart)/(char_duration+blank_duration))
            
                if( period_i >= sequence_length):
                    continueRoutine = False
                elif( period_i!=last_char and period_t < char_duration ):
                    experiment_char.text = experiment_seq[period_i]
                    last_char = period_i
                elif( period_i!=last_blank and period_t >=char_duration ):
                    experiment_char.text = ""
                    last_blank = period_i
            
            
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
                if tThisFlipGlobal > experiment_cross.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_cross.tStop = t  # not accounting for scr refresh
                    experiment_cross.frameNStop = frameN  # exact frame index
                    experiment_cross.setAutoDraw(False)
            
            # *experiment_char* updates
            if experiment_char.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                experiment_char.frameNStart = frameN  # exact frame index
                experiment_char.tStart = t  # local t and not account for scr refresh
                experiment_char.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_char, 'tStartRefresh')  # time at next scr refresh
                experiment_char.setAutoDraw(True)
            
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
        
           
            
        
        # the Routine "experiment_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "experiment_answer" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_7
        
        # 必须要空格提交才算有效回答
        confirmed = False
        
        answer = []
        
        inputset = ['backspace','space',*charset]
        
        event.clearEvents()
        
        experiment_input.text = experiment_answer_tip_text
        # keep track of which components have finished
        experiment_answerComponents = [experiment_input]
        for thisComponent in experiment_answerComponents:
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
        
        # --- Run Routine "experiment_answer" ---
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *experiment_input* updates
            if experiment_input.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                experiment_input.frameNStart = frameN  # exact frame index
                experiment_input.tStart = t  # local t and not account for scr refresh
                experiment_input.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_input, 'tStartRefresh')  # time at next scr refresh
                experiment_input.setAutoDraw(True)
            if experiment_input.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_input.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_input.tStop = t  # not accounting for scr refresh
                    experiment_input.frameNStop = frameN  # exact frame index
                    experiment_input.setAutoDraw(False)
            # Run 'Each Frame' code from code_7
            
            
            inputs = event.getKeys(inputset)
            if(len(inputs)>0):
                
                if(inputs[0]=="backspace"):
                    if(len(answer)>0):
                        answer.pop()
                    experiment_input.text = ''.join(answer)
                elif(inputs[0]=="space"):
                    confirmed = True
                    continueRoutine = False
                else:
                    answer.append(inputs[0])
                    experiment_input.text = ''.join(answer)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in experiment_answerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "experiment_answer" ---
        for thisComponent in experiment_answerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_7
        
        correct = confirmed and answer==experiment_seq
        
        record(experiment_block_idx,experiment_trial_idx,"Correct",correct)
        record(experiment_block_idx,experiment_trial_idx,"Submit",confirmed)
        record(experiment_block_idx,experiment_trial_idx,"Answer",answer)
        
        
        experiment_trial_idx +=1
        experiment_idx += 1
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
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
