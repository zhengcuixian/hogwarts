#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 0024 上午 7:28
# @Author  : zhengcx
# @File    : unit_demo.py
import unittest


class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def tearDown(self):
        print("tearDown")


    def test_sum(self):
        x = 1 + 2
        print(x)
        self.assertEqual(3, x, f'x={x} expection=3')

    def test_demo(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
