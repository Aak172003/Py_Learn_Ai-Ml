# Pipeline:

# 1. Apply multiple Transformation
# 2. But these transformations apply on sequentially (Output of previous transformation becomes input for the next transformer)
# 3. Apply on entire datasets

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Generating a random dataset with 10 rows and 4 columns
np.random.seed(42)
data = np.random.randn(10, 4)

# Creating a DataFrame and naming the columns
df = pd.DataFrame(data, columns=['f1', 'f2', 'f3', 'y'])

print(df)

from sklearn.pipeline import Pipeline

# Define FeatureUnion
pipeline = Pipeline([
    # Apply StandardScaler -> give 3 columns
    ('scaler', StandardScaler()),
    # Apply PCA, give 2 more pc1, pc2 columns
    ('pca', PCA(n_components=2))
])

# After Apply PCA we have only 2 rows,
# because initially we have 3 columns so in a fist step,
# when I apply standard scalar so this gives 3 columns, but I want to apply PCA, these 3 columns became input for PCA Transforms

x_transformed = pipeline.fit_transform(df)

print(pd.DataFrame(pipeline.fit_transform(x_transformed), columns=pipeline.get_feature_names_out()))
