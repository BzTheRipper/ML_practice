from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer
import pandas as pd
import os

path = "./melb_data.csv"

data = pd.read_csv(path)

melb_predictors = data.drop(['Price'], axis=1)


y = data.Price
X = melb_predictors.select_dtypes(exclude=['object'])


X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

def score_dataset(X_train, X_val, y_train, y_val):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_val)
    return mean_absolute_error(y_val, preds)

error_first = score_dataset(X_train, X_val, y_train, y_val)
print(f'Error at first: {error_first}')


missing_columns = [col for col in X_train.columns
    if X_train[col].isnull().any()]

X_train_col = X_train.drop(missing_columns, axis = 1)
X_val_col = X_val.drop(missing_columns, axis = 1)


error_col = score_dataset(X_train_col, X_val_col, y_train, y_val)
print(f'Error after droping columns: {error_col}')


# Drop rows with missing values in X_train and X_val
X_train_row = X_train.dropna()
print(X_train_row)
X_val_row = X_val.dropna()
# Ensure y_train and y_val remain aligned with X_train and X_val
y_train_row = y_train.loc[X_train_row.index]
y_val_row = y_val.loc[X_val_row.index]

error_row = score_dataset(X_train_row, X_val_row, y_train_row, y_val_row)
print(f'Error after droping rows: {error_row}')

my_imputer = SimpleImputer(strategy='mean')


imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_val = pd.DataFrame(my_imputer.transform(X_val))
print(imputed_X_train)
# Just Getting back the columns name....nothing important
imputed_X_train.columns = X_train.columns
imputed_X_val.columns = X_val.columns
print(imputed_X_train)

# It's my experiment for checking not in the tutorial
imputed_Missing_columns_check = [imp_col for imp_col in imputed_X_train
                                 if imputed_X_train[imp_col].isnull().any()]

print(imputed_Missing_columns_check)
# My experiment ended here...

imputed_error = score_dataset(imputed_X_train, imputed_X_val, y_train, y_val)
print(f'Before Binary Imputed error: {imputed_error}')

binary_X_train = X_train.copy()
binary_X_val = X_val.copy()

total_rows_inData = binary_X_train.shape[0]

for get_missing_columns in missing_columns:
    set_missing_value = get_missing_columns+'Missing'
    binary_X_train[set_missing_value] = 1
    binary_X_val[set_missing_value] = 1
    binary_X_train.loc[binary_X_train[get_missing_columns].isna(), set_missing_value] = 0
    binary_X_val.loc[binary_X_val[get_missing_columns].isna(), set_missing_value] = 0
    #print(set_missing_value)




binary_imputer = SimpleImputer(strategy='mean')

imputed_binary_X_train = pd.DataFrame(binary_imputer.fit_transform(binary_X_train))
imputed_binary_X_val = pd.DataFrame(binary_imputer.transform(binary_X_val))


imputed_error = score_dataset(imputed_binary_X_train, imputed_binary_X_val, y_train, y_val)

print(f'After Binary Imputed error: {imputed_error}')


X_train_plus = X_train.copy()
X_val_plus = X_val.copy()

# Make new columns indicating what will be imputed
for col in missing_columns:
    X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
    X_val_plus[col + '_was_missing'] = X_val_plus[col].isnull()


imputed_X_train_plus = pd.DataFrame(my_imputer.fit_transform(X_train_plus))
imputed_X_val_plus = pd.DataFrame(my_imputer.transform(X_val_plus))

imputed_bool_error = score_dataset(imputed_X_train_plus, imputed_X_val_plus, y_train, y_val)

print(f'After Bool Imputed error: {imputed_bool_error}')

missing_val_count_by_column = (X_train.isnull().sum())

get_missing_total = 0
for get_missing_total in missing_val_count_by_column[missing_val_count_by_column>0]:
    get_missing_total += get_missing_total
tot_missing = get_missing_total
print(tot_missing)