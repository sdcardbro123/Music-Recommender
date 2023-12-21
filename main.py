!pip install sklearn
!pip install pandas

#the importion part
import pandas as pd
import numpy as npy
from sklearn.tree import DecisionTreeClassifier

#now the csv file is imported
M = pd.read_txr(r"music.txt")

# Mapping 'Male' to 1 and 'Female' to 0
M['Sex'] = M['Sex'].map({'Male': 1, 'Female': 0})

# Convert other categorical columns to numerical values
M['Continent'] = pd.Categorical(M['Continent']).codes
M['Language Preferences'] = pd.Categorical(M['Language Preferences']).codes

# Display the modified DataFrame or delete if not reqd
print(M)

# Lessgo to lables and features
X = M["Age","Sex","Continent","Language Preferences"]

y = M["Genre"]

