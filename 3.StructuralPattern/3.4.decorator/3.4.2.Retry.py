class Retry(Foo):
    def __init__(self, foo):
        self.foo = foo

    def one_try(self, n):
        for _ in range(n):
            self.foo.one_try()
