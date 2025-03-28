import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
import os

print("Started From Here")

melb_data_path = "./melb_data.csv"

#print(os.path.exists(melb_data_path))

data = pd.read_csv(melb_data_path)

y = data.Price

X = data.drop(['Price'], axis=1)

#print(X.head())

X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

#print(y_valid_full)

missing_columns = [col for col in X_train_full
                    if X_train_full[col].isnull().any()]

#print(X_train_full.head())
X_train_full.drop(missing_columns, axis=1, inplace=True)
X_valid_full.drop(missing_columns, axis=1, inplace=True)
#print(X_train_full.head())

low_cordinality_columns = [ccolumns for ccolumns in X_train_full.columns
                            if X_train_full[ccolumns].dtype == 'object' and X_train_full[ccolumns].nunique() <= 10]

#print(low_cordinality_columns)

numerical_cols = [ncol for ncol in X_train_full.columns
                    if X_train_full[ncol].dtype in ["float64", "int64"]]

#print(numerical_cols)

my_cols = low_cordinality_columns + numerical_cols

X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()

s = (X_train.dtypes == 'object')
#print(s)
object_cols = list(s[s].index)
#print(object_cols)

def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100,random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    error = mean_absolute_error(y_valid, preds)
    return error
    
drop_X_train = X_train.select_dtypes(exclude=['object'])
#print(X_train.columns)
#print(drop_X_train.columns)
drop_X_valid = X_valid.select_dtypes(exclude=['object'])
print(score_dataset(drop_X_train, drop_X_valid, y_train, y_valid))

ordinal_encoder = OrdinalEncoder()

lable_X_train = X_train.copy()
lable_X_valid = X_valid.copy()

lable_X_train[object_cols] = ordinal_encoder.fit_transform(X_train[object_cols])
lable_X_valid[object_cols] = ordinal_encoder.transform(X_valid[object_cols])

print(score_dataset(lable_X_train, lable_X_valid, y_train, y_valid))

print("hi")