"""
    设计模式二:
        抽象工厂模式

        抽象工厂模式是一种创建型设计模式， 它能创建一系列相关的对象， 而无需指定其具体类

        抽象工厂模式建议为系列中的每件产品明确声明接口
        确保所有产品变体都继承这些接口
"""

from __future__ import annotations
from abc import ABC
from abc import abstractmethod


class AbstractFactory(ABC):
    """
        抽象工厂接口类
    """

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
        具体的工厂类1

        生产A1产品和B1产品
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
        具体的工厂类2

        生产A2产品和B2产品
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
        A产品抽象接口类
    """
    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    """
        A1产品
    """
    def useful_function_a(self) -> str:
        return "A1产品的功能"


class ConcreteProductA2(AbstractProductA):
    """
        A2产品
    """
    def useful_function_a(self) -> str:
        return "A2产品的功能"


class AbstractProductB(ABC):
    """
        B产品抽象接口类
    """

    @abstractmethod
    def useful_function_b(self) -> None:

        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:

        pass


class ConcreteProductB1(AbstractProductB):
    """
        B1产品类
    """
    def useful_function_b(self) -> str:
        return "B1产品的功能1."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"B1产品的另一个功能 ({result})"


class ConcreteProductB2(AbstractProductB):
    """
        B2产品类
    """

    def useful_function_b(self) -> str:
        return "B2产品的功能"

    def another_useful_function_b(self, collaborator: AbstractProductA):

        result = collaborator.useful_function_a()
        return f"B2产品的另一个功能({result})"


def client_code(factory: AbstractFactory) -> None:
    """
        客户端调用的代码  封装了客户端调用的逻辑
    :param factory: 抽象工厂类
    :return:
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


print("Client: Testing client code with the first factory type:")
client_code(ConcreteFactory1())

print("\n")

print("Client: Testing the same client code with the second factory type:")
client_code(ConcreteFactory2())
