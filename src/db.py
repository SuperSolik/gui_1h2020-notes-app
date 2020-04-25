import os
import sqlite3
import sys
from typing import Dict, Tuple, List


# DEV_NOTE_DB needs to be set before app usage
# export DEV_NOTE_DB=<path to db>
class Database:
    def __init__(self):
        self.conn = sqlite3.connect(os.getenv("DEV_NOTE_DB"))
        self.cursor = self.conn.cursor()
        self.check_connection()

    def __del__(self):
        self.conn.close()

    @staticmethod
    def rows_to_dict(cols: Tuple[str], rows: List[Tuple]) -> List[Dict]:
        result = []
        for row in rows:
            dict_row = dict(zip(cols, row))
            result.append(dict_row)
        return result

    def insert(self, table: str, column_values: Dict) -> None:
        columns = ', '.join(column_values.keys())
        values = [tuple(column_values.values())]
        placeholders = ', '.join('?' * len(column_values.keys()))
        self.cursor.executemany(
            f"insert into {table} "
            f"({columns}) "
            f"values ({placeholders})",
            values)
        conn.commit()

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
        conn.commit()

    def fetchall(self, table: str, columns: Tuple[str]) -> List[Dict]:
        columns_joined = ", ".join(columns)
        self.cursor.execute(f"select {columns_joined} from {table}")
        rows = self.cursor.fetchall()
        return rows_to_dict(columns, rows)

    def delete(self, table: str, row_id: int) -> None:
        row_id = int(row_id)
        self.cursor.execute(f"delete from {table} where id={row_id}")
        conn.commit()

    def check_connection(self) -> None:
        self.cursor.execute(
            "select name from sqlite_master "
            "where type='table' and name='notes'")
        table_exists = self.cursor.fetchall()
        if not table_exists:
            sys.exit('Connection to db failed')
