from dataclasses import dataclass
from functools import partial
from typing import Tuple

from src.controller.models.model import Model


@dataclass(unsafe_hash=True)
class Label:
    name: str
    id: int = None


class LabelModel(Model):
    def __init__(self):
        super().__init__()
        self.labels = None

    def get(self) -> Tuple[Label]:
        if self.labels is None:
            self._update()
        return self.labels

    def save(self, label: Label) -> Label:
        action = partial(self.db.update, 'labels', label.id) if label.id else partial(self.db.insert, 'labels')
        label = Label(name=label.name,
                      id=action({'name': label.name}))
        self._update()
        return label

    def delete(self, id: int) -> None:
        self.db.delete('labels', where=f'id={id}')
        self._update()

    def _update(self):
        dict_labels = self.db.select('labels', ('id', 'name'))
        self.labels = tuple(map(lambda label: Label(**label), dict_labels))
