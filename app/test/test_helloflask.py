import pytest

class ExampleClass():
    def __init__(self):
        self.attribute = "class attribute"

class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = ExampleClass()
        assert hasattr(x, 'attribute')
        assert x.attribute == "class attribute"
