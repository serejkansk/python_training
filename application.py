from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def logout(self):
            wd = self.wd
            wd.find_element_by_link_text("Logout").click()

    def retern_to_groups_page(self):
            wd = self.wd
            wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
            wd = self.wd
            self.open_groups_page()
            # init group creation
            wd.find_element_by_name("new").click()
            # fill group firm
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)
            # submit group creation
            wd.find_element_by_name("submit").click()
            self.retern_to_groups_page()

    def create_contact(self, group):
        wd = self.wd
        self.open_add_new_page()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(group.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(group.nickname)
        # submit contact creation
        wd.find_element_by_name("submit").click()

    def open_add_new_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def open_groups_page(self):
            wd = self.wd
            wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
            wd = self.wd
            # login
            self.open_home_page()
            wd.find_element_by_name("user").click()
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys(username)
            wd.find_element_by_name("pass").click()
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys(password)
            wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self):
            wd = self.wd
            # open home page
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()