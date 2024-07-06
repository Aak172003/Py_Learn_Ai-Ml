import pandas as pd

df = pd.read_csv('D:\\Python_Things\\Py_Learn-main\\Practical_Tools\\Csv_Files\\titanic.csv',
                 usecols=['Pclass', 'Survived',
                          'Age'])

print("df['Age'] : ", df['Age'])
# print(df.head(10))

# fill the NaN values from median
# (Means find median of individual feature and fill that where NaN is present)
df['Age'] = df['Age'].fillna(df['Age'].median())

print("df['Age'] : : : :: ", df['Age'])
# Give the idea about no of NaN values still present or not if yes, so how many present
print(df.isnull().sum())

from sklearn.model_selection import train_test_split

X = df.iloc[:, 1:]
y = df.iloc[:, 0]

print("X", X)
print("y", y)
# split the data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

print("-----------------------------------------------------------------")
print("About X")
print(X_train)
print(X_test)

print("About y")
print("y_train : ", y_train)
print("y_test : ", y_test)

from sklearn.preprocessing import StandardScaler

scalar = StandardScaler()

# Here a scalar object learns and transforms the given input data
X_train_scaled = scalar.fit_transform(X_train)

print("X_train_scalar ::::::::::::::: ")
print(X_train_scaled)

print(X_test)

# perform transform on test data so that we can train our model on transformed data
X_test_scaled = scalar.transform(X_test)
print(X_test_scaled)

print(X_test)

# Model Building -> perform two thing
# .fit() -> fit for the train data
# .predict() -> predict for the test data

from sklearn.linear_model import LogisticRegression
classification = LogisticRegression()

# scaled input, output
print(classification.fit(X_train_scaled, y_train))

# Prediction
print(classification.predict(X_test_scaled))


