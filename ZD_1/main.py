import pandas as pd
import numpy as np

# Create 15 rows, 4 columns with column names A B C D of random ints from 0 100
df = pd.DataFrame(np.random.randint(
    0, 100, size=(15, 4)), columns=list('ABCD'))


def min_max(item):
    '''It is a scaling technique method in which data points are shifted 
    and rescaled so that they end up in a range of 0 to 1.
    It is also known as min-max scaling.'''
    return (item - item.min())/(item.max() - item.min())


def standardize(df):
    '''Standardization is another scaling method where the values are centered 
    around mean with a unit standard deviation'''
    return (df-df.mean())/df.std()


df_norm = df.apply(min_max)
df_stand = standardize(df)

print(df)
print(df_norm)
print(df_stand)
