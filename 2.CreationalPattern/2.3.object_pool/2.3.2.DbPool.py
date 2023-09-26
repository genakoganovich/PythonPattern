class DbPool:
    # your code here
    def __init__(self, size=10):
        """
        Создаем экземляров в количестве size
        """
        self._connections = size

    def acquire(self):
        """
        Отдаем экземпляр и удаляем его из списка свободных
        """
        if self._connections:
            self._connections -= 1
            return f'Доступы выданы, осталось подключений: {self._connections}'
        else:
            return 'no resources'

    def release(self, connection):
        """
        Возвращаем экземпляр обратно в пул
        """
        self._connections += 1


class DbConnection:
    pass
