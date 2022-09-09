# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2022-09-08
import pytest


# @pytest.fixture()
def test_add(login):
    print(f'加入购物车{login[0]}')



def test_add2(login):
    print(f'下单操作2{login[0]}')
