from dataclasses import dataclass
from functools import partial, lru_cache
from typing import Iterable

from src.controller.models.model import Model


@dataclass(unsafe_hash=True)
class Label:
    name: str
    id: int = None


class LabelModel(Model):
    def __init__(self):
        super().__init__()

    @lru_cache(maxsize=1)
    def get(self) -> Iterable[Label]:
        dict_labels = self.db.select('labels', ('id', 'name'))
        return map(lambda label: Label(**label), dict_labels)

    def save(self, label: Label) -> Label:
        action = partial(self.db.update, 'labels', label.id) if label.id else partial(self.db.insert, 'labels')
        label = Label(name=label.name,
                      id=action({'name': label.name}))
        self.get.cache_clear()
        return label

    def delete(self, id: int) -> None:
        self.db.delete('labels', where=f'id={id}')
        self.get.cache_clear()

