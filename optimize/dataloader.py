import json
from io import BytesIO
from typing import Any, Dict

import pandas as pd


def read_json(buffer: BytesIO) -> Any:
    return json.load(buffer)


def csv_to_buffer(buffer: BytesIO) -> pd.DataFrame:
    dataframe = pd.read_csv(buffer)
    return dataframe


def excel_to_buffer(buffer: BytesIO, sheet_name=None) -> pd.DataFrame:
    dataframe = pd.read_excel(buffer, sheet_name=sheet_name)
    return dataframe


def dataframes_from_xlsx_buffer(buffer: BytesIO) -> Dict[Any, pd.DataFrame]:
    dataframes = {}
    with pd.ExcelFile(buffer) as xlsx:
        for sheet_name in xlsx.sheet_names:
            df = pd.read_excel(xlsx, sheet_name=sheet_name)
            dataframes[sheet_name] = df
    return dataframes
