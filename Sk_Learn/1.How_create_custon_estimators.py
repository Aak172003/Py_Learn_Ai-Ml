from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.utils.validation import check_X_y


# Inherit this class from two classes (BaseEstimator, ClassifierMixin),
# This is because we are trying to make c class which is compatible with a sklearn library, which means
# we can access all things from sklearn via user_create_class

# BaseEstimator , ClassifierMixin -> These both are base classes
class MostFrequentClassClassifier(BaseEstimator, ClassifierMixin):

    # Python Constructor
    def __init__(self):
        self.most_frequent_ = None

    def fit(self, X, y):
        # validate input X and target vector y
        X, y = check_X_y(X, y)

        # Ensure y is 1D -> because output col must be single or 1D
        y = np.ravel(y)

        # Manually compute the most frequent class
        unique_classes, counts = np.unique(y, return_counts=True)
        self.most_frequent_ = unique_classes[np.argmax(counts)]

        return self

    # Predict logic
    def predict(self, x):
        if self.most_frequent_ is None:
            raise ValueError("This classifier instance is not fitted yet")

        # Predict the most frequent class for each input sample
        return np.full(shape=(x.shape[0],), fill_value=self.most_frequent_)

    def score(self, x, y):
        """Rerurn the mean accuracy on the given test data and labels......"""
        y = np.ravel(y)
        predictions = self.predict(x)
        return accuracy_score(y, predictions)
# Call above class

from sklearn.model_selection import train_test_split

# sklearn have datasets as well
from sklearn.datasets import load_iris

iris = load_iris()
print("iris : : : ", iris)
x, y = iris.data, iris.target

print("-----------------------------------")
print(x)
print(y)
print("-----------------------------------")

# split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)

print(x_train)
print(x_test)

print("--------------------")
print(y_train)
print(y_test)

# create an object of the above class
# and use its functions via. operator
classifier = MostFrequentClassClassifier()
classifier.fit(x_train, y_train)

score = classifier.score(x_test, y_test)
print(f"Accuracy of MostFrequentClassClassifier : {score} ")

# make predictions
predictions = classifier.predict(x_test)
# Evaluate the custom Estimator
print(f"Predict class for all test instruments : {predictions[0]}")

print(f"classifier.most_frequent_ --------------  {classifier.most_frequent_}")

from sklearn.model_selection import cross_val_score

print(cross_val_score(classifier, x_train, y_train))
