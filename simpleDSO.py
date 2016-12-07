#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############################################################################
#
#	QT4 application for DSO UNI-T 2XXX/3XXX
#	It allows get screenshot of screen
#
#	Ing. Tomas Kosan, 2008-2010
#
#############################################################################

#############################################################################
#
#	QT4 application for DSO UNI-T 2XXX/3XXX
#	It allows get screenshot of screen
#
#	Ing. Tomas Kosan, 2008-2010
#
#############################################################################
#
#
#  COMO COORRER:  sudo python simpleDSO.py  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11 
#  
#  Si no se pone SUDO da err
#############################################################################
# To install "usb" module:
# ------------------------
#
# Download "pyusb1.0.0.zip" zip file from:        https://sourceforge.net/projects/pyusb/?source=typ_redirect
# From readMe file:   
# sudo apt-get install python libusb-1.0-0   and then...
# sudo python setup.py install  (In same folder where you extracted zip file)
############################################################################# 

#############################################################################
# To convert .UI file to .PY file:
# -------------------------------
#
# Install: sudo apt install pyqt4-dev-tools
#
# Then:  pyuic4 -x MyIU.ui -o MyPY.py
#
#############################################################################

#############################################################################
# most widgets do not normally emit a signal when they are resized. In order
# to do this, you would need to re-implement the QGraphicsView class and its 
# resizeEvent method, modifying it to emit such a signal
#
# Use "Promote to..." in QtDesigner
#
# See links:
# http://stackoverflow.com/questions/5467149/pyqt-graphicsview-resize-event
# http://stackoverflow.com/questions/19622014/how-to-use-promote-to-in-qt-designer-in-pyqt4
# http://stackoverflow.com/questions/8955780/qwidget-resize-signal/36630691#36630691
#
# SOLVED: When mainWindow is resized, then mainWindow and Qwidget sizes are printed:
# Go into: class DSO_main(QtGui.QMainWindow, simpleUI.Ui_MainWindow):

#	def resizeEvent(self,resizeEvent):	# Si se agranda el main Window, entonces se dispara el evento
#		print"hola"
#		print self.gwScreen.size()      # Obtengo las medidas del QWidget donde se dibuja la grilla
#		print self.normalGeometry()		# Obtengo las medidas y posición del MainWindow
#		print self.gwScreen.width() 	# Obtengo las medidas como int
#		print self.gwScreen.height() 	# Obtengo las medidas como int
#
#############################################################################




import sys, time, threading, Queue, types,  csv
import os.path
from PyQt4 import QtCore, QtGui, Qt

# import converted ui file
from UI import simpleUI	

# import UNI-T class
from ut2XXX import UT2XXX, utils
# import data packet definitions
#from ut2XXX_definitions import *
# import graphic classes and utils
import graphic
import math_operations
import copy				# Used for deep object copy

version = "simpleDSO 0.3"

# from main to thread
Que_main2thread = Queue.Queue()
# thread to main
Que_thread2main = Queue.Queue()

