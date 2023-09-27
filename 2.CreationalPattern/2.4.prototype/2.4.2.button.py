import copy


class Button:
    def __init__(self, os, button_type):
        if os == 'Windows':
            self.colour = 'синий'
        else:
            self.colour = 'белый'

        self.button_type = button_type

        if self.button_type == 'Чекбокс':
            self.message = f'Галочка поставлена, цвет {self.colour}'
        else:
            self.message = f'На кнопку нажали, цвет {self.colour}'

    def push(self):
        print(self.message)


win_checkbox = Button('Windows', 'Чекбокс')
win_pushbutton = Button('Windows', 'Кнопка Нажатия')
mac_checkbox = Button('Mac', 'Чекбокс')
mac_pushbutton = Button('Mac', 'Кнопка Нажатия')
