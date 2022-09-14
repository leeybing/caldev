# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2022-09-08
import pytest
import allure


def test_add3():
    assert 1 == 1


def test_add4():
    assert 1 == 1


@pytest.mark.amoke
def test_add5():
    assert 1 == 2


def test_add6():
    assert 1 == 1


@allure.epic('登录王大鹏')
@allure.feature('登录测试')
@pytest.mark.add
class TestA:
    @allure.story('add测试')
    @allure.link('bug管理')
    def test_add7(self):
        with allure.step('打开页面'):
            print('打开页面')
        with allure.step('登录操作'):
            print('登录操作')

        with allure.step('输入用户名'):
            print('输入用户名')

        with allure.step('输入密码'):
            print('输入密码')

        with allure.step('点击登录'):
            print('点击登录')
            assert 1 == 2

    @allure.story('update测试')
    def test_add8(self):
        assert 1 == 1

    @allure.story('query测试')
    def test_add9(self):
        assert 1 == 2

    @allure.story('delete测试')
    def test_add10(self):
        assert 1 == 1

    @pytest.mark.skipif(1 == 1, reason='不想执行')
    def test_add11(self):
        assert 1 == 1


@pytest.mark.parametrize('x,y,z', ((1, 2, 2), (1, 2, 3), (1, 3, 3), (1, 4, 4)), ids=['a', 'b', 'c', 'd'])
def test_add122(x, y, z):
    a = x * y
    assert a == z


if __name__ == '__main__':
    pytest.main(['-vs', 'test_demo2.py'])
