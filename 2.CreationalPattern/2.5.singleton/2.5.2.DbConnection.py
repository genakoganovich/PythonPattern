class Singleton(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
            print('Вы подключились к базе данных')
        else:
            print('Существует активное подключение')
        return cls._instance


class DbConnection(metaclass=Singleton):
    pass
