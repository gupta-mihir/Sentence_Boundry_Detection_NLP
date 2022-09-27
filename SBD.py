import sklearn
import pandas as pd
#Learning how to use sklearn 
from sklearn.datasets import load_iris
iriss = load_iris()
df_iris = pd.DataFrame(iriss.data, columns=iriss.feature_names)
df_iris.head()

with open('SBD.train.txt') as f:
    lines = f.read(1000)
    print(lines, end='')
    #need to import learn library
