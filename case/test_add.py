# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2022-09-10

import pytest


@pytest.mark.add
@pytest.mark.parametrize('x,y,result', [[1, 2, 3], [99, 99, 198], [-99, -99, -198]])
def test_add(start_case, x, y, result, end_all_case):
    assert x + y == result
