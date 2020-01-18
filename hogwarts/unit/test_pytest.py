#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 0024 上午 7:38
# @Author  : zhengcx
# @File    : test_pytest.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5

def setup_module():
    print("setup module")

def setup_function():
    print("setup function")

class TestClass:

    def setup(self):
        print("setup")

    @classmethod
    def setup_class(cls):
        print("setup class")

    def test_one(self):
        x="this"
        assert "h" in x

    def test_two(self):
        x="hello"
        assert hasattr(x, "hello")






