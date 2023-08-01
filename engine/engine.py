from abc import ABC

class Engine(ABC):
    def needs_service(self):
        raise NotImplementedError("needs_service() method must be implemented in subclasses.")
