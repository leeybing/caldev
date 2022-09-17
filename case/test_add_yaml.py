# # -*- coding:utf-8 -*-
# # autu :liyongbing
# # time: 2022-09-10
#
# import pytest
# # from HDev.tools import read_yaml
# from HDev.tools.read_yaml import read_yaml
#
# #
# # def get_data_by_mark(type_data, file, mark_data):
# #     data = read_yaml(type_data, file).get(mark_data)
# #     # print(data)
# #     return data
#
#
# @pytest.mark.add1
# class TestAdd:
#
#     @pytest.mark.P0
#     @pytest.mark.parametrize('x,y,result', get_data_by_mark('add', 'formDatas.yaml', 'P0'))
#     def test_add(self, start_case, x, y, result, cal_init, end_all_case):
#         res = cal_init.add(x, y)
#         assert res == result
#
#     @pytest.mark.P1
#     @pytest.mark.parametrize('x,y,result', get_data_by_mark('add', 'formDatas.yaml', 'P1'))
#     def test_add_11(self, start_case, x, y, result, cal_init, end_all_case):
#         res = cal_init.add(x, y)
#         assert res == result
