# -*- coding: utf-8 -*-

from base.action import ElementActions
from page.pages import *
from test.steps import Steps
from utils import L


class TestLogin:
    def test_login(self, action: ElementActions):
        L.d('test_login')
        account = Steps.get_account()
        action.sleep(3)
        # action.test_SwipeGuideImages()
        action.click(HomePage.登录入口)
        action.text(LoginPage.账户, account[0])
        action.text(LoginPage.密码, account[1])
        action.sleep(1)
        action.click(LoginPage.登录)
        action.sleep(3)
        assert action._find_text_in_page("我的")
