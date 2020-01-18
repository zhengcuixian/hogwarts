#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 0024 下午 9:41
# @Author  : zhengcx
# @File    : test_div.py
from hogwarts.unit.div import div
import pytest

@pytest.mark.happy
def test_div_int():
    assert div(2, 1) == 2

@pytest.mark.happy
def test_div_float():
    assert div(10, 3) == 3.3333333

@pytest.mark.exception
def test_div_expection():
    assert div(10, 'a')

@pytest.mark.exception
def test_div_zero():
    assert div(2, 0) == None


@pytest.mark.happy
@pytest.mark.parametrize("num1, num2, exception", {
    (10, 2, 5),
    (5, 10, 0.5),
    (-10, -2, 5)
})
def test_div_int_param(num1, num2, exception):
    assert div(num1, num2) == exception


@pytest.mark.happy
@pytest.mark.parametrize("num1, num2, exception", {
    (10, 3, 3.33333),
    (1, 3, 0.3),
    (-10, -3, 3.3333)
})
def test_div_float_param(num1, num2, exception):
    assert div(num1, num2) == exception


@pytest.mark.exception
@pytest.mark.parametrize("num1, num2", {
    (8, 'a'),
    ('b', 6),
    ('c', 'd')
})
def test_div_expection_param(num1, num2):
    assert div(num1, num2)


@pytest.mark.exception
@pytest.mark.parametrize("num1, num2,exception", {
    (0, 10, 0),
    (10, 0, None),
    (0, 0, None)
})
def test_div_zero_param(num1, num2,exception):
    assert div(num1, num2) == exception

