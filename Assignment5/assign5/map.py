import numpy as np
data = np.genfromtxt('C:\Users\Sai Monika Tadaka\Documents\Data Visualization\Assignment5\assign5\try.csv', delimiter=',', skip_header=10,
                     skip_footer=10, names=True)
ax1.plot(data['x'], data['y'], color='r', label='the data')