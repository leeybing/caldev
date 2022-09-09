# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2022-09-10

import pytest


@pytest.fixture()
def start_case():
    print('开始执行用例')
    yield
    print('用例执行完毕')


@pytest.fixture(scope='session')
def end_all_case():
    yield
    print('所有用例执行完毕')


@pytest.fixture()
def add(x, y):
    return x + y
