from typing import Iterable, Tuple

from src.controller.models.notemodel import NoteModel, Note
from src.controller.models.labelmodel import LabelModel, Label
from src.db import Database


class Controller:
    def __init__(self):
        self.db = Database()
        self.labels = LabelModel()
        self.notes = NoteModel()

    # labels
    def get_labels(self) -> Tuple[Label]:
        return tuple(self.labels.get())

    def save_label(self, label: Label = None) -> Label:
        return self.labels.save(label)

    def delete_label(self, id: int) -> None:
        self.labels.delete(id)

    # notes
    def get_notes(self, label_id: int = None) -> Tuple[Note]:
        return tuple(self.notes.get(label_id))

    def save_note(self, note: Note) -> Note:
        return self.notes.save(note)

    def delete_note(self, id: int) -> None:
        self.notes.delete(id)

    # notes_label
    def add_labels_to_note(self, note_id: int, label_ids: Iterable[int]) -> None:
        self.notes.add_labels(note_id, label_ids)

    def get_labels_for_note(self, note_id) -> Tuple[Label]:
        return tuple(self.notes.get_labels(note_id))