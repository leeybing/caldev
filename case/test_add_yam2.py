# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2022-09-10

import pytest
# from HDev.tools import read_yaml
from HDev.tools.read_yaml import read_yaml
import sys


@pytest.mark.cal
@pytest.mark.add33
class TestAdd:
    # def get_data_by_mark(type_data, file, mark_data):
    #     # yaml已类名命令键，动态获取键当前类名来获取数据
    #     data = read_yaml(file).get(sys._getframe().f_code.co_name)
    #     # print(data)
    #     return data
    datas = read_yaml('formDatas1.yaml').get(sys._getframe().f_code.co_name).get('datas')
    print(datas)
    P0_datas = datas.get('P0')
    P0_ids = datas.get('P0_ids')
    P1_datas = datas.get('P1')
    P1_ids = datas.get('P1_ids')

    @pytest.mark.P0
    @pytest.mark.parametrize('x,y,result', P0_datas, ids=P0_ids)
    def test_add222(self, start_case, x, y, result, cal_init, end_all_case):
        res = cal_init.add(x, y)
        assert res == result

    @pytest.mark.P1
    @pytest.mark.parametrize('x,y,result', P1_datas, ids=P1_ids)
    def test_add_123(self, start_case, x, y, result, cal_init, end_all_case):
        res = cal_init.add(x, y)
        assert res == result
