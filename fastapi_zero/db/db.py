from abc import ABC, abstractmethod


class BaseDB(ABC):
    @abstractmethod
    def get_session(self):
        """Get a new database session."""
        pass
