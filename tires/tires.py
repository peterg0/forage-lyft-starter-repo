from abc import ABC, abstractmethod

class Tires(ABC):
    def __init__(self, sensorScore):
        self.sensorScore = sensorScore

    @abstractmethod
    def needs_service(self):
        pass
