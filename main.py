!pip install sklearn
!pip install pandas

#the importion part
import pandas as pd
import numpy as npy
from sklearn.tree import DecisionTreeClassifier

#now the csv file is imported
M = pd.read_csv(r"music.csv")
M #rub this if you dont want to inspect this
#splitting this into sections