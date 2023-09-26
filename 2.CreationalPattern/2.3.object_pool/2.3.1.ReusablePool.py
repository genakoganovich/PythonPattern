class ReusablePool:
    """
    Класс, который создает экземпляры Reusable и раздает их
    """

    def __init__(self, size):
        """
        Создаем экземляров в количестве size
        """
        self._reusables = [Reusable() for _ in range(size)]

    def acquire(self):
        """
        Отдаем экземпляр и удаляем его из списка свободных
        """
        return self._reusables.pop()

    def release(self, reusable):
        """
        Возвращаем экземпляр обратно в пул
        """
        self._reusables.append(reusable)


class Reusable:
    """
    Класс который делает, что-то долгое, требующее много ресурсов
    """

    pass


def main():
    reusable_pool = ReusablePool(10)
    reusable = reusable_pool.acquire()
    reusable_pool.release(reusable)


if __name__ == "__main__":
    main()
