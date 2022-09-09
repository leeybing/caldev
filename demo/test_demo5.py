# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2022-09-08
import pytest
import logging
import time


def add(x):
    return x + 1


@pytest.mark.run(order=3)
@pytest.mark.get
def check_add():
    time.sleep(1)
    logging.info('用例1测试')
    logging.info('用例1步骤测试')
    assert add(3) == 3


@pytest.mark.run(order=22)
@pytest.mark.update
def check_add2():
    time.sleep(1)
    logging.info('用例2测试')
    logging.info('用例2步骤测试')
    assert add(3) == 4


@pytest.mark.run(order=1)
@pytest.mark.add
class CheckA:

    def test_add33(self):
        time.sleep(1)
        logging.info('用例3测试')
        logging.info('用例3步骤测试')
        assert 1 == 1

    @pytest.mark.parametrize('a', ['自动化测试', '测试开发'])
    def test_add44(self,a):
        logging.info(f'用例3测试--{a}')
        logging.info(f'用例3步骤测试--{a}')
        print(a)
        assert 1 == 1



if __name__ == '__main__':
    pytest.main(['-vs', 'test_demo.py'])
