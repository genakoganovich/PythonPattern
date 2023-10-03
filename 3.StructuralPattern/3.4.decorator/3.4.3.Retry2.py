class Foo:
    def one_try(self, n):
        pass


class Retry(Foo):
    def __init__(self, foo):
        self.foo = foo

    def one_try(self, n):
        for _ in range(n):
            try:
                self.foo.one_try()
                break
            except FooError:
                pass
        else:
            print('no success')
