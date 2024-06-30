import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('D:\\Python_Things\\Py_Learn\\Deep_Learning\\placement.csv')

# Print the DataFrame and its shape
print(df)
print(df.shape)

# Correct the scatter plot call
sns.scatterplot(x=df['cgpa'], y=df['resume_score'], hue=df['placed'])

# Show the plot
plt.show()

x = df.iloc[:, 0:2]
y = df.iloc[:, -1]

print("x : ", x.head(), "y :", y.head())

from sklearn.linear_model import Perceptron

p = Perceptron()

print("Perceptron : ", p)

p.fit(x, y)
print("w1 , w2 -> ", p.coef_)

print("b -> ", p.intercept_)

print("Shape of x:", x.shape)

from mlxtend.plotting import plot_decision_regions

# Ensure 'x' is a numpy array and 'y' is a 1-dimensional array
x = x.values
y = y.values

plot_decision_regions(x, y, clf=p, legend=2)

# Show the plot
plt.show()
