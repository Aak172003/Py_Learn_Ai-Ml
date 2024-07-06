import pandas as pd
import numpy as np

# Define the data with numeric labels for sentiment
data = {
    "Social Media Platform": ["Twitter", "Facebook", "Instagram", "Twitter", "Facebook",
                              "Instagram", "Twitter", "Facebook", "Instagram", "Twitter"],
    "Review": ["Love the new update!", "Too many ads now", "Great for sharing photos",
               "Newsfeed algorithm is biased", "Privacy concerns with latest update",
               "Amazing filters!", "Too much spam", "Easy to connect with friends",
               "Stories feature is fantastic", "Customer support lacking"],
    "age": [21, 19, np.nan, 17, 24, np.nan, 30, 19, 16, 31],
    "Sentiment": [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]  # Numeric labels: 1 for Positive, 0 for Negative
}

# Create a DataFrame
df = pd.DataFrame(data)

print(df)

from sklearn.preprocessing import FunctionTransformer, OneHotEncoder
from sklearn.pipeline import FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer


def count_words(reviews):
    # Count the number of words in each review
    # Assuming reviews is a 1D array-like of text strings
    return np.array([len(review.split()) for review in reviews]).reshape(-1, 1)


# Create the FunctionTransformer using the count_words function
# word_count_transformer -> this is a transformer, this can easily access all functionalities of sklearn library

word_count_transformer = FunctionTransformer(count_words)

feature_union = FeatureUnion([
    ('word_count', word_count_transformer),
    ('bag_of_words', CountVectorizer())
])

# This defines what transformer applies on which column
# Transformer is used because we can apply different transformer on separate columns

column_transformer = ColumnTransformer(
    transformers=[
        # simple implement impute to handle null values
        ('age_imputer', SimpleImputer(strategy='mean'), ['age']),
        # Simple applies One hot encoder (This gives common name)
        ('platform_ohe', OneHotEncoder(), ['Social Media Platform']),

        # This applies feature Union and feature union define above
        # Feature union itself apply two transformer
        # 1. Word of bag
        # 2. Word count - >word count is not a built - in transformer, so I build by myself
        ('review_processing', feature_union, 'Review')
    ],
    remainder='drop'  # Drop other columns not specified here
)

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MaxAbsScaler
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.pipeline import Pipeline

final_pipeline = Pipeline(steps=[
    ('col_transformer', column_transformer),
    ('scaler', MaxAbsScaler()),
    ('selector', SelectKBest(score_func=chi2, k=10)),
    ('classifier', LogisticRegression())
])

print(final_pipeline.fit(df.drop(columns=['Sentiment']), df['Sentiment'])
)
