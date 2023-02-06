#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 九月 18, 2022, at 23:59
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



BLOCK_NUMS = CONFIG["BLOCK_NUMS"]
BLOCK_TRIALS = CONFIG["BLOCK_TRIALS"]

# 脑电连接模块 bnu
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
mark_weizhi = [mark_rig,mark_down,mark_left,mark_up]

# TEXT CONFIG
guide_text = "您好，欢迎参加本次实验\n在实验过程中，屏幕中央会呈现一个“＋”\n在“＋”的四周会呈现很多的方块和一个圆形\n请注视屏幕中央，用余光寻找圆形图案\n当圆形出现在屏幕上方时按“F”做出反应，\n当圆形出现在屏幕下方时按“J”做出反应\n明白实验后按空格键进入练习。"
practice_confirm_text = "练习已结束，\n若您已了解本实验操作请按“Y”键，进入正式实验；\n若您还未熟悉实验操作请按“N”键，重新进行练习。"
experiment_rest_text = "请休息一下，当您觉得状态恢复良好时\n可随时按空格键继续。"
experiment_end_text = "实验结束，感谢参与\n按空格退出"

# CONDITIONAL FLAG
experiment_stage = "before_experiment

# PRACTICE CONFIG
practice_repeats = 8
practice_idx = 0

# EXPERIMENT CONFIG
experiment_block_nums = BLOCK_NUMS#bnu
experiment_block_trials = BLOCK_TRIALS#bnu



# DATA PREPARE
import itertools
show_orders = []
for x in  itertools.permutations([1, 2, 3, 4],4):
    show_orders.append(x)
    
orders_count = len(show_orders)

order_mapping = ["f","j","j","f"]


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
#     originPath='E:\\Work\\focus-experiment\\src\\tasks\\project\\vs_eeg.py',
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
practice_response = keyboard.Keyboard()
practice_cross = visual.TextStim(win=win, name='practice_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
rect_1 = visual.Rect(
    win=win, name='rect_1',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.15, 0.35), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
rect_2 = visual.Rect(
    win=win, name='rect_2',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.27, 0.27), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
rect_3 = visual.Rect(
    win=win, name='rect_3',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.4, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
rect_4 = visual.Rect(
    win=win, name='rect_4',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.4, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
rect_5 = visual.Rect(
    win=win, name='rect_5',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0, -0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
rect_6 = visual.Rect(
    win=win, name='rect_6',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.35, 0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
rect_7 = visual.Rect(
    win=win, name='rect_7',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.35, -0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
rect_8 = visual.Rect(
    win=win, name='rect_8',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.27, -0.27), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)
rect_9 = visual.Rect(
    win=win, name='rect_9',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.15, -0.35), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-11.0, interpolate=True)
rect_10 = visual.Rect(
    win=win, name='rect_10',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.35, -0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-12.0, interpolate=True)
rect_11 = visual.Rect(
    win=win, name='rect_11',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.15, -0.35), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-13.0, interpolate=True)
rect_12 = visual.Rect(
    win=win, name='rect_12',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.27, -0.27), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-14.0, interpolate=True)
rect_13 = visual.Rect(
    win=win, name='rect_13',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.15, 0.35), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-15.0, interpolate=True)
rect_14 = visual.Rect(
    win=win, name='rect_14',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.27, 0.27), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-16.0, interpolate=True)
rect_15 = visual.Rect(
    win=win, name='rect_15',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0, 0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-17.0, interpolate=True)
rect_16 = visual.Rect(
    win=win, name='rect_16',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.35, 0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-18.0, interpolate=True)
