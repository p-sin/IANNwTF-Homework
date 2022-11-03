from __future__ import annotations  # 3.10 <= python version


class Cat:
    def __init__(self, name: str):
        self.name = name

    def greet(self, other: Cat):
        print(f"Hello I am {self.name}! I see you are also a cool " +
              f"fluffy kitty {other.name}, let’s together purr at " +
              "the human, so that they shall give us food!")
