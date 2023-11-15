import json
from io import BytesIO
from typing import Any, Dict

import pandas as pd


def json_to_buffer(data: Any) -> BytesIO:
    buffer = BytesIO()
    json.dump(data, buffer)
    buffer.seek(0)
    return buffer


def csv_to_buffer(dataframe: pd.DataFrame) -> BytesIO:
    buffer = BytesIO()
    dataframe.to_csv(buffer)
    buffer.seek(0)
    return buffer


def excel_to_buffer(dataframe: pd.DataFrame) -> BytesIO:
    buffer = BytesIO()
    with pd.ExcelWriter(buffer) as xlsx:
        dataframe.to_excel(xlsx)
    buffer.seek(0)
    return buffer


def dataframes_to_xlsx_buffer(dataframes: Dict[str, pd.DataFrame]) -> BytesIO:
    buffer = BytesIO()
    with pd.ExcelWriter(buffer) as xlsx:
        for sheet_name, df in dataframes.items():
            df.to_excel(xlsx, sheet_name=sheet_name)
    buffer.seek(0)
    return buffer
