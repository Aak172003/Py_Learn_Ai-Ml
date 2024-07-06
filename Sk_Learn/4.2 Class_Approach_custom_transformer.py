from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


class MedianIQRScalar(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.median_ = None
        self.iqr_ = None

    def fit(self, x, y=None):
        # calculate medians and inter-quartile range for each feature
        self.median_ = np.median(x, axis=0)
        Q1 = np.percentile(x, 25, axis=0)
        Q2 = np.percentile(x, 75, axis=0)

        print(f"Q1 : {Q1}")
        print(f"Q2 : {Q2}")
        self.iqr_ = Q2 - Q1

        print("self.iqr : ", self.iqr_)

        # Handle a case where IQR is 0 to avoid division by zero during transform
        self.iqr_[self.iqr_ == 0] = 1
        return self

    def transform(self, x):
        if self.median_ is None or self.iqr_ is None:
            raise RuntimeError("The transformer has not been filled yet. ")

        return (x - self.median_) / self.iqr_


from sklearn.datasets import make_blobs

x, _ = make_blobs(n_samples=100, n_features=2, centers=3, random_state=42)

# Creating Object
scalar = MedianIQRScalar()

# fit the scale to the data
scalar.fit(x)

# Transform the data
x_scaled = scalar.transform(x)

# Check the first few rows of the transformed data
print("Transformer data (first 5 rows) : ")
print(x_scaled[0:5])
