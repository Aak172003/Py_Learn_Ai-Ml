# Feature Union:

# 1. Apply multiple Transformation
# 2. But these transformations apply to parallel
# 3. Apply on entire datasets

import pandas as pd
import numpy as np

# Generating the random datasets with 10 rows and 4 columns

# Use seed function to freeze the random value
np.random.seed(100)

data = np.random.randn(10, 4)
print(data)

# Creating a DataFrame and naming the columns
df = pd.DataFrame(data, columns=['f1', 'f2', 'f3', 'y'])

print(df)

from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Define FeatureUnion
feature_union = FeatureUnion([
    # Apply StandardScaler -> give 3 columns
    ('scaler', StandardScaler()),
    # Apply PCA, give 2 more pc1, pc2 columns
    ('pca', PCA(n_components=2))
])

# After horizontally concatenate, we have 5 columns
x_transformed = feature_union.fit_transform(df.drop(columns=['y']))

print("----------------------------")
print(pd.DataFrame(x_transformed, columns=feature_union.get_feature_names_out()))