circle_1 = visual.ShapeStim(
    win=win, name='circle_1',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(0.35, 0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-19.0, interpolate=True)
circle_2 = visual.ShapeStim(
    win=win, name='circle_2',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(0.15, -0.35), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-20.0, interpolate=True)
circle_3 = visual.ShapeStim(
    win=win, name='circle_3',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(-0.35, -0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-21.0, interpolate=True)
circle_4 = visual.ShapeStim(
    win=win, name='circle_4',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(-0.15, 0.35), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-22.0, interpolate=True)

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
experiment_response = keyboard.Keyboard()
experiment_cross = visual.TextStim(win=win, name='experiment_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
experiment_rect1 = visual.Rect(
    win=win, name='experiment_rect1',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.15, 0.35), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
experiment_rect2 = visual.Rect(
    win=win, name='experiment_rect2',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.27, 0.27), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
experiment_rect3 = visual.Rect(
    win=win, name='experiment_rect3',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.4, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
experiment_rect4 = visual.Rect(
    win=win, name='experiment_rect4',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.4, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
experiment_rect5 = visual.Rect(
    win=win, name='experiment_rect5',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0, -0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
experiment_rect6 = visual.Rect(
    win=win, name='experiment_rect6',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.35, 0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
experiment_rect7 = visual.Rect(
    win=win, name='experiment_rect7',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.35, -0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
experiment_rect8 = visual.Rect(
    win=win, name='experiment_rect8',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.27, -0.27), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)
experiment_rect9 = visual.Rect(
    win=win, name='experiment_rect9',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0.15, -0.35), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-11.0, interpolate=True)
experiment_rect10 = visual.Rect(
    win=win, name='experiment_rect10',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.35, -0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-12.0, interpolate=True)
experiment_rect11 = visual.Rect(
    win=win, name='experiment_rect11',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.15, -0.35), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-13.0, interpolate=True)
experiment_rect12 = visual.Rect(
    win=win, name='experiment_rect12',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.27, -0.27), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-14.0, interpolate=True)
experiment_rect13 = visual.Rect(
    win=win, name='experiment_rect13',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.15, 0.35), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-15.0, interpolate=True)
experiment_rect14 = visual.Rect(
    win=win, name='experiment_rect14',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.27, 0.27), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-16.0, interpolate=True)
experiment_rect15 = visual.Rect(
    win=win, name='experiment_rect15',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(0, 0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-17.0, interpolate=True)
experiment_rect16 = visual.Rect(
    win=win, name='experiment_rect16',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45.0, pos=(-0.35, 0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-18.0, interpolate=True)
experiment_circle1 = visual.ShapeStim(
    win=win, name='experiment_circle1',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(0.35, 0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-19.0, interpolate=True)
experiment_circle2 = visual.ShapeStim(
    win=win, name='experiment_circle2',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(0.15, -0.35), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-20.0, interpolate=True)
experiment_circle3 = visual.ShapeStim(
    win=win, name='experiment_circle3',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(-0.35, -0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-21.0, interpolate=True)
experiment_circle4 = visual.ShapeStim(
    win=win, name='experiment_circle4',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(-0.15, 0.35), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-22.0, interpolate=True)

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
    
    practice_order_table = []        
    for i in range(0,practice_repeats):
        x = random.randint(0,orders_count-1)
        practice_order_table.append(x)
        
    
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
    # Run 'End Routine' code from init_practice
    for c in goodportary:#bnu
        try:
            c.send(mark_start)
    except:
        tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
        core.quit()
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
        practice_answer = None
            
        # UPDATE TEXT
        group_id = practice_order_table[(int)(practice_idx/4)]
        show_id = show_orders[group_id][(practice_idx+1)%4] - 1 
        
        
        circles = [circle_1,circle_2,circle_3,circle_4]
        rects = [rect_6,rect_9,rect_10,rect_13]
        
        for i in range(0,4):
            if i==show_id:
                circles[i].opacity = 1
                rects[i].opacity = 0
            else:
                circles[i].opacity = 0
                rects[i].opacity = 1
                
                
        practice_response.keys = []
        practice_response.rt = []
        _practice_response_allKeys = []
        # keep track of which components have finished
        practice_trialComponents = [practice_response, practice_cross, rect_1, rect_2, rect_3, rect_4, rect_5, rect_6, rect_7, rect_8, rect_9, rect_10, rect_11, rect_12, rect_13, rect_14, rect_15, rect_16, circle_1, circle_2, circle_3, circle_4]
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
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_2
            
            if(practice_answer==None and practice_response.status==STARTED and len(practice_response.keys)>0):
                practice_answer = practice_response.keys[0]
            
                
            # bnu
            if practice_cross.status == STARTED:
                if tThisFlipGlobal > practice_cross.tStartRefresh + 1-frameTolerance:
                    for c in goodportary:#bnu
                        try:
                            c.send(mark_weizhi[show_id])
                        except:
                            tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                            core.quit()
            
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
                if tThisFlipGlobal > practice_response.tStartRefresh + 2-frameTolerance:
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
            
            # *rect_1* updates
            if rect_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_1.frameNStart = frameN  # exact frame index
                rect_1.tStart = t  # local t and not account for scr refresh
                rect_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_1, 'tStartRefresh')  # time at next scr refresh
                rect_1.setAutoDraw(True)
            if rect_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_1.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_1.tStop = t  # not accounting for scr refresh
                    rect_1.frameNStop = frameN  # exact frame index
                    rect_1.setAutoDraw(False)
            
            # *rect_2* updates
            if rect_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_2.frameNStart = frameN  # exact frame index
                rect_2.tStart = t  # local t and not account for scr refresh
                rect_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_2, 'tStartRefresh')  # time at next scr refresh
                rect_2.setAutoDraw(True)
            if rect_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_2.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_2.tStop = t  # not accounting for scr refresh
                    rect_2.frameNStop = frameN  # exact frame index
                    rect_2.setAutoDraw(False)
            
            # *rect_3* updates
            if rect_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_3.frameNStart = frameN  # exact frame index
                rect_3.tStart = t  # local t and not account for scr refresh
                rect_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_3, 'tStartRefresh')  # time at next scr refresh
                rect_3.setAutoDraw(True)
            if rect_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_3.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_3.tStop = t  # not accounting for scr refresh
                    rect_3.frameNStop = frameN  # exact frame index
                    rect_3.setAutoDraw(False)
            
            # *rect_4* updates
            if rect_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_4.frameNStart = frameN  # exact frame index
                rect_4.tStart = t  # local t and not account for scr refresh
                rect_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_4, 'tStartRefresh')  # time at next scr refresh
                rect_4.setAutoDraw(True)
            if rect_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_4.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_4.tStop = t  # not accounting for scr refresh
                    rect_4.frameNStop = frameN  # exact frame index
                    rect_4.setAutoDraw(False)
            
            # *rect_5* updates
            if rect_5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_5.frameNStart = frameN  # exact frame index
                rect_5.tStart = t  # local t and not account for scr refresh
                rect_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_5, 'tStartRefresh')  # time at next scr refresh
                rect_5.setAutoDraw(True)
            if rect_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_5.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_5.tStop = t  # not accounting for scr refresh
                    rect_5.frameNStop = frameN  # exact frame index
                    rect_5.setAutoDraw(False)
            
            # *rect_6* updates
            if rect_6.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_6.frameNStart = frameN  # exact frame index
                rect_6.tStart = t  # local t and not account for scr refresh
                rect_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_6, 'tStartRefresh')  # time at next scr refresh
                rect_6.setAutoDraw(True)
            if rect_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_6.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_6.tStop = t  # not accounting for scr refresh
                    rect_6.frameNStop = frameN  # exact frame index
                    rect_6.setAutoDraw(False)
            
            # *rect_7* updates
            if rect_7.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_7.frameNStart = frameN  # exact frame index
                rect_7.tStart = t  # local t and not account for scr refresh
                rect_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_7, 'tStartRefresh')  # time at next scr refresh
                rect_7.setAutoDraw(True)
            if rect_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_7.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_7.tStop = t  # not accounting for scr refresh
                    rect_7.frameNStop = frameN  # exact frame index
                    rect_7.setAutoDraw(False)
            
            # *rect_8* updates
            if rect_8.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_8.frameNStart = frameN  # exact frame index
                rect_8.tStart = t  # local t and not account for scr refresh
                rect_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_8, 'tStartRefresh')  # time at next scr refresh
                rect_8.setAutoDraw(True)
            if rect_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_8.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_8.tStop = t  # not accounting for scr refresh
                    rect_8.frameNStop = frameN  # exact frame index
                    rect_8.setAutoDraw(False)
            
            # *rect_9* updates
            if rect_9.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_9.frameNStart = frameN  # exact frame index
                rect_9.tStart = t  # local t and not account for scr refresh
                rect_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_9, 'tStartRefresh')  # time at next scr refresh
                rect_9.setAutoDraw(True)
            if rect_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_9.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_9.tStop = t  # not accounting for scr refresh
                    rect_9.frameNStop = frameN  # exact frame index
                    rect_9.setAutoDraw(False)
            
            # *rect_10* updates
            if rect_10.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_10.frameNStart = frameN  # exact frame index
                rect_10.tStart = t  # local t and not account for scr refresh
                rect_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_10, 'tStartRefresh')  # time at next scr refresh
                rect_10.setAutoDraw(True)
            if rect_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_10.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_10.tStop = t  # not accounting for scr refresh
                    rect_10.frameNStop = frameN  # exact frame index
                    rect_10.setAutoDraw(False)
            
            # *rect_11* updates
            if rect_11.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_11.frameNStart = frameN  # exact frame index
                rect_11.tStart = t  # local t and not account for scr refresh
                rect_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_11, 'tStartRefresh')  # time at next scr refresh
                rect_11.setAutoDraw(True)
            if rect_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_11.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_11.tStop = t  # not accounting for scr refresh
                    rect_11.frameNStop = frameN  # exact frame index
                    rect_11.setAutoDraw(False)
            
            # *rect_12* updates
            if rect_12.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_12.frameNStart = frameN  # exact frame index
                rect_12.tStart = t  # local t and not account for scr refresh
                rect_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_12, 'tStartRefresh')  # time at next scr refresh
                rect_12.setAutoDraw(True)
            if rect_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_12.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_12.tStop = t  # not accounting for scr refresh
                    rect_12.frameNStop = frameN  # exact frame index
                    rect_12.setAutoDraw(False)
            
            # *rect_13* updates
            if rect_13.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_13.frameNStart = frameN  # exact frame index
                rect_13.tStart = t  # local t and not account for scr refresh
                rect_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_13, 'tStartRefresh')  # time at next scr refresh
                rect_13.setAutoDraw(True)
            if rect_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_13.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_13.tStop = t  # not accounting for scr refresh
                    rect_13.frameNStop = frameN  # exact frame index
                    rect_13.setAutoDraw(False)
            
            # *rect_14* updates
            if rect_14.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_14.frameNStart = frameN  # exact frame index
                rect_14.tStart = t  # local t and not account for scr refresh
                rect_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_14, 'tStartRefresh')  # time at next scr refresh
                rect_14.setAutoDraw(True)
            if rect_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_14.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_14.tStop = t  # not accounting for scr refresh
                    rect_14.frameNStop = frameN  # exact frame index
                    rect_14.setAutoDraw(False)
            
            # *rect_15* updates
            if rect_15.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_15.frameNStart = frameN  # exact frame index
                rect_15.tStart = t  # local t and not account for scr refresh
                rect_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_15, 'tStartRefresh')  # time at next scr refresh
                rect_15.setAutoDraw(True)
            if rect_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_15.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_15.tStop = t  # not accounting for scr refresh
                    rect_15.frameNStop = frameN  # exact frame index
                    rect_15.setAutoDraw(False)
            
            # *rect_16* updates
            if rect_16.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                rect_16.frameNStart = frameN  # exact frame index
                rect_16.tStart = t  # local t and not account for scr refresh
                rect_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_16, 'tStartRefresh')  # time at next scr refresh
                rect_16.setAutoDraw(True)
            if rect_16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rect_16.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    rect_16.tStop = t  # not accounting for scr refresh
                    rect_16.frameNStop = frameN  # exact frame index
                    rect_16.setAutoDraw(False)
            
            # *circle_1* updates
            if circle_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                circle_1.frameNStart = frameN  # exact frame index
                circle_1.tStart = t  # local t and not account for scr refresh
                circle_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_1, 'tStartRefresh')  # time at next scr refresh
                circle_1.setAutoDraw(True)
            if circle_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_1.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_1.tStop = t  # not accounting for scr refresh
                    circle_1.frameNStop = frameN  # exact frame index
                    circle_1.setAutoDraw(False)
            
            # *circle_2* updates
            if circle_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                circle_2.frameNStart = frameN  # exact frame index
                circle_2.tStart = t  # local t and not account for scr refresh
                circle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_2, 'tStartRefresh')  # time at next scr refresh
                circle_2.setAutoDraw(True)
            if circle_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_2.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_2.tStop = t  # not accounting for scr refresh
                    circle_2.frameNStop = frameN  # exact frame index
                    circle_2.setAutoDraw(False)
            
            # *circle_3* updates
            if circle_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                circle_3.frameNStart = frameN  # exact frame index
                circle_3.tStart = t  # local t and not account for scr refresh
                circle_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_3, 'tStartRefresh')  # time at next scr refresh
                circle_3.setAutoDraw(True)
            if circle_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_3.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_3.tStop = t  # not accounting for scr refresh
                    circle_3.frameNStop = frameN  # exact frame index
                    circle_3.setAutoDraw(False)
            
            # *circle_4* updates
            if circle_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                circle_4.frameNStart = frameN  # exact frame index
                circle_4.tStart = t  # local t and not account for scr refresh
                circle_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_4, 'tStartRefresh')  # time at next scr refresh
                circle_4.setAutoDraw(True)
            if circle_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_4.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_4.tStop = t  # not accounting for scr refresh
                    circle_4.frameNStop = frameN  # exact frame index
                    circle_4.setAutoDraw(False)
            
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
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        
        # --- Prepare to start Routine "practice_feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from practice_judge
        correct = order_mapping[show_id]==practice_answer
        if(correct):
            practice_response_tip.text = "正确"
        else:
            practice_response_tip.text = "错误"
        
        #bnu
        if correct:
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
        # Run 'End Routine' code from practice_judge
        
        practice_idx += 1
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

