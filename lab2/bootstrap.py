import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
import math

import numpy as np 




def boostrap(statistic_func, iterations, data):
	samples  = np.random.choice(data,replace = True, size = [iterations, len(data)])
	#print samples.shape
	data_mean = data.mean()
	vals = []
	for sample in samples:
		sta = statistic_func(sample)
		#print sta
		vals.append(sta)
	b = np.array(vals)
	#print b
	lower, upper = np.percentile(b, [2.5, 97.5])
	return data_mean,lower, upper



if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	#print df.columns
	
	data = df.values.T[0]
	boot = boostrap(np.mean, 100000, data)
	
	total = 0.0
	for i in data:
		total = total + ((i-boot[0])**2)
	var = total / data.size
	print ("Variance: "+str(var))
	standard_dev = math.sqrt(var)
	print ("Standard Deviation: "+str(standard_dev))
	print (boot)
	


	