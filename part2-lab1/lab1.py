# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":

    from abc import ABC, abstractmethod
    import doctest


    class Door(ABC):
        def __init__(self, height: float, width: float, material: str):
            if height <= 0 or width <= 0:
                raise ValueError("размеры двери не могут быть ноль и меньше")
            self.height = height
            self.width = width
            self.material = material

        def open_door(self) -> str:
            ...

        def close_door(self) -> str:
            ...


    class WoodenDoor(Door):
        def open_door(self) -> str:
            return "Дверь открыта"

        def close_door(self) -> str:
            return "Дверь закрыта"


    class Window(ABC):
        def __init__(self, glass_type: str, is_open: bool):
            self.glass_type = glass_type
            self.is_open = is_open

        def open_window(self) -> None:
            ...

        def close_window(self) -> None:
            ...


    class SlidingWindow(Window):
        def open_window(self) -> None:
            self.is_open = True

        def close_window(self) -> None:
            self.is_open = False


    class ApplePie(ABC):
        def __init__(self, weight: float, apples: int):
            if weight <= 0 or apples <= 0:
                raise ValueError("Вес пирога и количество яблок должны быть больше нуля")
            self.weight = weight
            self.apples = apples

        def bake(self) -> str:
            ...

        def serve(self) -> str:
            ...


    class FreshApplePie(ApplePie):
        def bake(self) -> str:
            return "Яблочный пирог печётся"

        def serve(self) -> str:
            return "Свежий яблочный пирог подаётся к столу."


    if __name__ == "__main__":
        doctest.testmod()