experiment_idx = 0
experiment_block_idx = 1
experiment_trial_idx = 1

for c in goodportary:#bnu
    try:
        c.send(mark_end)
    except:
        tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
        core.quit()
        
# CONDITIONAL FLAG
experiment_stage = "experiment_prepare"

# DATA PREPARE
import random

experiment_order_table = []        
for i in range(0,experiment_block_nums*experiment_block_trials):
    x = random.randint(0,orders_count-1)
    experiment_order_table.append(x)
    
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
# Run 'End Routine' code from init_experiment
for c in goodportary:#bnu
    try:
        c.send(mark_start)
    except:
        tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
        core.quit()
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
        
        
        # CONDITIONAL FLAG
        experiment_stage = "practice"
        experiment_answer = None
            
        # UPDATE TEXT
        group_id = experiment_order_table[(int)(experiment_idx/4)]
        show_id = show_orders[group_id][(experiment_idx+1)%4] - 1 
        
        record(experiment_block_idx,experiment_trial_idx,"TrueAnswer",order_mapping[show_id])
        
        circles = [experiment_circle1,experiment_circle2,experiment_circle3,experiment_circle4]
        rects = [experiment_rect6,experiment_rect9,experiment_rect10,experiment_rect13]
        
        for i in range(0,4):
            if i==show_id:
                circles[i].opacity = 1
                rects[i].opacity = 0
            else:
                circles[i].opacity = 0
                rects[i].opacity = 1
                
        
        
        
        experiment_response.keys = []
        experiment_response.rt = []
        _experiment_response_allKeys = []
        # keep track of which components have finished
        experiment_trialComponents = [experiment_response, experiment_cross, experiment_rect1, experiment_rect2, experiment_rect3, experiment_rect4, experiment_rect5, experiment_rect6, experiment_rect7, experiment_rect8, experiment_rect9, experiment_rect10, experiment_rect11, experiment_rect12, experiment_rect13, experiment_rect14, experiment_rect15, experiment_rect16, experiment_circle1, experiment_circle2, experiment_circle3, experiment_circle4]
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
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_4
            
            if(experiment_answer==None and experiment_response.status==STARTED and len(experiment_response.keys)>0):
                experiment_answer = experiment_response.keys[0]
                record(experiment_block_idx,experiment_trial_idx,"ReactTime",t-experiment_response.tStart)
            
            
            # bnu
            if experiment_cross.status == STARTED:
                if tThisFlipGlobal > experiment_cross.tStartRefresh + 1-frameTolerance:
                    for c in goodportary:#bnu
                        try:
                            c.send(mark_weizhi[show_id])
                        except:
                            tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
                            core.quit()
            
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
                if tThisFlipGlobal > experiment_response.tStartRefresh + 2-frameTolerance:
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
            
            # *experiment_rect1* updates
            if experiment_rect1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect1.frameNStart = frameN  # exact frame index
                experiment_rect1.tStart = t  # local t and not account for scr refresh
                experiment_rect1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect1, 'tStartRefresh')  # time at next scr refresh
                experiment_rect1.setAutoDraw(True)
            if experiment_rect1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect1.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect1.tStop = t  # not accounting for scr refresh
                    experiment_rect1.frameNStop = frameN  # exact frame index
                    experiment_rect1.setAutoDraw(False)
            
            # *experiment_rect2* updates
            if experiment_rect2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect2.frameNStart = frameN  # exact frame index
                experiment_rect2.tStart = t  # local t and not account for scr refresh
                experiment_rect2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect2, 'tStartRefresh')  # time at next scr refresh
                experiment_rect2.setAutoDraw(True)
            if experiment_rect2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect2.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect2.tStop = t  # not accounting for scr refresh
                    experiment_rect2.frameNStop = frameN  # exact frame index
                    experiment_rect2.setAutoDraw(False)
            
            # *experiment_rect3* updates
            if experiment_rect3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect3.frameNStart = frameN  # exact frame index
                experiment_rect3.tStart = t  # local t and not account for scr refresh
                experiment_rect3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect3, 'tStartRefresh')  # time at next scr refresh
                experiment_rect3.setAutoDraw(True)
            if experiment_rect3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect3.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect3.tStop = t  # not accounting for scr refresh
                    experiment_rect3.frameNStop = frameN  # exact frame index
                    experiment_rect3.setAutoDraw(False)
            
            # *experiment_rect4* updates
            if experiment_rect4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect4.frameNStart = frameN  # exact frame index
                experiment_rect4.tStart = t  # local t and not account for scr refresh
                experiment_rect4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect4, 'tStartRefresh')  # time at next scr refresh
                experiment_rect4.setAutoDraw(True)
            if experiment_rect4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect4.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect4.tStop = t  # not accounting for scr refresh
                    experiment_rect4.frameNStop = frameN  # exact frame index
                    experiment_rect4.setAutoDraw(False)
            
            # *experiment_rect5* updates
            if experiment_rect5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect5.frameNStart = frameN  # exact frame index
                experiment_rect5.tStart = t  # local t and not account for scr refresh
                experiment_rect5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect5, 'tStartRefresh')  # time at next scr refresh
                experiment_rect5.setAutoDraw(True)
            if experiment_rect5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect5.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect5.tStop = t  # not accounting for scr refresh
                    experiment_rect5.frameNStop = frameN  # exact frame index
                    experiment_rect5.setAutoDraw(False)
            
            # *experiment_rect6* updates
            if experiment_rect6.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect6.frameNStart = frameN  # exact frame index
                experiment_rect6.tStart = t  # local t and not account for scr refresh
                experiment_rect6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect6, 'tStartRefresh')  # time at next scr refresh
                experiment_rect6.setAutoDraw(True)
            if experiment_rect6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect6.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect6.tStop = t  # not accounting for scr refresh
                    experiment_rect6.frameNStop = frameN  # exact frame index
                    experiment_rect6.setAutoDraw(False)
            
            # *experiment_rect7* updates
            if experiment_rect7.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect7.frameNStart = frameN  # exact frame index
                experiment_rect7.tStart = t  # local t and not account for scr refresh
                experiment_rect7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect7, 'tStartRefresh')  # time at next scr refresh
                experiment_rect7.setAutoDraw(True)
            if experiment_rect7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect7.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect7.tStop = t  # not accounting for scr refresh
                    experiment_rect7.frameNStop = frameN  # exact frame index
                    experiment_rect7.setAutoDraw(False)
            
            # *experiment_rect8* updates
            if experiment_rect8.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect8.frameNStart = frameN  # exact frame index
                experiment_rect8.tStart = t  # local t and not account for scr refresh
                experiment_rect8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect8, 'tStartRefresh')  # time at next scr refresh
                experiment_rect8.setAutoDraw(True)
            if experiment_rect8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect8.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect8.tStop = t  # not accounting for scr refresh
                    experiment_rect8.frameNStop = frameN  # exact frame index
                    experiment_rect8.setAutoDraw(False)
            
            # *experiment_rect9* updates
            if experiment_rect9.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect9.frameNStart = frameN  # exact frame index
                experiment_rect9.tStart = t  # local t and not account for scr refresh
                experiment_rect9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect9, 'tStartRefresh')  # time at next scr refresh
                experiment_rect9.setAutoDraw(True)
            if experiment_rect9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect9.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect9.tStop = t  # not accounting for scr refresh
                    experiment_rect9.frameNStop = frameN  # exact frame index
                    experiment_rect9.setAutoDraw(False)
            
            # *experiment_rect10* updates
            if experiment_rect10.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect10.frameNStart = frameN  # exact frame index
                experiment_rect10.tStart = t  # local t and not account for scr refresh
                experiment_rect10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect10, 'tStartRefresh')  # time at next scr refresh
                experiment_rect10.setAutoDraw(True)
            if experiment_rect10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect10.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect10.tStop = t  # not accounting for scr refresh
                    experiment_rect10.frameNStop = frameN  # exact frame index
                    experiment_rect10.setAutoDraw(False)
            
            # *experiment_rect11* updates
            if experiment_rect11.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect11.frameNStart = frameN  # exact frame index
                experiment_rect11.tStart = t  # local t and not account for scr refresh
                experiment_rect11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect11, 'tStartRefresh')  # time at next scr refresh
                experiment_rect11.setAutoDraw(True)
            if experiment_rect11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect11.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect11.tStop = t  # not accounting for scr refresh
                    experiment_rect11.frameNStop = frameN  # exact frame index
                    experiment_rect11.setAutoDraw(False)
            
            # *experiment_rect12* updates
            if experiment_rect12.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect12.frameNStart = frameN  # exact frame index
                experiment_rect12.tStart = t  # local t and not account for scr refresh
                experiment_rect12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect12, 'tStartRefresh')  # time at next scr refresh
                experiment_rect12.setAutoDraw(True)
            if experiment_rect12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect12.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect12.tStop = t  # not accounting for scr refresh
                    experiment_rect12.frameNStop = frameN  # exact frame index
                    experiment_rect12.setAutoDraw(False)
            
            # *experiment_rect13* updates
            if experiment_rect13.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect13.frameNStart = frameN  # exact frame index
                experiment_rect13.tStart = t  # local t and not account for scr refresh
                experiment_rect13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect13, 'tStartRefresh')  # time at next scr refresh
                experiment_rect13.setAutoDraw(True)
            if experiment_rect13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect13.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect13.tStop = t  # not accounting for scr refresh
                    experiment_rect13.frameNStop = frameN  # exact frame index
                    experiment_rect13.setAutoDraw(False)
            
            # *experiment_rect14* updates
            if experiment_rect14.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect14.frameNStart = frameN  # exact frame index
                experiment_rect14.tStart = t  # local t and not account for scr refresh
                experiment_rect14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect14, 'tStartRefresh')  # time at next scr refresh
                experiment_rect14.setAutoDraw(True)
            if experiment_rect14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect14.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect14.tStop = t  # not accounting for scr refresh
                    experiment_rect14.frameNStop = frameN  # exact frame index
                    experiment_rect14.setAutoDraw(False)
            
            # *experiment_rect15* updates
            if experiment_rect15.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect15.frameNStart = frameN  # exact frame index
                experiment_rect15.tStart = t  # local t and not account for scr refresh
                experiment_rect15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect15, 'tStartRefresh')  # time at next scr refresh
                experiment_rect15.setAutoDraw(True)
            if experiment_rect15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect15.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect15.tStop = t  # not accounting for scr refresh
                    experiment_rect15.frameNStop = frameN  # exact frame index
                    experiment_rect15.setAutoDraw(False)
            
            # *experiment_rect16* updates
            if experiment_rect16.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_rect16.frameNStart = frameN  # exact frame index
                experiment_rect16.tStart = t  # local t and not account for scr refresh
                experiment_rect16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_rect16, 'tStartRefresh')  # time at next scr refresh
                experiment_rect16.setAutoDraw(True)
            if experiment_rect16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_rect16.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_rect16.tStop = t  # not accounting for scr refresh
                    experiment_rect16.frameNStop = frameN  # exact frame index
                    experiment_rect16.setAutoDraw(False)
            
            # *experiment_circle1* updates
            if experiment_circle1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_circle1.frameNStart = frameN  # exact frame index
                experiment_circle1.tStart = t  # local t and not account for scr refresh
                experiment_circle1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_circle1, 'tStartRefresh')  # time at next scr refresh
                experiment_circle1.setAutoDraw(True)
            if experiment_circle1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_circle1.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_circle1.tStop = t  # not accounting for scr refresh
                    experiment_circle1.frameNStop = frameN  # exact frame index
                    experiment_circle1.setAutoDraw(False)
            
            # *experiment_circle2* updates
            if experiment_circle2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_circle2.frameNStart = frameN  # exact frame index
                experiment_circle2.tStart = t  # local t and not account for scr refresh
                experiment_circle2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_circle2, 'tStartRefresh')  # time at next scr refresh
                experiment_circle2.setAutoDraw(True)
            if experiment_circle2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_circle2.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_circle2.tStop = t  # not accounting for scr refresh
                    experiment_circle2.frameNStop = frameN  # exact frame index
                    experiment_circle2.setAutoDraw(False)
            
            # *experiment_circle3* updates
            if experiment_circle3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_circle3.frameNStart = frameN  # exact frame index
                experiment_circle3.tStart = t  # local t and not account for scr refresh
                experiment_circle3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_circle3, 'tStartRefresh')  # time at next scr refresh
                experiment_circle3.setAutoDraw(True)
            if experiment_circle3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_circle3.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_circle3.tStop = t  # not accounting for scr refresh
                    experiment_circle3.frameNStop = frameN  # exact frame index
                    experiment_circle3.setAutoDraw(False)
            
            # *experiment_circle4* updates
            if experiment_circle4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                experiment_circle4.frameNStart = frameN  # exact frame index
                experiment_circle4.tStart = t  # local t and not account for scr refresh
                experiment_circle4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(experiment_circle4, 'tStartRefresh')  # time at next scr refresh
                experiment_circle4.setAutoDraw(True)
            if experiment_circle4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > experiment_circle4.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    experiment_circle4.tStop = t  # not accounting for scr refresh
                    experiment_circle4.frameNStop = frameN  # exact frame index
                    experiment_circle4.setAutoDraw(False)
            
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
        
        correct = order_mapping[show_id]==experiment_answer
        
        record(experiment_block_idx,experiment_trial_idx,"Correct",correct)
        record(experiment_block_idx,experiment_trial_idx,"Answer",experiment_answer)
        
        experiment_idx += 1
        experiment_trial_idx += 1
        
        
        #bnu
        if correct:
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
        
        
        
        
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
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
    experiment_idx = 0
    
    # the Routine "experiment_rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed experiment_block_nums repeats of 'experiment_loop'

# Run 'End Experiment' code from variable_init

for c in goodportary:#bnu
    try:
        c.send(mark_end)
    except:
        tkinter.messagebox.showinfo('错误','脑电采集设备连接断开')
        core.quit()


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
