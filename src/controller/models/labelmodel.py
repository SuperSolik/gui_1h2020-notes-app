from dataclasses import dataclass
from typing import Iterable
from functools import partial

from src.controller.models.model import Model


@dataclass
class Label:
    name: str
    id: int = None


class LabelModel(Model):
    def __init__(self):
        super().__init__()

    def get(self) -> Iterable[Label]:
        dict_labels = self.db.select('labels', ('id', 'name'))
        return map(lambda label: Label(**label), dict_labels)

    def save(self, label: Label) -> Label:
        action = partial(self.db.update, 'labels', label.id) if label.id else partial(self.db.insert, 'labels')
        return Label(name=label.name,
                     id=action({'name': label.name}))

    def delete(self, id: int) -> None:
        self.db.delete('labels', id)
