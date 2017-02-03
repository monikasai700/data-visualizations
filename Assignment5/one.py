import csv 
import numpy as np
import matplotlib.pyplot as plot
with open('avg.txt') as inf:
 x=[]
 y=[]
 for line in csv.reader(inf):
  plot.scatter(x,y)
 plot.plot(*np.loadtxt("test.txt",unpack=True), linewidth=2.0)

 plot.show()