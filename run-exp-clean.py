#!/usr/bin/env python
"""
WHACK-A-MOLE Paradigm
Initial Version: April 24, 2015, Kathryn Schuler
Updated Version: May 5, 2016, Kathryn Schuler
------------------------
"""
#from psychopy import visual, core, info, event, data
#import datetime, os, sys, itertools
"""
*********************************************************************************
SETUP EXPERIMENT PARAMTERS
*********************************************************************************
"""
EXP_INFO = {
	'exp-id': 0000,											# experiment ID number (fixed value)
	'subject': raw_input("enter subject no: "), 			# subject ID (requests user input)
	'condition': raw_input("enter condition (A or B):")   	# condition (requests user input)
}
MONITOR = {
	'size': [1440, 900],		# pixel dimensions of the monitor
	'screen': 0,				# if more than 1 screen, which one to display on?
	'bg-color': 'white',		# what should the background color be?
	}
MOUSE = {
	'mouse-visible': True		# should the mouse be visible? (boolean)
}
KEYBOARD = {
	'quit':['escape'],			# keys that quit the experiment
	'next':['space']			# keys that advance
}
TEXT = {
	'pos': [0,300],				# [x,y] position of the instructions
	'height': 20,				# how big is the font?
	'wrap' : 800,				# how many pixels before words wrap to next line?
	'color': 'gray',			# what color is the text?
	'font': 'Arial'				# what font is the text?
	}
PROG_BAR = {
	'pos': [0, 350],			# [x,y] position of the progress bar
	'height':20,				# height of progress bar
	'width':680,				# width of progress bar
	'color-outline': 'gray',	# outline color of progress bar
	'color-fill':'black',		# fill color of progress bar
	'fill-opacity':0.8,			# opacity of fill in progress bar
	'level-pos':[400, 350]		# [x,y] position of level information by progress bar
	}
BOXES = {
	'color-line': 'gray',		# box line color
	'box-size':[101, 101],		# [w,h] size of boxes
	'pos': [					# a list of the exact [x,y] positions of each box;
	(-225, -75),					# the legnth of this list tells program
	(75, 75),						# how many boxes you have
	(-225, 75),
	(-75, 75),
	(-75, -75),
	(375, 75),
	(225, 75),
	(-375, -75),
	(225, -75),
	(375, -75),
	(75, -75),
	(-375, 75)
	]
}
RATING_SCALE = {
	'pos': [0, -250],			# [x,y] position of rating scale
	'pos-happy': [175, -250],	# [x,y] position of happy face
	'pos-sad': [-175, -250]		# [x,y] position of sad face
	}
"""
*********************************************************************************
SETUP ONSCREEN INSTRUCTIONS
*********************************************************************************
"""
#These appear before for the exposure phase
EXPOSE_INSTRUCT = '''
Exposure.
'''
#These appear when the subjects finished a block
BLOCK_FEEDBACK = '''
Great Job! You may now take a break.  Press space bar when you are ready to continue.
'''
#These appear before the rating phase
RATING_INSTRUCT = '''
Rating
'''
#These appear during every rating trial
RATING_TRIAL_INSTRUCT = '''
How often did the mole move in this order?
'''
#These appear at the end of the experiment.
END_INSTRUCT = '''
Thanks for playing! The experiment is over.
'''
"""
*********************************************************************************
 The main experiment class, which contains all the experiments objects and methods.
*********************************************************************************
"""

print "Hello, conda is working for now."


