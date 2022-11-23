"""
Permite adaptar classes de diferentes tipos em uma mesma interface.
Exemplo: Dog, Cat, Human, Car
- o que possuem em comum: fazer barulho
"""

from typing import Callable, TypeVar

T = TypeVar("T")


class Dragon:
    def __init__(self) -> None:
        self.name = "Dragon"

    def roawr(self) -> str:
        return "Roawr!"


class Joker:
    def __init__(self) -> None:
        self.name = "Joker"

    def crazy(self) -> str:
        return "Risadinha!"


class Human:
    def __init__(self) -> None:
        self.name = "Human"

    def speak(self) -> str:
        return "'hello'"


class Adapter:
    """Adapts an object by replacing methods.
    Usage
    ------
    dog = Dog()
    dog = Adapter(dog, make_noise=dog.bark)
    """

    def __init__(self, obj: T, **adapted_methods: Callable):
        """We set the adapted methods in the object's dict."""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object."""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict."""
        return self.obj.__dict__


def main():
    
    objects = []
    dragon = Dragon()
    print(dragon.__dict__)
    
    objects.append(Adapter(dragon, make_noise=dragon.roawr))
    
    print(objects[0].original_dict())
    
    joker = Joker()
    objects.append(Adapter(joker, make_noise=joker.crazy))
    
    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))


    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))
    

if __name__ == "__main__":
    main()