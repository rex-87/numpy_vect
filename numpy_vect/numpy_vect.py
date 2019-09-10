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

	import pandas as pd
	import numpy as np
	import time
	import random
	
	def get_area(a, b, c):
		
		if c == "m2":
			return a*b
		elif c == "km2":
			return a*b/(1000**2)
		else:
			raise Exception("Invalid c value = '{}'".format(c))
		
	def get_area_np_where(a, b, c):
		return np.where(c == "m2", a*b, a*b/(1000**2))
	
	def get_formatted_area(a, b, c):
		return "{} {}".format(get_area(a, b, c), c)	
	
	def get_area_m2(a, b):
		return a*b

	def get_area_km2(a, b):
		return a*b/(1000**2)
		
	def get_formatted_area_m2(a, b):
		return "{} m2".format(get_area_m2(a, b))
	
	def get_formatted_area_km2(a, b):
		return "{} km2".format(get_area_km2(a, b))
		
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
	print()
	
	# numpy array size
	ss = 5000000
	print("array size: {}".format(ss))
	print()
	
	# list of parameters
	a_list = [1000*random.random() for i in range(ss)]
	b_list = [1000*random.random() for i in range(ss)]
	c_list = [int_to_unit(int(2*random.random())) for i in range(ss)]
	
	# numpy vectorize functions
	v_get_area = np.vectorize(get_area)
	
	# list to numpy array
	a_npa = np.array(a_list)
	b_npa = np.array(b_list)
	c_npa = np.array(c_list)
	
	# lists to pandas dataframe
	abc_df = pd.DataFrame.from_dict({'a':a_list, 'b':b_list, 'c':c_list})
	
	print("pandas (scalar/array function)")
	print("------------------------------")
	start_time = time.time()
	abc_df['rr'] = get_area_np_where(abc_df['a'], abc_df['b'], abc_df['c'])
	print("Time elapsed: {:.3f} seconds".format(time.time() - start_time))
	print()
	
	print("pandas (np.where)")
	print("-----------------")
	start_time = time.time()
	abc_df['rr2'] = np.where(abc_df.c == "m2", abc_df.a*abc_df.b, abc_df.a*abc_df.b/(1000**2))
	print("Time elapsed: {:.3f} seconds".format(time.time() - start_time))
	print()
	
	print("pandas (np.select)")
	print("-----------------")
	start_time = time.time()
	abc_df['rr3'] = np.select(condlist = [abc_df.c == "m2", abc_df.c == "km2"], choicelist = [abc_df.a*abc_df.b, abc_df.a*abc_df.b/(1000**2)], default = -1)
	print("Time elapsed: {:.3f} seconds".format(time.time() - start_time))
	print()
	# import pdb; pdb.set_trace()
	
	print("numpy")
	print("-----")
	start_time = time.time()
	m2_indexes = (c_npa == "m2")
	km2_indexes = (c_npa == "km2")
	rr_m2_npa = get_area_m2(a_npa[m2_indexes], b_npa[m2_indexes])
	rr_km2_npa = get_area_km2(a_npa[km2_indexes], b_npa[km2_indexes])
	print("Time elapsed: {:.3f} seconds".format(time.time() - start_time))
	print()
	
	print("For-loop")
	print("--------")
	start_time = time.time()
	rr_list = []
	for index_ in range(ss):
		rr_list.append(get_area(a_list[index_], b_list[index_], c_list[index_]))
	# print(rr_list)
	print("Time elapsed: {:.3f} seconds".format(time.time() - start_time))
	print()
	
	print("np.vectorize")
	print("-------------")
	
	# compute results
	start_time = time.time()
	rr_npa = v_get_area(a_npa, b_npa, c_npa)
	print("Time elapsed: {:.3f} seconds".format(time.time() - start_time))
	

## -------- SOMETHING WENT WRONG -----------------------------	
except:

	import traceback
	LOG.error("Something went wrong! Exception details:\n{}".format(traceback.format_exc()))

## -------- GIVE THE USER A CHANCE TO READ MESSAGES-----------
finally:
	
	input("Press any key to exit ...")
