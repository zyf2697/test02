import allure


class TestLogin:
    def test_a(self):
        print("\n111")
        assert 1

    @allure.step("测试步骤001")
    def test_b(self):
        print("\naaa")
        allure.attach('描述1','请输入用户名')
        print("\nbbbb")
        allure.attach('描述2','请输入密码')
        assert 0
