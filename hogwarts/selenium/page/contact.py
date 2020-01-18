from selenium.webdriver.common.by import By


class Contact:
    _add_member_button = (By.CSS, "xxx")
    def add_member(self):
        self.driver.find_element("添加成员").click
        #sendkeys
        #click save
        return self

    def add_memeber_error(self, data):
        #return AddMemeberPage()
        pass

    def search(self, name):
        pass

    def import_users(self, data):
        pass

    def export_users(self):
        pass

    def set_department(self, data):
        pass

    def delete(self):
        pass

    def invite(self):
        pass

    def add_department(self):
        pass