from abc import ABC

from car import Car


class Battery(ABC):
    def needs_service(self):
        raise NotImplementedError("needs_service() method must be implemented in subclasses.")
