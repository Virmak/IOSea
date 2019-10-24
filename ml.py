import json
import numpy as np
from sklearn.linear_model import LinearRegression



trainData = json.load(open("train_data.json", "r"))

trainInput = list()
trainOutput = list()

for row in trainData:
    trainInput.append(row['date'])
    trainOutput.append(row['sea_level'])

ti = np.array(trainInput)
ti.reshape(-1, 1)
print(ti)

predictor = LinearRegression(n_jobs = -1)
predictor.fit(X=ti, y=trainOutput)