import json
from io import BytesIO
from typing import Any, Dict

import pandas as pd


class DefaultLoader:

    def __init__(self, mime: str, all_sheets: bool = False):
        self.mime = mime
        self.all_sheets = all_sheets

    def __call__(self, buffer: BytesIO, *args: Any, **kwds: Any) -> Any:
        if self.mime == "json":
            return read_json(buffer)
        elif self.mime == "csv":
            return read_csv_buffer(buffer)
        elif self.mime == "xlsx":
            if self.all_sheets:
                return read_xlsx_sheets_buffer(buffer)
            else:
                return read_excel_buffer(buffer)


def read_json(buffer: BytesIO) -> Any:
    return json.load(buffer)


def read_csv_buffer(buffer: BytesIO) -> pd.DataFrame:
    dataframe = pd.read_csv(buffer)
    return dataframe


def read_excel_buffer(buffer: BytesIO, sheet_name=0) -> pd.DataFrame:
    dataframe = pd.read_excel(buffer, sheet_name=sheet_name)
    return dataframe


def read_xlsx_sheets_buffer(buffer: BytesIO) -> Dict[Any, pd.DataFrame]:
    dataframes = {}
    with pd.ExcelFile(buffer) as xlsx:
        for sheet_name in xlsx.sheet_names:
            df = pd.read_excel(xlsx, sheet_name=sheet_name)
            dataframes[sheet_name] = df
    return dataframes
