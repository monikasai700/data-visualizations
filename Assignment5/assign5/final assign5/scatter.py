import pandas as pd
import matplotlib.pyplot as plt
# load the data from the file
df = pd.read_csv('forscatter.csv')
# import the scatter_matrix functionality
from pandas.tools.plotting import scatter_matrix
# define colors list, to be used to plot survived either red (=0) or green (=1)
colors=['red','green']
# make a scatter plot
scatter_matrix(df,figsize=[20,20],marker='x')
plt.show()
df.info()