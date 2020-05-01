import time
from dataclasses import dataclass
from datetime import datetime
from functools import partial
from typing import Iterable, List

from src.controller.models.model import Model


@dataclass
class Note:
    name: str
    content: str
    date: datetime = None
    id: int = None


class NoteModel(Model):
    def __init__(self):
        super().__init__()

    def get(self) -> Iterable[Note]:
        return map(
            lambda dict_note: Note(
                id=dict_note['id'],
                name=dict_note['name'],
                content=dict_note['content'],
                date=datetime.fromtimestamp(dict_note['date'])
            ),
            self.db.fetchall('notes', ('id', 'name', 'content', 'date'))
        )

    def save(self, note: Note) -> Note:
        action = partial(self.db.update, 'notes', note.id) if note.id else partial(self.db.insert, 'notes')
        now = time.time()
        return Note(
            name=note.name,
            content=note.content,
            date=datetime.fromtimestamp(now),
            id=action({
                'name': note.name,
                'content': note.content,
                'date': now
            })
        )

    def delete(self, id: int) -> None:
        self.db.delete('notes', id)

    def add_label(self, note_id: int, label_ids: List[int]):
