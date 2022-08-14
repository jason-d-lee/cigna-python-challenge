import numpy as np
import pandas as pd

data = pd.read_csv('python\data.csv')

for col in data.columns[1:]:
    print('Column: ' + str(col))
    print('Min: ' + str(data[col].min()))
    print('Max: ' + str(data[col].max()))
    print('Avg: ' + str(data[col].mean()))
    print()

flattened_data = pd.Series(np.array(data.iloc[:, 1:]).flatten()).dropna()

print('Maximum Value Of All Results: {}'.format(flattened_data.max()))
print('Minimum Value Of All Results: {}'.format(flattened_data.min()))
print('Average Value Of All Results: {}'.format(flattened_data.mean()))