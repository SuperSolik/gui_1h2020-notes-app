from src.shared.singleton import SingletonMeta


class Model(metaclass=SingletonMeta):
    def __init__(self):
        self.entities = []

    def save(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass
