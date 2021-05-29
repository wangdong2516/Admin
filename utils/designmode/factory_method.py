"""
    关于21种设计模式
"""

# 工厂方法模式

from __future__ import annotations
from abc import ABC
from abc import abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        """
            工厂方法，去产生默写特定的产品
        :return:
        """
        pass

    def some_operation(self) -> str:
        """
            自定义操作
        :return:
        """

        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    # 产品共性的方法

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


class ConcreteCreator1(Creator):
    """
        具体的创造者
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct2()


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
