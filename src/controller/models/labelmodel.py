from dataclasses import dataclass
from functools import partial
from typing import Iterable

from src.controller.models.model import Model


@dataclass
class Label:
    name: str
    id: int = None


class LabelModel(Model):
    def __init__(self):
        super().__init__()

    def get(self) -> Iterable[Label]:
        return map(lambda dict_label: Label(name=dict_label['name'], id=dict_label['id']),
                   self.db.fetchall('labels', ('id', 'name')))

    def save(self, label: Label) -> Label:
        action = partial(self.db.update, 'labels', label.id) if label.id else partial(self.db.insert, 'labels')
        return Label(
            name=label.name,
            id=action({'name': label.name}),
        )

    def delete(self, id: int) -> None:
        self.db.delete('labels', id)
