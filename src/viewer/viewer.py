from abc import ABC, abstractmethod


class Viewer(ABC):
    @abstractmethod
    def show_message(self, message: str) -> None:
        pass

    @abstractmethod
    def show_response(self, response) -> None:
        pass
