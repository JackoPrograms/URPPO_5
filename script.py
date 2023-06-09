import timeit

code ="""
import pandas as pd
import numpy as np
import tensorflow as tf


data = pd.read_csv('iris.data', header=None, names=['column 1', 'column 2', 'column 3','column 4', 'Title'])
print(data)

df = data.drop(columns=[
    'column 2'
])
print(df)

# with tf.device('/device:CPU:0'):
# with tf.device('/GPU:0'):
with tf.device('/job:localhost/replica:0/task:0/device:GPU:1'):
    def Sqrt(x):
        Sqrt_all = 0
        for i in range(x*x):
            Sqrt_all += np.sqrt(x)
        return Sqrt_all

    df.loc[df["column 1"] >= 6, "column 1"] = Sqrt(10000)
    print(df)

"""
execution_time = timeit.timeit(stmt = code,  number = 1)
print("Single Execution time:",execution_time, "seconds")