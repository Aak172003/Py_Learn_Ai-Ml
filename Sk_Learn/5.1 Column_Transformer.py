import pandas as pd
import numpy as np

# Define the data with Social Media Platform, reviews, age and sentiments
# All are of different datatypes data
# Means these all are heterogeneous data
# Note: we can't apply multiple transformation on single column

# numeric labels for sentiment

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

# Create dataframe
df = pd.DataFrame(data)
print(df)

from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

# Define the column transformer
column_transformer = ColumnTransformer(
    transformers=[
        ('platform_ohe', OneHotEncoder(), ['Social Media Platform']),
        ('review_bow', CountVectorizer(), 'Review'),
        ('age_impute', SimpleImputer(), ['age'])
    ],
    # Drop other columns not specified in transformers,
    # because sentiment is output, but if we had another feature, so I will mention
    remainder='drop')

print(pd.DataFrame(column_transformer.fit_transform(df).toarray(), columns=column_transformer.get_feature_names_out()))
