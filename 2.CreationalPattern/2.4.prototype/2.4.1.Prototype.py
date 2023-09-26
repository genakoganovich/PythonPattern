import copy


class Prototype:
    """
    Пример класса, экземпляры которого мы будем копировать
    """

    pass


def main():
    prototype = Prototype()
    prototype_copy = copy.deepcopy(prototype)


if __name__ == "__main__":
    main()
    