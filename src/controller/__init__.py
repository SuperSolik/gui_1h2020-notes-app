from typing import List

from src.controller.models.labelmodel import LabelModel, Label
from src.db import Database
from src.interfaces.iview import IView


class Controller:
    def __init__(self, view: IView):
        self.view = view
        self.db = Database()
        self.labels = LabelModel()

    def get_labels(self) -> List[Label]:
        return self.labels.get()

    def create_label(self, name: str) -> Label:
        return self.labels.save(name)

    def delete_label(self, id: int) -> None:
        self.labels.delete(id)

    def update_label(self, label: Label) -> None:
        self.labels.save(label.name, label.id)
