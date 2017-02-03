from pandas import read_csv
import matplotlib.pyplot as plt
from pandas.tools.plotting import parallel_coordinates
data = read_csv('try.csv')
plt.figure()
parallel_coordinates(data,'Index')
plt.show()

