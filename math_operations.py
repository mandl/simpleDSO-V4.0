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
	

		
	def operate(self, ch_data, equation = ""):
		
		transf = (self.DOTS_TO_CENTER + ch_data["y_offset"])								# Calculate the real center of the wave expressed in dots or pixels
		dotsToVolts = [  (  (x-transf)/self.DOT_PER_DIV  ) for x in ch_data["samples"]]		# Transform dots to real volts to avoid mistakes in debugging
		mathOperation = [  eval(  equation  ) for x in dotsToVolts]							# Operate mathematically on each element
		voltsToDots = [  int(x * self.DOT_PER_DIV +  transf) for x in mathOperation]		# Antitransform: Volts to dots or pixels
		
		return voltsToDots
					
	def seno(self,x):
		return math.sin(x)
		
