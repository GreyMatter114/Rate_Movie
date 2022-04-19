import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import pickle
from generate import *

df = pd.DataFrame.from_dict(di)
print(df)
X = df[['Script','Technique','VFX','Direction','Acting']]
y = df[['Overall']]
regr = linear_model.LinearRegression()
regr.fit(X, y)
with open('model','wb') as f:
  pickle.dump(regr,f)


