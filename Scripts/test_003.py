import allure

class Test_002:
    @allure.severity(allure.severity_level.BLOCKER)
    def test_oo2_1(self):
        print('\ntest_oo2_1')
        assert True

    @allure.severity(allure.severity_level.CRITICAL)
    def test_oo2_2(self):
        print('\ntest_oo2_1')
        assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_oo2_3(self):
        print('\ntest_oo2_1')
        assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_oo2_4(self):
        print('\ntest_oo2_1')
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_oo2_5(self):
        print('\ntest_oo2_1')
        assert False