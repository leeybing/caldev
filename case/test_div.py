# # -*- coding:utf-8 -*-
# # autu :liyongbing
# # time: 2022-09-10
# import pytest
#
#
# @pytest.mark.div
# class TestDiv:
#
#     @pytest.mark.P0
#     @pytest.mark.parametrize('x,y,result', [[99, 1, 99], [0, 99, 0], [0, -99, 0]])
#     def test_add(self, start_case, x, y, result, cal_init, end_all_case):
#         res = cal_init.div(x, y)
#         assert res == result
#
#     @pytest.mark.P1
#     @pytest.mark.parametrize('x,y,result', [[100, 100, '参数大小超出范围'], [99, 99, 198], [-99, -99, -198]])
#     def test_add_1(self, start_case, x, y, result, cal_init, end_all_case):
#         res = cal_init.div(x, y)
#         assert res == result
#
#     @pytest.mark.P1_1
#     @pytest.mark.parametrize('x,y,result', [['忘', 2, 'TypeError'], [1, 0, 'ZeroDivisionError']])
#     def test_add_4(self, start_case, cal_init, end_all_case, x, y, result):
#         # 异常捕获
#         with pytest.raises(eval(result)) as e:
#             cal_init.div(x, y)
#         assert result == e.typename
