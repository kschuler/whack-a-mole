#!/usr/bin/env python
"""
WHACK-A-MOLE Paradigm
Initial Version: April 24, 2015, Kathryn Schuler
Updated Version: May 5, 2016, Kathryn Schuler
------------------------
"""
from psychopy import visual, core, event #, info, data
#import datetime, os, sys, itertools

class WhackAMoleExperiment(object):
	def __init__(self):
		self.expInfo = {
			'exp-id': 0000,											# experiment ID number (fixed value)
			'subject': raw_input("enter subject no: "), 			# subject ID (requests user input)
			'condition': raw_input("enter condition (A or B): ")   	# condition (requests user input)
		}
		self.expWindow = visual.Window(
			units = 'pix',
		 	winType = 'pyglet',
			screen = 0,
			color = 'white',
		 	size = [1440, 900],
			fullscr = True,
			allowGUI = False
		)
		self.expMouse = event.Mouse(
		 	win = self.expWindow,
		 	visible = False
		)
		self.expText = visual.TextStim(
			win = self.expWindow,
			pos = [0, 300],
			color = 'gray',
			height = 20,
			font = 'Helvetica',
			wrapWidth = 800
		)
		self.progBarOutline = visual.Rect(
			win = self.expWindow,
			pos = [0, 350],
			width = 680,
			height = 23,
			lineColor =  'gray'
		)
		self.progBar = visual.Rect(
			win = self.expWindow,
			pos = [0, 350],
			width = 680,
			height = 20,
			fillColor = 'black',
			opacity = 0.8
		)
		self.progBarLevel = visual.TextStim(
			win = self.expWindow,
			text = 'level 1',
			pos = [400, 350],
			color = 'gray',
			height = 20,
			font = 'Helvetica'
		)
		self.ratingScale = visual.RatingScale(
			win = self.expWindow,
			pos = [0, -300],
			low = 1,
			high = 5,
			precision = 1,
			textColor = 'gray',
			marker = 'triangle',
			size = 0.60,
			stretch = 1.0,
			lineColor = 'gray',
			markerColor = 'blue',
			scale = None
		)
		self.mole = visual.ImageStim(
			win = self.expWindow,
			units = 'pix',
			size = (100,100),
			pos = (0,0),
			image = 'images/mole.png'
		)
	def generateDisplay(self):
		self.progBarOutline.draw()
		self.progBarLevel.draw()
		self.progBar.draw()
		self.expText.draw()
		self.ratingScale.draw()
		self.mole.draw()
		self.expWindow.flip()
		core.wait(5)

exp = WhackAMoleExperiment()
exp.generateDisplay()


# """
# *********************************************************************************
# MAIN EXPERIMENT FUNCTIONS
# *********************************************************************************
# """
# def runExperiment():
# 	setupExperiment()
#
# def setupExperiment():
#
#

# class WhackAMoleExperiment(object):
# 	def __init__(self):
# 		self.expClock = core.Clock()
# 		self.today = datetime.datetime.now()

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
