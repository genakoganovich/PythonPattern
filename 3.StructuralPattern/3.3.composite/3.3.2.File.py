from abc import ABC, abstractmethod

# your code here
import abc


class Component(metaclass=abc.ABCMeta):
    """
    Абстракция для определения единого общего метода
    """

    @abc.abstractmethod
    def display(self, prev=''):
        pass


class File(Component):
    def __init__(self, name):
        self.name = name
        self.is_directory = False

    def display(self, prev=''):
        print(f'{prev}|- {self.name}')


class Directory(Component):
    def __init__(self, name):
        self.name = name
        self.is_directory = True
        self.children = set()

    def add_child(self, child):
        self.children.add(child)

    def display(self, prev=''):
        print(f'{prev}{self.name}')
        for child in sorted(self.children, key=lambda x: (x.is_directory, x.name)):
            child.display(f'{prev}|  ')


class Client:
    def __init__(self, component):
        self.component = component

    def display(self):
        self.component.display()


"""
Пример теста
root = Directory("root")
file1 = File("file1")
file2 = File("file2")
dir1 = Directory("dir1")
file3 = File("file3")
file4 = File("file4")
dir2 = Directory("dir2")
file5 = File("file5")
file6 = File("file6")
dir3 = Directory("dir3")
file7 = File("file7")
file8 = File("file8")
root.add_child(file1)
root.add_child(file2)
root.add_child(dir1)
dir1.add_child(file3)
dir1.add_child(file4)
dir1.add_child(dir2)
dir2.add_child(file5)
dir2.add_child(file6)
root.add_child(dir3)
dir3.add_child(file7)
dir3.add_child(file8)
client = Client(root)
client.display()
"""
