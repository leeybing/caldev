# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2022-09-08
import pytest


def add(x):
    return x + 1


@pytest.mark.parametrize('a', ['自动化测试', '测试开发'])
def test_add(a):
    assert add(3) == 4


def test_add2():
    assert add(3) == 5


if __name__ == '__main__':
    pytest.main(['-vs', 'test_demo3.py'])
