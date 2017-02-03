import pandas as pd
import numpy as np
import os

df = pd.DataFrame()

for f in ['C:\Users\Sai Monika Tadaka\Documents\Data Visualization\jenna\GE2012Cty (1)']:
    data = pd.read_excel(f, 'Sheet1')
    df = df.append(data)

df.to_excel("C:\Users\Sai Monika Tadaka\Documents\Data Visualization\jenna\GE2012Tot (1)")