# thread of DSO class
#def DSO_thread(equationF1):
def DSO_thread():
	
	try:
		want_run = True
		offline = False
		
		# basic init of DSO comunication
		dso = UT2XXX.UNI_T_DSO()
				
		# MAXI: Math basic init for wave mathematical operations
		dsoMath = math_operations.Math()
		
		# test if device is connected
		if not dso.is_present:
			Que_thread2main.put("ERR_NOT_FOUND")
			offline = True
			want_run = False
			return

		msg = ""
		
		loop = 0
		
		while want_run:
			loop += 1
			try:
				msg = Que_main2thread.get_nowait()				
				eqF1 = Que_main2thread.get_nowait()				# Store F1 wave transformation function
			
				
			except:
				pass
			else:
				print "Dbg:Processing",msg
				# parse commands
				if msg == "END_NOW":
					want_run = False
					
				elif msg == "REMOTE_ON" and not offline:	
					dso.enter_far_mode()
					
				elif msg == "REMOTE_OFF" and not offline:	
					dso.leave_far_mode()
						
				elif msg == "GET_WAVE" and not offline:
					#print "Msg from main: get wave"
					dso.get_waveform()
					
					# *********************************************
					# MAXI
					
					#F1_data = dso.ch2_data												# Not a good idea. Use deepcopy
					F1_data = copy.deepcopy(dso.ch2_data)								# Deep object copy. Using ch2_data as template
					
					if (eqF1 == "x" ):													# If not transformation (x = x):
						F1_data["samples"] = dsoMath.operate( F1_data, "x - x + 1")		# To show in screen a little up from ch2_data
					else:
						F1_data["samples"] = dsoMath.operate( F1_data, eqF1 )			# Make the transformation
				
					# *********************************************
					
					Que_thread2main.put("DATA")
					
					Que_thread2main.put(dso.ch1_data)
					
					
					print dso.ch1_data                     #MAXI: AQUI PUEDE VERSE TODO EL DICCIONARIO CON LOS DATOS
					print " ---------------------------------------------------------------------------------"
					print dso.ch2_data
					print " ---------------------------------------------------------------------------------"
					#print F1_data
					
					Que_thread2main.put(dso.ch2_data)
					Que_thread2main.put(F1_data)  #MAXI
					
					Que_thread2main.put(dso.data_raw)
					#print "Data send."
				elif msg == "SAVE_SCREENSHOT" and not offline:
					Que_thread2main.put("PIXDATA")
					Que_thread2main.put(dso.get_screenshot())
						
				elif msg == "LOAD_WAVE":
					m =  Que_main2thread.get_nowait()
					#print m
					dso.parse_waveform(m)
					Que_thread2main.put("DATA")
					Que_thread2main.put(dso.ch1_data)	
					Que_thread2main.put(dso.ch2_data)
				
				elif msg == "RECONNECT":
					dso.init()
					if not dso.is_present:
						Que_thread2main.put("ERR_NOT_FOUND")
						offline = True
					else:
						offline = False
					
				# if it is integer, we have direct message	
				elif type(msg) == type(1) and not offline:
					dso.send_message(msg)
				else:
					msg = ""
#			if loop > 500:
#				loop = 0
#				dso.leave_far_mode()	
			time.sleep(0.001)	

	except Exception, (s):
		#print s
		Que_thread2main.put("EXCEPTION")
		Que_thread2main.put(s)
	print "Wrn: Thread end."
	try:
		dso.close()
	except:
		pass

# main class - GUI
class DSO_main(QtGui.QMainWindow, simpleUI.Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		
		
		
		print "Inf: DSO remote app is starting ..."
		self.setupUi(self)
		print "Inf: DSO remote app started."
		
		self.F1 = "x" 							#Default definition of F1 wave transformation function
		
		print "LA ECUACION en DSO_Main:"
		print self.F1
		
		self.dso_thread = threading.Thread(target=DSO_thread) 
		self.dso_thread.start()
				
		self.scene = graphic.DSO_Scene()
		
		self.gwScreen.setScene(self.scene)
		self.gwScreen.update()
		
		# autoupdate timer
		self.auto_timer = QtCore.QTimer()
		
		#self.auto_timer.start(1000)
		self.connect(self.auto_timer, QtCore.SIGNAL("timeout()"), self.updateScreen)
		
		# timer for checking msg queue
		self.timer = QtCore.QTimer()
		self.timer.start(10)
		self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateState)
		
		# Events
		self.pushButton_5.clicked.connect(self.updateEq) #MAXI
		
		self.updateScreen()
		
		self.loadScreenFromDso()

		self.setWindowTitle(QtGui.QApplication.translate("MainWindow", version, None, QtGui.QApplication.UnicodeUTF8))


	def updateEq(self):
		print self.F1 
		#self.F1 = "sqrt(x)"
		self.F1 = "int(x)"
		
		
	def reconnect(self):
		#if self.dso_thread.isAlive():
			#print "Thread allready started", self.dso_thread
		#else:
			#del self.dso_thread
			#self.dso_thread = threading.Thread(target=DSO_thread)
			#self.dso_thread.start()
		Que_main2thread.put("RECONNECT")
		
	#	
	def setTimer(self, force_stop = False):
		if not force_stop and self.auto_timer.isActive():
			self.auto_timer.stop()
		else:
			self.auto_timer.start()
			

	def updateScreen(self):
		if Que_main2thread.empty():
			Que_main2thread.put("GET_WAVE")
			Que_main2thread.put(self.F1)	#MAXI
		
	def saveScreenshot2png(self, data):
		
		screen = QtGui.QPixmap()
		screen.loadFromData(data)
		
		screen = screen.scaledToWidth(640)
		
		self.scene.showPixmap(screen)
		
