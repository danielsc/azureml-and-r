import pandas as pd
import os
os.environ["AZUREML_MODEL_DIR"] = os.getcwd()

data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data', 'attrition.csv')

data = pd.read_csv(data_path)
data.head()

from score import init,run

init()
ret = run(data.head())

print(ret.__class__)
print(ret)


