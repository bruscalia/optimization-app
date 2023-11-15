import json
from io import BytesIO
from typing import Any, Dict

import pandas as pd


class DefaultWriter:

    def __init__(self, mime: str):
        self.mime = mime

    def __call__(self, data: Any, *args: Any, **kwds: Any) -> Any:
        if self.mime == "json":
            return write_json_buffer(data)
        elif self.mime == "csv":
            assert isinstance(data, pd.DataFrame), "Data is not a dataframe to write to csv"
            return write_csv_buffer(data)
        elif self.mime == "xlsx":
            if isinstance(data, dict):
                return write_frames_xlsx_buffer(data)
            elif isinstance(data, pd.DataFrame):
                return write_xlsx_buffer(data)
            else:
                raise ValueError(f"Wrong datatype for xlsx {type(data)}")


def write_json_buffer(data: Any) -> BytesIO:
    buffer = BytesIO()
    json_str = json.dumps(data)
    buffer.write(json_str.encode('utf-8'))  # Encoding to bytes
    buffer.seek(0)
    return buffer


def write_csv_buffer(dataframe: pd.DataFrame) -> BytesIO:
    buffer = BytesIO()
    dataframe.to_csv(buffer)
    buffer.seek(0)
    return buffer


def write_xlsx_buffer(dataframe: pd.DataFrame) -> BytesIO:
    buffer = BytesIO()
    with pd.ExcelWriter(buffer) as xlsx:
        dataframe.to_excel(xlsx)
    buffer.seek(0)
    return buffer


def write_frames_xlsx_buffer(dataframes: Dict[str, pd.DataFrame]) -> BytesIO:
    buffer = BytesIO()
    with pd.ExcelWriter(buffer) as xlsx:
        for sheet_name, df in dataframes.items():
            df.to_excel(xlsx, sheet_name=sheet_name)
    buffer.seek(0)
    return buffer