#		filename = QtGui.QFileDialog.getSaveFileName(self, u"Enter name and path to file", u"./", u"Images (*.png)", u"???")
#		if filename:
#			print screen.save(filename)
				

	def loadLWave(self):
		filename = QtGui.QFileDialog.getSaveFileName(self, u"Enter name and path to file", u"./", u"Data (*.dat)", u"???")
		if filename:
			#self.loaded_data = open(filename)
			self.setTimer(True)
			Que_main2thread.put("LOAD_WAVE")
			Que_main2thread.put(filename)

	def updateState(self):
		#print "Timer start"
		try:
			msg = Que_thread2main.get_nowait()
		except Exception:
			pass
		else:
#			print "Msg from thread:",msg
			if msg == "DATA":
				self.ch1_data = Que_thread2main.get()
				self.ch2_data = Que_thread2main.get()
				self.F1_data  = Que_thread2main.get()
				self.data_raw = Que_thread2main.get()
				
				#self.scene.updateScreen(self.ch1_data, self.ch2_data )
				self.scene.updateScreen(self.ch1_data, self.ch2_data,  self.F1_data  ) # MAXI: Added a F1 function
				
			
			if msg == "ERR_NOT_FOUND":
				QtGui.QMessageBox.critical(self, u"Error", u"UNI-T DSO  not found. This error is cricital.\nTurn on DSO and connect it with PC by USB cable. Then run program again.")
				self.close()
				
			if msg == "PIXDATA":
				print "Inf: Recieve pixmap data."
				self.saveScreenshot2png(Que_thread2main.get())
				
			if msg == "EXCEPTION":
				self.setTimer(True)
				excep = Que_thread2main.get()
				print "Err: Exception in thread:",excep
				try:
					QtGui.QMessageBox.critical(self, u"Exception", u"Communication error ocured:\n"+str(excep))
				except:
					QtGui.QMessageBox.critical(self, u"Exception", u"Comunication error ocured.")

				
	
	
	def closeEvent(self, closeEvent):
		print "Inf: Closing"
		Que_main2thread.put("END_NOW")
		time.sleep(0.2)
		closeEvent.accept()

	def loadDataFromDso(self, force=True):
		if force:
			self.updateScreen()
		
	def processAction(self, action):
		if action.text() == "About":
			QtGui.QMessageBox.about(self,"Program "+version, "<b>Ing. Tomas Kosan, 2010</b> \
			<br><br>This program allows taking data from UNI-T DSOs<br>and save them to harddisk as an image or a CSV file.<br> \
			It also can take real screenshot of screen  of DSO.")
		if action.text() == "Exit":
			self.close()


	def loadScreenFromDso(self):
		Que_main2thread.put("SAVE_SCREENSHOT")
    
	def saveProgramScreen(self):
		self.image = QtGui.QPixmap(640,480)
		self.image.fill(QtCore.Qt.black)
		screenshot = QtGui.QPainter(self.image)
		self.gwScreen.render(screenshot)#, self.gwScreen.rect())
		filename = QtGui.QFileDialog.getSaveFileName(self, u"Enter name and path to file", u"./", u"Png (*.png)", u"screenshot.png")
		if filename:
			self.image.save(filename,"PNG")
    
	def setAutoUpdate(self, state):
		if state:
			self.auto_timer.start(self.updateValue.value())
		else:
			self.auto_timer.stop()

	def saveDataToCSV(self):
		self.loadDataFromDso()
		filename = QtGui.QFileDialog.getSaveFileName(self, u"Enter name and path to file", u"./", u"CSV (*.csv)", u"???")
		if filename:
			print "Inf: raw data from DSO:\n", self.data_raw
			print "Inf: Saving to", filename
			writer = csv.writer(open(filename, "wb"), delimiter=';')
			writer.writerow(self.ch1_data["samples"])
			writer.writerow(self.ch2_data["samples"])

			writer = csv.writer(open(filename.replace(".csv", "_raw.csv"), "wb"), delimiter=';')
			writer.writerow(self.data_raw)

def main(args):
	app=QtGui.QApplication(args)
	#app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app.quit)
	app.setStyle("plastique")
	mainWindow = DSO_main()
	mainWindow.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main(sys.argv)
