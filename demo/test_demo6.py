# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2022-09-08
import pytest


def add(x):
    return x + 1


def test_add(devCmd):
    print(eval(devCmd))

    ss = devCmd.split(',')

    assert int(ss[0]) + int(ss[1]) == 4
