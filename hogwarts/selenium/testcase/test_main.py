from hogwarts.selenium.page.main import Main


class TestMain:
    def test_add_memeber(self):
        main = Main()
        main.add_member().add_member("XXXX")
        assert "aaa" in main.ipmort_user().get_message()
