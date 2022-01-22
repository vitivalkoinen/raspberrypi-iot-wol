from abc import abstractmethod

class ConfigRepository:
    @abstractmethod
    def load(self):
        pass