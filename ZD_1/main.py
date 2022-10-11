import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(
    0, 100, size=(15, 4)), columns=list('ABCD'))


def min_max(item):
    return (item - item.min())/(item.max() - item.min())


def standardize(df):
    return (df-df.mean())/df.std()


df_norm = df.apply(min_max)
df_stand = standardize(df)

print(df)
print(df_norm)
print(df_stand)
