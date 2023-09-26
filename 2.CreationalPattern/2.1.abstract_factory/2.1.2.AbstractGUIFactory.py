import abc


class AbstractGUIFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_button(self):
        pass

    @abc.abstractmethod
    def create_checkbox(self):
        pass


class WinFactory(AbstractGUIFactory, abc.ABC):
    def create_button(self):
        return PushButton('синий')

    def create_checkbox(self):
        return Checkbox('синий')


class MacFactory(AbstractGUIFactory, abc.ABC):
    def create_button(self):
        return PushButton('белый')

    def create_checkbox(self):
        return Checkbox('белый')


class AbstractButton(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, colour):
        self.colour = colour

    @abc.abstractmethod
    def push(self):
        pass


class Checkbox(AbstractButton, abc.ABC):
    def __init__(self, colour):
        # AbstractButton.__init__(self, colour)
        super().__init__(colour)

    def push(self):
        print(f'Галочка поставлена, цвет {self.colour}')


class PushButton(AbstractButton, abc.ABC):
    def __init__(self, colour):
        # AbstractButton.__init__(self, colour)
        super().__init__(colour)

    def push(self):
        print(f'На кнопку нажали, цвет {self.colour}')
