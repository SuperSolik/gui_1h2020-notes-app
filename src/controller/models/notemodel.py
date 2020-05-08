from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from functools import partial
from itertools import cycle
from typing import Iterable, Dict, cast as typecast

from src.controller.models.labelmodel import Label
from src.controller.models.model import Model


@dataclass
class Note:
    name: str
    content: str
    date: datetime = None
    id: int = None

    @staticmethod
    def from_dict_note(dict_note: Dict) -> Note:
        note = Note(*dict_note.values())
        note.date = datetime.fromtimestamp(typecast(float, note.date))
        return note


class NoteModel(Model):
    def __init__(self):
        super().__init__()

    def get(self, label_id: int = None) -> Iterable[Note]:
        dict_notes = self.db.select(
            'notes', ('notes.name', 'notes.content', 'notes.date', 'notes.id'),
            joins=(('relation', 'notes.id=note_id'), ('labels', 'labels.id=label_id')) if label_id else [],
            where=f'labels.id={label_id}' if label_id else None)
        return map(Note.from_dict_note, dict_notes)

    def save(self, note: Note) -> Note:
        action = partial(self.db.update, 'notes', note.id) if note.id else partial(self.db.insert, 'notes')
        now = datetime.now()
        return Note(name=note.name,
                    content=note.content,
                    date=now,
                    id=action({
                        'name': note.name,
                        'content': note.content,
                        'date': now.timestamp()
                    }))

    def delete(self, id: int) -> None:
        self.db.delete('notes', where=f'id={id}')

    # labels
    def add_labels(self, note_id: int, label_ids: Iterable[int]) -> None:
        self.db.insert_many('relation', ('note_id', 'label_id'), zip(cycle([note_id]), label_ids))

    def delete_labels(self, note_id: int, label_ids: Iterable[int]) -> None:
        joined_label_ids = ', '.join(map(str, label_ids))
        self.db.delete('relation', where=f"note_id={note_id} and label_id in ({joined_label_ids})")

    def get_labels(self, note_id: int) -> Iterable[Label]:
        rows = self.db.select('notes', ('labels.name', 'labels.id'),
                              joins=(('relation', 'notes.id=note_id'), ('labels', 'labels.id=label_id')),
                              where=f'notes.id={note_id}')
        return map(lambda row: Label(*row.values()), rows)
