from dataclasses import dataclass
from typing import Tuple

from src.controller.models.model import Model
from src.db import Database


@dataclass
class Label:
    id: int
    name: str


class LabelModel(Model):
    def __init__(self):
        super().__init__()
        self.db = Database()

    def get(self) -> Tuple[Label]:
        dict_labels = self.db.fetchall('labels', ('id', 'name'))
        return tuple(map(lambda label: Label(**label), dict_labels))

    def save(self, name: str, id: int = None) -> Label:
        return Label(
            name=name,
            id=self.db.update('labels', id, {'name': name}) if id else self.db.insert('labels', {'name': name}),
        )

    def delete(self, id: int) -> None:
        self.db.delete('labels', id)
