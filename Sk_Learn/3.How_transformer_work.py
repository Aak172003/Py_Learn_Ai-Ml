from sklearn.datasets import make_regression
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Generate some datasets
x, y = make_regression(n_samples=100, n_features=2, noise=0.1, random_state=42)

print(x)
print("-------------------------------------------")
print(y)
# use the transformer directly
x_transformd = StandardScaler().fit_transform(x)

print("x_transformd : ", x_transformd)

# Transformer applies in one go all datasets

# Here we give x_transformed and y to linear Regression to learn something from this data
LinearRegression().fit(x_transformd, y)
