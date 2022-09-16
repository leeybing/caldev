# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2022-09-10

import pytest


@pytest.mark.add
class TestAdd:

    @pytest.mark.P0
    @pytest.mark.parametrize('x,y,result', [[1, 2, 3], [99, 99, 198], [-99, -99, -198]])
    def test_add(self, start_case, x, y, result, add_init, end_all_case):
        res = add_init.add(x, y)
        assert res == result

    @pytest.mark.P1
    @pytest.mark.parametrize('x,y,result', [[100, 100, '参数大小超出范围'], [99, 99, 198], [-99, -99, -198]])
    def test_add_1(self, start_case, x, y, result, add_init, end_all_case):
        res = add_init.add(x, y)
        assert res == result
