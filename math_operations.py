#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#
import math

class Math:

	# init
	def __init__(self):
		
		""" Init of basic data. Chanel data is not expressed as volts, it seems to be 
		expressed as pixels dots (Useful way to make easy to draw wave). In Y direction,
		zero (Dot) is at bottom (Not at middle of screen as indicated by common sense)"""
		
		self.DOT_PER_DIV = 25.0			# pixels or dots per scope division 
		self.DOTS_TO_CENTER = 128		# Dot o pixel quantity until center line in vertical direction (Y), in other words, from bottom to center
		self.X_DIV = 10					# Number of screen divisions in X
		self.Y_DIV = 8		 			# Number of screen divisions in Y
		
		self.WORD_INT = "int"
		
		

		
	def operate(self, ch_data, ch1_data, ch2_data, equation = ""):
		""" This function perform all mathematical operations introduced
		by the user. Integration and derivation need some code here"""
		
		self.ch1_data = ch1_data
		self.ch2_data = ch2_data
		
		# Used for integration
		if self.WORD_INT in equation:
			self.accum = 0																	# accumulate sum of integration
			self.delta_t = (ch_data ["s_div"] * self.X_DIV )  /  len(ch_data["samples"])
			equation = equation.replace(self.WORD_INT , "self.integrate")
		
		#If ch1 is used in equation. Allow different ways of writing 
		if ("ch1") in equation:	
			equation = equation.replace("ch1" , "self.ch1(idx)")
		elif ("Ch1") in equation:	
			equation = equation.replace("Ch1" , "self.ch1(idx)")
		elif ("CH1") in equation:	
			equation = equation.replace("CH1" , "self.ch1(idx)")
		elif ("cH1") in equation:	
			equation = equation.replace("cH1" , "self.ch1(idx)")
	
		#If ch2 is used in equation. Allow different ways of writing
		if ("ch2") in equation:	
			equation = equation.replace("ch2" , "self.ch2(idx)")
		elif ("Ch2") in equation:	
			equation = equation.replace("Ch2" , "self.ch2(idx)")
		elif ("CH2") in equation:	
			equation = equation.replace("CH2" , "self.ch2(idx)")
		elif ("cH2") in equation:
			equation = equation.replace("cH2" , "self.ch2(idx)")		

		#equation = "sqrt(x)"
		# Start of performing mathematical operations 
		transf = (self.DOTS_TO_CENTER + ch_data["y_offset"])								# Calculate the real center of the wave expressed in dots or pixels
		
		dotsToVolts = [  (  (x-transf)/self.DOT_PER_DIV  ) for x in ch_data["samples"]]		# Transform dots to real volts to avoid mistakes in debugging
		
		#mathOperation = [  eval(  equation  ) for x in dotsToVolts]							# Operate mathematically on each element
		mathOperation = [  eval(  equation  ) for idx, x in enumerate(dotsToVolts)]			# Adding "enumerate" allow us to access to index number "idx"
		#mathOperation = [  eval("self.ch1(idx)") for idx, x in dotsToVolts]
		
		voltsToDots = [  int(x * self.DOT_PER_DIV +  transf) for x in mathOperation]		# Antitransform: Volts to dots or pixels
		
		return voltsToDots
	
		
		
	def integrate(self, x ):
		self.accum = self.accum + (x*self.delta_t*1000) # ATENCIOONNN!!!! HAY QUE SACAR EL 1000
		
		return self.accum 
		
		
	def ch1(self,idx):	
		""" Transforms from dot to volts and returns the ch1 value solicitated by the index"""
		
		transf = (self.DOTS_TO_CENTER + self.ch1_data["y_offset"])								# Calculate the real center of the wave expressed in dots or pixels
		dotsToVolts = [  (  (x-transf)/self.DOT_PER_DIV  ) for x in self.ch1_data["samples"]]		# Transform dots to real volts to avoid mistakes in debugging
		
		return dotsToVolts[idx]
	
	
	def ch2(self,idx):	
		""" Transforms from dot to volts and returns the ch2 value solicitated by the index"""
		
		transf = (self.DOTS_TO_CENTER + self.ch2_data["y_offset"])								# Calculate the real center of the wave expressed in dots or pixels
		dotsToVolts = [  (  (x-transf)/self.DOT_PER_DIV  ) for x in self.ch2_data["samples"]]		# Transform dots to real volts to avoid mistakes in debugging
		
		return dotsToVolts[idx]
		
		
		
		
	
		


# Add any mathematical function:					

def sin(x):
	return math.sin(x)

def cos(x):
	return math.cos(x)

def tan(x):
	return math.tan(x)
		
def sqrt(x):
	return math.sqrt(x)

def abs(x):						# Absolut number
	return math.fabs(x)

def exp(x):						
	return math.exp(x)

def pow(x,y):
	return math.pow(x, y)


