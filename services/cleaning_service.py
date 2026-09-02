
def validate_data(df):

    shape = df.shape

    missing_values = df.isnull().sum()

    duplicate_count = df.duplicated().sum()

    columns = df.columns.tolist()

    datatypes = df.dtypes


    validation_report = {
        "shape": shape,
        "missing_values": missing_values,
        "duplicate_count": duplicate_count,
        "columns": columns,
        "datatypes": datatypes
    }

    return validation_report