#
# class WhackAMoleExperiment(object):
# 	def __init__(self):
# 		self.expClock = core.Clock()
# 		self.today = datetime.datetime.now()
# 		self.win = visual.Window(units='pix',
# 			winType = 'pyglet', screen = MONITOR['screen'], color = MONITOR['bg-color'],
# 			size = MONITOR['size'],  fullscr = True, allowGUI = True
# 		)
# 		self.mouse = event.Mouse(win = self.win,
# 			visible = True
# 		)
# 		self.instructions = visual.TextStim(self.win,
# 			text = '', pos = TEXT['pos'], color = TEXT['color'], height = TEXT['height'],
# 			font = TEXT['font'], wrapWidth = TEXT['wrap']
# 		)
# 		self.accuracy = visual.TextStim(self.win,
# 			text = '', pos= (0, 300), color = 'black', height = 25, font = 'Arial', wrapWidth = 800
# 		)
# 		self.speed = visual.TextStim(self.win,
# 			text = '', pos = (0, 200), color = 'black', height = 25, font = 'Arial', wrapWidth = 800
# 		)
# 		self.level = visual.TextStim(self.win,
# 			text = '', pos = PROG_BAR['level-pos'], color = TEXT['color'], height = TEXT['height'],
# 			font = TEXT['font'], wrapWidth = TEXT['wrap']
# 		)
# 		self.progressOutline = visual.Rect(self.win,
# 			units = 'pix', pos = PROG_BAR['pos'], width = PROG_BAR['width'], height = PROG_BAR['height']+3,
# 			lineColor = PROG_BAR['color-outline']
# 		)
# 		self.progressBar = visual.Rect(self.win,
# 			units = 'pix', pos = PROG_BAR['pos'], width = PROG_BAR['width'], height = PROG_BAR['height'],
# 			fillColor = PROG_BAR['color-fill'], opacity = PROG_BAR['fill-opacity']
# 		)
# 		self.ratingScale = visual.RatingScale(self.win,
# 			pos = RATING_SCALE['pos'],  low=1, high=5, precision = 1, textColor = TEXT['color'],
# 			marker = 'triangle', size = 0.60, stretch = 1.0, lineColor = TEXT['color'],
# 			markerColor = 'blue', scale = None
# 			)
# 		self.happyFace = visual.ImageStim(self.win,
# 			image = 'images/green-happy-face.png', pos = RATING_SCALE['pos-happy']
# 		)
# 		self.sadFace = visual.ImageStim(self.win,
# 			image = 'images/red-sad-face.png', pos = RATING_SCALE['pos-sad']
# 		)
# 		self.mole = visual.ImageStim(self.win,
# 			units = 'pix', size = (100,100), pos = (0,0),
# 			image = 'images/mole.png'
# 		)
#
# 	def runExperiment(self):
# 		self.setupExperiment()
# 		self.exposure()
# 		#self.ratingTest()
# 		#self.displayInstructions(END_INSTRUCT)
#
# 	def setupExperiment(self):
# 		self.win.setMouseVisible(WINDOW['mouse-visible'])
# 		self.infoData = [EXP_INFO['exp-id'], self.today, EXP_INFO['subject'], EXP_INFO['condition']]
# 		self.initializeBoxes()
#
# 	def exposure(self):
# 		EXP_INFO['expPhase'] = 'exposure'
# 		self.loadTrials('conditions/'+EXP_INFO['condition']+'-exposure.xlsx', EXPOSURE['order'], EXPOSURE['reps'])
# 		self.displayInstructions(EXPOSE_INSTRUCT)
# 		whichLevel = 1
# 		for trial in self.trials:
# 			whichSeq = trial.seqnum
# 			for s in trial.thisseq:
# 				corrBox, corrPos = (self.boxes[s], BOXES['pos'][s])
# 				self.changeProgressBar(self.trials.thisN, self.trials.nTotal)
# 				self.moveMole(corrPos)
# 				self.generateDisplay(str(whichLevel)+' of 18')
# 				self.collectResponses(corrBox, whichSeq, whichLevel)
# 			if self.trials.thisN in BREAK_AFTER:
# 				self.displayInstructions(BLOCK_FEEDBACK)
# 				whichLevel += 1
#
# 	def initializeBoxes(self):
# 		self.boxes = []
# 		for pos in range(len(BOXES['pos'])):
# 			box = visual.Rect(self.win, units = 'pix', height = BOXES['box-size'][0], width = BOXES['box-size'][1], pos = BOXES['pos'][pos], lineColor = BOXES['color-line'])
# 			self.boxes.append(box)
#
# 	def loadTrials(self, thisFile, thisMethod = 'random', numReps=1):
# 		self.conditionsFile = data.importConditions(thisFile)
# 		self.trials = data.TrialHandler(self.conditionsFile,
# 			method = thisMethod, nReps = numReps, extraInfo = EXP_INFO)
#
# 	def changeProgressBar(self, thisTrial, numTrials):
# 		pixels_per_trial = PROG_BAR['width']/(numTrials)
# 		pixels_this_trial = (thisTrial+1)*pixels_per_trial
# 		width = PROG_BAR['width'] - pixels_this_trial
# 		newxpos = ((-PROG_BAR['width']/2) + (PROG_BAR['width']/2 - pixels_this_trial))/2
# 		self.progressBar.setWidth(width)
# 		self.progressBar.setPos([newxpos, PROG_BAR['pos'][1]])
#
# 	def generateDisplay(self, whichLevel):
# 		self.drawBoxes()
# 		self.mole.draw()
# 		self.drawProgressBar(whichLevel)
# 		self.win.flip()
#
# 	def displayInstructions(self, whichText = '', isTrial = False):
# 		self.instructions.setText(whichText)
# 		self.instructions.draw()
# 		self.drawBoxes(False)
# 		if isTrial == False:
# 			self.win.flip()
# 			event.waitKeys(keyList=KEYS_NEXT)
# 		else: pass
#
# 	def moveMole(self, molePos):
# 		"""set the position of the mole to molePos argument"""
# 		self.mole.setPos(molePos)
#
# 	def collectResponses(self, correctBox, whichSeq, whichLevel):
# 		attemptno, iscorrect = self.resetRT()
# 		while iscorrect == False:
# 			pressed, RT = self.mouse.getPressed(getTime = True)
# 			mousePos = self.mouse.getPos()
# 			if pressed[0] and RT[0]:
# 				attemptno += 1
# 				iscorrect = self.checkCorrect(correctBox, mousePos)
# 				self.writeData([whichLevel, whichSeq, attemptno, iscorrect, RT[0]], ',')
# 				print 'writing to data...', attemptno, iscorrect, RT[0]
# 				pressed[0], RT[0] = (0.0, 0.0)
# 			if event.getKeys(['escape']): core.quit()
#
# 	def resetRT(self):
# 		self.expClock.reset()
# 		self.mouse.clickReset()
# 		attemptno, iscorrect = (0, False)
# 		return attemptno, iscorrect
#
# 	def checkCorrect(self, correctBox, mousePos):
# 		if correctBox.contains(mousePos): iscorrect = True
# 		else: iscorrect = False
# 		return iscorrect
#
# 	def writeData(self, dataList, seperate = '', newLine = True):
# 		"""writes a data file."""
# 		self.dataFile = open('data/'+EXP_INFO['subject']+'-'+self.today.strftime('%Y-%m-%d-%H%M%S')+'.csv', 'a')
# 		if newLine == True:
# 			self.dataFile.write('\n')
# 		for item in itertools.chain(self.infoData, dataList):
# 			self.dataFile.write(str(item)+ seperate)
# 		self.dataFile.close()
#
# 	def drawBoxes(self, isTrue = True):
# 		for box in self.boxes:
# 			box.setAutoDraw(isTrue)
#
# 	def drawProgressBar(self, whichLevel = '0'):
# 		self.progressOutline.draw()
# 		self.progressBar.draw()
# 		self.level.setText(whichLevel)
# 		self.level.draw()
#
# 	def distance(self):
# 		#tell how far mole moved from last time
# 		dist = math.hypot(x2 - x1, y2 - y1)
#
# 	def displayFeedback(self, correctTrials, trialNumber, elapsedTime):
# 		"""displays feedback about number of correct trials (accuracy) and how long the block took."""
# 		if correctTrials/trialNumber > 0.8: improveText = 'go faster!'
# 		else : improveText = 'be more accurate!'
# 		self.accuracy.setText('You caught the Mole  '+str(round(correctTrials/trialNumber,2)*100)+'  % of the time')
# 		self.speed.setText('in  '+str(round(elapsedTime, 2))+'  seconds.  Try to '+improveText)
# 		self.accuracy.draw()
# 		self.speed.draw()
# 		self.win.flip()
# 		core.wait(5)
#
# 	def countCorrectTrials(self, attemptno, iscorrect, correctTrials):
# 		"""counter for the number of correct trials"""
# 		if attemptno == 1 and iscorrect == 1:
# 			correctTrials += 1
# 		return correctTrials
#
# # Request user input with dialog box
# if not gui.DlgFromDict(EXP_INFO, order=['subject', 'condition']).OK:
# 		core.quit()
#
#
# exp = WhackAMoleExperiment()
# exp.runExperiment()
