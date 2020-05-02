from typing import List

from src.controller.models.notemodel import NoteModel, Note
from src.controller.models.labelmodel import LabelModel, Label
from src.db import Database


class Controller:
    def __init__(self):
        self.db = Database()
        self.labels = LabelModel()
        self.notes = NoteModel()

    # labels
    def get_labels(self) -> List[Label]:
        return list(self.labels.get())

    def save_label(self, label: Label = None) -> Label:
        return self.labels.save(label)

    def delete_label(self, id: int) -> None:
        self.labels.delete(id)

    # notes
    def get_notes(self) -> List[Note]:
        return list(self.notes.get())

    def save_note(self, note: Note) -> Note:
        return self.notes.save(note)

    def delete_note(self, id: int) -> None:
        self.notes.delete(id)

    def add_label_to_note(self, note_id: int, label_ids: List[int]):
        self.notes.add_label(note_id, label_ids)
