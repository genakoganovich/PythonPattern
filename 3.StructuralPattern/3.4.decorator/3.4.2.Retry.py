import sys
import io
import random


class Foo:
    def one_try(self, n):
        pass


class Retry(Foo):
    def __init__(self, foo):
        self.foo = foo

    def one_try(self, n):
        for _ in range(n):
            output_stream = sys.stdout
            sys.stdout = io.StringIO()
            self.foo.one_try()
            output = sys.stdout.getvalue()
            sys.stdout = output_stream
            print(output)

            if output.rstrip() == 'Success try':
                break
        else:
            print('no success')
