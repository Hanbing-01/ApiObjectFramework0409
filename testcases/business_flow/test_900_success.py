import time

import allure
import javaobj
import jsonpath
import pytest
import requests

# 基础配置（你的域名）

@allure.epic('主流程测试')
@allure.feature('订单流程测试')
class TestBankLoginCookie:
    """银行登录接口（Cookie模式）测试用例"""

    @allure.title('执行成功01')
    def test_01_login_success(self):
        """用例1：正确账号密码登录，成功获取Cookie"""
        url  = "http://14.29.184.142:8090/pinter/bank/api/login"
        data = {
            "userName": "admin",
            "password": "1234"
        }

        # 发送POST请求
        resp = requests.post(url, data=data)

        # 1. 断言状态码为200
        assert resp.status_code == 200, "请求失败，状态码非200"

    @allure.title('执行成功02')
    def test_02_login_wrong_password(self):
        """用例2：账号正确、密码错误，登录失败"""
        url  = "http://14.29.184.142:8090/pinter/bank/api/login"
        data = {
            "userName": "admin",
            "password": "wrongpass"
        }

        resp = requests.post(url, data=data)

        assert resp.status_code == 200
        print("❌ 密码错误响应:", resp.text)
