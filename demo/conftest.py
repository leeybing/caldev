# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2022-09-08
from typing import List

import pytest


@pytest.fixture(params=['abc', 'edf'])
def login(request):
    print(request.param)
    yield request.param
    print('关闭浏览器')


# 收集完用后，执行改hook方法
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(type(items))
    print(items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')


def pytest_addoption(parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    mygroup = parser.getgroup('addDev')
    mygroup.addoption('--env',
                      dest='env',
                      action='store',
                      help='set your run env')


@pytest.fixture(scope='function')
def devCmd(request):
    devenv = request.config.getoption('env')
    return devenv


@pytest.fixture()
def cmdopt(pytestconfig):
    # 从配置对象获取cmdopt的值
    return pytestconfig.getoption("env")

