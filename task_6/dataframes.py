from datetime import datetime

import pandas as pd

from main import validate_data, get_data


def transform_data() -> pd.DataFrame:
    data = get_data()
    documents = validate_data(data)
    df = pd.DataFrame(documents)
    df.rename(columns={'key1': 'document_id',
                       'key2': 'document_dt',
                       'key3': 'document_name'}, inplace=True)
    return df


def add_column() -> pd.DataFrame:
    df = transform_data()
    df["load_dt"] = datetime.now()
    return df
