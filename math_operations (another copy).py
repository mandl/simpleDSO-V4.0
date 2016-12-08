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
		
		

		
	def operate(self, ch_data, ch1_data, ch2_data equation = ""):
		""" This function perform all mathematical operations introduced
		by the user. Integration and derivation need some code here"""
		
		#self.ch1_data = ch1_data
		#self.ch2_data = ch2_data
		
		# Used for integration
		if self.WORD_INT in equation:
			self.accum = 0																	# accumulate sum of integration
			self.delta_t = (ch_data ["s_div"] * self.X_DIV )  /  len(ch_data["samples"])
			equation = equation.replace(self.WORD_INT , "self.integrate")
		
		# If ch1 is used in equation
		#if ("Ch1") in equation:	
		#	equation = equation.replace("Ch1" , "self.ch1(i)")
		#else if ("CH1")	
		#	equation = equation.replace("CH1" , "self.ch1(i)")
		#else if ("cH1")	
		#	equation = equation.replace("cH1" , "self.ch1(i)")
		
			

		#equation = "sqrt(x)"
		# Start of performing mathematical operations 
		transf = (self.DOTS_TO_CENTER + ch_data["y_offset"])								# Calculate the real center of the wave expressed in dots or pixels
		dotsToVolts = [  (  (x-transf)/self.DOT_PER_DIV  ) for x in ch_data["samples"]]		# Transform dots to real volts to avoid mistakes in debugging
		mathOperation = [  eval(  equation  ) for x in dotsToVolts]							# Operate mathematically on each element
		voltsToDots = [  int(x * self.DOT_PER_DIV +  transf) for x in mathOperation]		# Antitransform: Volts to dots or pixels
		print "dotsToVolts:"
		print  mathOperation
		print ""
		print "VIOLETA:"
		print  voltsToDots
		return voltsToDots
		self.accum = 0	
		
		
	def integrate(self, x ):
		self.accum = self.accum + (x*self.delta_t*1000)
		return self.accum 
		
	#def ch1(self,i):
		
		
		
		
	
		


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


