from typing import List
from recordclass import RecordClass

from src.controller.models.model import Model
from src.db import Database


class Label(RecordClass):
    id: int
    name: str


class LabelModel(Model):
    def __init__(self):
        super().__init__()
        self.db = Database()

    def get(self) -> List[Label]:
        return self.db.fetchall('labels', ('id', 'name'))

    def save(self, name: str, id: int = None) -> Label:
        return Label(
            name=name,
            id=self.db.update('labels', id, {'name': name}) if id else self.db.insert('labels', {'name': name}),
        )

    def delete(self, id: int) -> None:
        self.db.delete('labels', id)
