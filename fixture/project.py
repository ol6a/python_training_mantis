from selenium.webdriver.support.ui import Select
from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def return_to_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Proceed").click()

    def create_project(self, project):
        self.open_project_page()
        self.init_project_creation()
       # self.fill_project_form("11111", "release", "private", "wertyu")
        self.fill_project_form(project)
        self.submit_project_creation()
        self.project_cache=None

    def delete_project(self, name):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_link_text("%s" % name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def submit_project_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        wd.find_element_by_name("status").click()
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_state)
        wd.find_element_by_name("view_state").click()
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    def init_project_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    project_cache = None
    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache=[]
            for element in wd.find_elements_by_xpath("//table[3]//tr[@class='row-1']"):
                cells = element.find_elements_by_tag_name("td")
                text=cells[0].text
                self.project_cache.append(Project(name=text))
            for element in wd.find_elements_by_xpath("//table[3]//tr[@class='row-2']"):
                cells = element.find_elements_by_tag_name("td")
                text=cells[0].text
                self.project_cache.append(Project(name=text))
        return list(self.project_cache)



