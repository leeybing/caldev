# -*- coding:utf-8 -*-
# autu :liyongbing
# time: 2022-09-10
import pytest
from HDev.tools.read_yaml import read_yaml
import sys


@pytest.mark.cal
@pytest.mark.div
class TestDiv:
    datas = read_yaml('formDatas1.yaml').get(sys._getframe().f_code.co_name).get('datas')
    print(datas)
    P0_datas = datas.get('P0')
    P0_ids = datas.get('P0_ids')
    P1_datas = datas.get('P1')
    P1_ids = datas.get('P1_ids')
    P1_1_datas = datas.get('P1_1')
    P1_1_ids = datas.get('P1_1_ids')

    @pytest.mark.P0
    @pytest.mark.parametrize('x,y,result', P0_datas, ids=P0_ids)
    def test_add(self, start_case, x, y, result, cal_init, end_all_case):
        res = cal_init.div(x, y)
        assert res == result

    @pytest.mark.P1
    @pytest.mark.parametrize('x,y,result', P1_datas, ids=P1_ids)
    def test_add_1(self, start_case, x, y, result, cal_init, end_all_case):
        res = cal_init.div(x, y)
        assert res == result

    @pytest.mark.P1_1
    @pytest.mark.parametrize('x,y,result', P1_1_datas, ids=P1_1_ids)
    def test_add_4(self, start_case, cal_init, end_all_case, x, y, result):
        # 异常捕获
        with pytest.raises(eval(result)) as e:
            cal_init.div(x, y)
        assert result == e.typename
