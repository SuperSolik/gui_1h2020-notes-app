import os
import sqlite3
import sys
from typing import Dict, Tuple, List

from src.shared.singleton import SingletonMeta


# DEV_NOTE_DB needs to be set before app usage
# export DEV_NOTE_DB=<path to db>
class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.conn = sqlite3.connect(os.getenv("DEV_NOTE_DB"))
        self.cursor = self.conn.cursor()
        self.check_connection()

    def __del__(self):
        self.conn.close()

    @staticmethod
    def rows_to_dict(cols: Tuple[str], rows: List[Tuple]) -> List:
        result = []
        for row in rows:
            dict_row = dict(zip(cols, row))
            result.append(dict_row)
        return result

    def insert(self, table: str, column_values: Dict) -> int:
        columns = ', '.join(column_values.keys())
        placeholders = ', '.join('?' * len(column_values.keys()))

        self.cursor.execute(
            f"insert into {table} "
            f"({columns}) "
            f"values ({placeholders})",
            list(column_values.values()))
        self.conn.commit()

        return self.cursor.lastrowid

    def update(self, table: str, row_id: int, column_values: Dict) -> None:
        row_id = int(row_id)
        raw_placeholders = map(lambda col: f"{col} = ?", column_values.keys())
        placeholders = ', '.join(raw_placeholders)
        values = [tuple(column_values.values())]
        self.cursor.executemany(
            f"update {table} set "
            f"{placeholders} "
            f"where id={row_id}",
            values)
        self.conn.commit()

    def fetchall(self, table: str, columns: Tuple[str, ...]) -> List:
        columns_joined = ", ".join(columns)
        self.cursor.execute(f"select {columns_joined} from {table}")
        rows = self.cursor.fetchall()
        return Database.rows_to_dict(columns, rows)

    def delete(self, table: str, row_id: int) -> None:
        row_id = int(row_id)
        self.cursor.execute(f"delete from {table} where id={row_id}")
        self.conn.commit()

    def check_connection(self) -> None:
        self.cursor.execute(
            "select name from sqlite_master "
            "where type='table' and name='notes'")
        table_exists = self.cursor.fetchall()
        if not table_exists:
            sys.exit('Connection to db failed')
