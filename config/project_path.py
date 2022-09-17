# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/8/21
import os.path
import os

# from Tools import logger

# 当前路径
cur_path = os.path.abspath(os.path.dirname(__file__))

# 项目所在根目录
project_path = cur_path[:cur_path.rfind("HDev") + len("HDev")]


# config
def config_path():
    return os.sep.join([project_path, 'config'])


# config
def dates_path():
    return os.sep.join([project_path, 'dates'])

print(config_path())


# 日志目录路径
def log_path():
    return os.sep.join([project_path, 'Log'])


# 日志目录路径
def log_file(source_file):
    return os.sep.join([log_path(), f"{source_file}"])


# # Common/Config文件路径
# def common_config_path():
#     return os.sep.join([common_path(), 'Config'])
#
#
# # 资源Source目录路径
# def source_catalog():
#     # return Path(report(), file_path)
#     return os.sep.join([common_path(), 'Source'])
#
#
# # 谷歌驱动文件
#
# def chrome_driver():
#     return os.sep.join([common_path(), 'Driver', 'chromedriver.exe'])
#

# print(chrome_driver())

# 资源文件路径
# def source_path(source_file):
#     return os.sep.join([source_catalog(), f"{source_file}"])


# # DBsource文件路径
# def DBsource_path(source_file):
#     return os.sep.join([common_path(), 'DBSource', f"{source_file}"])
#
#
# # 配置文件路径#####
# def config_path(file_path):
#     return os.sep.join([source_catalog(), f"{file_path}"])
#
#
# # 填报预置数据文件目录路径
# def base_formData():
#     return os.sep.join([common_path(), "BaseData"])


# 填报预置数据文件路径
def base_form_data_path(file_path):
    return os.sep.join([dates_path(), f"{file_path}"])



# c20,Case目录
def case():
    return os.sep.join([project_path, 'Case'])


# Case/TestCase测试用例
def case_path():
    return os.sep.join([case(), 'V8R4C20', 'TestCase'])


def case_path_C50():
    return os.sep.join([case(), 'V8R4C50', 'TestCase'])


# conftest文件路径
def conftest_path():
    return os.sep.join([project_path, 'Case', 'conftest.py'])
    # return os.path.join(case(), 'conftest.py')


# 业务流测试用例模板文件夹
def flow_base_case_path():
    return os.sep.join([case_path(), 'Sdata_flow'])


# C50业务流测试用例模板文件夹
def flow_base_case_path_C50():
    return os.sep.join([case_path_C50(), 'Sdata_flow'])


# 生成业务流测试用例文件夹
def flow_case_path(name):
    """
    动态生成测试用例目录
    """
    return os.sep.join([flow_base_case_path(), name])


# 生成业务流测试用例文件夹
def create_flow_file_path(path):
    root_path = generate_all_case_path()
    file_ath = os.sep.join([root_path, path])
    if not os.path.exists(file_ath):
        os.makedirs(file_ath)


# 生成业务流测试用例文件夹
def create_flow_file_path_C50(path):
    root_path = generate_all_case_path()
    file_ath = os.sep.join([root_path, path])
    if not os.path.exists(file_ath):
        os.makedirs(file_ath)


# 生成填报测试用例文件夹
def flow_case(id, name_id):
    """
    动态生成测试用例目录
    """
    create_flow_file_path(id)
    return os.sep.join([all_case_path(id), f'{name_id}.py'])


# 生成填报测试用例文件夹
def flow_case_C50(id, name_id):
    """
    动态生成测试用例目录
    """
    create_flow_file_path_C50(id)
    return os.sep.join([all_case_path(id), f'{name_id}.py'])


# 业务流测试模板名称
def flow_test_name_path():
    return os.sep.join([flow_base_case_path(), 'test_flowPath.py'])


# C50业务流测试模板名称
def flow_test_name_path_C50():
    return os.sep.join([flow_base_case_path_C50(), 'test_flowPath.py'])


# 填报测试用例模板文件夹
def form_base_path():
    return os.sep.join([case_path(), 'Sdata_form'])
    # return os.path.join(project_path, case_path(), 'Sdata_form/')


# 生成填报测试用例文件夹
def form_case_path(name):
    """
    动态生成测试用例目录
    """
    return os.sep.join([form_base_path(), name])


# 生成填报测试用例文件夹
def all_case_path(name):
    """
    动态生成测试用例目录
    """
    return os.sep.join([generate_all_case_path(), name])


# 生成填报测试用例文件夹
def all_case_path_C50(name):
    """
    动态生成测试用例目录
    """
    return os.sep.join([generate_all_case_path(), name])


# 生成填报测试用例文件夹
def form_case(id, name_id):
    """
    动态生成测试用例目录
    """
    create_file_path(id)
    return os.sep.join([all_case_path(id), f'{name_id}.py'])


# 生成C50版本填报测试用例文件夹
def form_case_C50(id, name_id):
    """
    动态生成测试用例目录
    """
    create_file_path_C50(id)
    return os.sep.join([all_case_path_C50(id), f'{name_id}.py'])


# 生成填报测试用例文件夹
def create_file_path(path):
    root_path = generate_all_case_path()
    file_ath = os.sep.join([root_path, path])
    if not os.path.exists(file_ath):
        os.makedirs(file_ath)


# 生成C50填报测试用例文件夹
def create_file_path_C50(path):
    root_path = generate_all_case_path()
    file_ath = os.sep.join([root_path, path])
    if not os.path.exists(file_ath):
        os.makedirs(file_ath)


# 填报新增测试模板名称
def form_test_name_path():
    return os.path.join(project_path, case_path(), 'Sdata_form/', 'test_form_operate_case.py')


# C50版本填报新增测试模板名称
def form_test_name_path_C50():
    return os.path.join(project_path, case_path_C50(), 'Sdata_form/', 'test_form_operate_case.py')


# 填报删除测试模板名称
def form_del_test_name_path():
    return os.path.join(project_path, case_path(), 'Sdata_form/', 'test_form_del.py')


# 填报修改测试模板名称
def form_update_test_name_path():
    return os.path.join(project_path, case_path(), 'Sdata_form/', 'test_form_update.py')


# 所有生成用例存在的目录
def generate_all_case_path():
    return os.sep.join([case(), 'Temp', 'Sdata_generate_case'])


# 测试报告路径
def report():
    return os.sep.join([case(), 'Temp', 'Report'])


# 报告目录
def report_path(file_path):
    return os.sep.join([report(), file_path])


# pytest生成report路径
def generate_report_path(file_path):
    return os.sep.join([report_path(file_path), 'report'])


# pytest生成report，index.html路径
def generate_html_path(file_path):
    return os.sep.join([generate_report_path(file_path), 'index.html'])


# pytest生成result路径
def generate_result_path(file_path):
    return os.sep.join([report_path(file_path), 'result'])


# allure临时文件history目录
def history_path(file_path):
    return os.sep.join([generate_report_path(file_path), 'history'])


# allure临时文件data目录
def data_path(file_path):
    return os.sep.join([generate_report_path(file_path), 'data'])


# allure临时文件history-trend.json文件路径
def history_trend_path(file_path):
    return os.sep.join([history_path(file_path), 'history-trend.json'])


def history_file_path(file_path):
    return os.sep.join([history_path(file_path), 'history.json'])


# allure临时文件history-trend.json文件路径
def data_suites_path(file_path):
    return os.sep.join([data_path(file_path), 'suites.json'])


if __name__ == '__main__':
    res = flow_base_case_path()
    print('11', res)
