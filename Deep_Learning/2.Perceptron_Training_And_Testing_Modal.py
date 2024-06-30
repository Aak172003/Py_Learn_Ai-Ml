
# from sklearn.datasets import  make_classification
import sklearn.datasets as datasets

make_classification = datasets.make_classification

import numpy as np
import matplotlib.pyplot as plt

# Generate datasets using make_classification in sklearn

x, y = make_classification(n_samples=100, n_features=2, n_informative=1, n_redundant=0, n_classes=2,
                           n_clusters_per_class=1, random_state=41, hypercube=False, class_sep=10)

print("x:\n", x)
print("y: \n", y)

print(plt.figure(figsize=(10, 6)))
print(plt.scatter(x[:, 0], x[:, 1], c=y, cmap='winter', s=100))

plt.show()