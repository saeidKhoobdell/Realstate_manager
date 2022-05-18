from abc import ABC, abstractmethod


class Region(ABC):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)