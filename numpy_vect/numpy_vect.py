# -*- coding: utf-8 -*-
"""
	numpy_vect
	
	This project is an example of a Python project generated from cookiecutter-python.
"""

## -------- COMMAND LINE ARGUMENTS ---------------------------
## https://docs.python.org/3.7/howto/argparse.html
import argparse
CmdLineArgParser = argparse.ArgumentParser()
CmdLineArgParser.add_argument(
	"-v",
	"--verbose",
	help = "display debug messages in console",
	action = "store_true",
)
CmdLineArgs = CmdLineArgParser.parse_args()

## -------- LOGGING INITIALISATION ---------------------------
import misc
misc.MyLoggersObj.SetConsoleVerbosity(ConsoleVerbosity = {True : "DEBUG", False : "INFO"}[CmdLineArgs.verbose])
LOG, handle_retval_and_log = misc.CreateLogger(__name__)

try:
	
	## -------------------------------------------------------
	## THE MAIN PROGRAM STARTS HERE
	## -------------------------------------------------------	

	import numpy as np
	import time
	
	def get_area(a, b, c):
		
		if c == "m2":
			return a*b
		elif c == "km2":
			return a*b/(1000**2)
		else:
			raise Exception("Invalid c value = '{}'".format(c))
			
	def get_formatted_area(a, b, c):

		return "{} {}".format(get_area(a, b, c), c)	
		
	def int_to_unit(ii):
	
		if ii == 0:
			return "m2"
		elif ii == 1:
			return "km2"
		else:
			raise Exception("Invalid ii value = '{}'".format(ii))
	
	print("Numpy Vectorisation")
	print("-------------------")
	print()
	print("get_area : Compute area from two lengths (a, b) and select unit from an input string (c)")
	print("This function works as standalone (with integers and strings) and with numpy arrays when converted via numpy.vectorize")
	print()
	
	a = 250
	b = 650
	c = "m2"
	print("{}*{}; c = {}: ".format(a, b, c), get_formatted_area(a, b, c))
	print()
	
	# numpy vectorize functions
	v_get_formatted_area = np.vectorize(get_formatted_area)
	v_int_to_unit = np.vectorize(int_to_unit)
	
	# numpy array size
	ss = 1000000
	print("numpy array size: {}".format(ss))
	
	# compute results
	start_time = time.time()
	print(v_get_formatted_area(np.random.randint(0, 1000, size = ss), np.random.randint(0, 1000, size = ss), v_int_to_unit(np.random.randint(0, 2, size = ss))))
	print("Time elapsed: {:.2} seconds".format(time.time() - start_time))

## -------- SOMETHING WENT WRONG -----------------------------	
except:

	import traceback
	LOG.error("Something went wrong! Exception details:\n{}".format(traceback.format_exc()))

## -------- GIVE THE USER A CHANCE TO READ MESSAGES-----------
finally:
	
	input("Press any key to exit ...")
