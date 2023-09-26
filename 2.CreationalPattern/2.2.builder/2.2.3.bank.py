import abc

class Builder(metaclass=abc.ABCMeta):
    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _nbki_request(self):
        pass

    @abc.abstractmethod
    def _job_call(self):
        pass

    @abc.abstractmethod
    def _property_check(self):
        pass

class Product:
    def __init__(self):
        self.result = [] # ['БКИ проверен', "На работу позвонили", "Недвижимость есть"]

class ConcreteBuilder(Builder):
    #your code here

class Director:
    def construct(self, builder):
    #your code here
