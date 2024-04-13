# Pandas: Apply a Function to each Cell of a DataFrame

import math
import pandas as pd

df = pd.DataFrame({
    'A': [1, 1, 1, 2, 3],
    'B': [1, 2, 3, 4, 5],
    'C': [0, 0, 3, 4, 5],
})

print(df)

print('-' * 50)

print(df.applymap(math.sqrt))