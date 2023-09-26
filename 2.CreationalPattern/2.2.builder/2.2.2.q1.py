from abc import ABCMeta, abstractmethod


class IBuilder(metaclass=ABCMeta):
    "Абстрактный строитель бургеров"

    @staticmethod
    @abstractmethod
    def build_part_a():
        "Build part a"

    @staticmethod
    @abstractmethod
    def build_part_b():
        "Build part b"

    @staticmethod
    @abstractmethod
    def build_part_c():
        "Build part c"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"


class Builder(IBuilder):
    "Строитель бургера с говяжьей котлеткой, помидором и кетчупом"

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append('Говяжья котлетка')
        return self

    def build_part_b(self):
        self.product.parts.append('Помидор')
        return self

    def build_part_c(self):
        self.product.parts.append('Кетчуп')
        return self

    def get_result(self):
        return self.product


class Product():
    "Бургер"

    def __init__(self):
        self.parts = []


class Director:
    "Директор"

    def construct(self, builder):
        "Метод, который запускает строителя"
        builder.build_part_a()
        builder.build_part_b()
        builder.build_part_c()
        builder.get_result()
        return builder.product


director = Director()
builder = Builder()
PRODUCT = director.construct(builder)
print(PRODUCT.parts)
