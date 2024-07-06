# Type - 1 (Functional Transformer) -> these are those kinds of transformer,
# which never learn anything from data, even this transformer is totally independent of data

# These are Stateless Transformer
# Functional Transformer

import numpy as np


def cube_transform(x):
    return np.power(x, 3)


from sklearn.preprocessing import FunctionTransformer

cube_transformer = FunctionTransformer(cube_transform)

# Working part

from sklearn.datasets import make_regression
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Generate some datasets
x, y = make_regression(n_samples=100, n_features=2, noise=0.1, random_state=42)

print(x)
x_transformed = cube_transformer.transform(x)

print("After Transformed ---------------------------- ")
print(x_transformed)

print(LinearRegression().fit(x_transformed, y))
