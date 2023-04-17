from typing import Any, Protocol


class Database(Protocol):
    def create(self, new_row: Any) -> Any:
        ...

    def create_many(self, new_rows: list[Any]) -> None:
        ...

    def get(self, model: Any, filter: dict) -> Any:
        ...

    def get_all(self, model: Any) -> list[Any]:
        ...

    def update(self, filter: dict, model: Any, new_row: Any) -> None:
        ...

    def delete(self, filter: dict, model: Any) -> None:
        ...
