from suds.client import Client
from suds import WebFault
from fixture.project import Project
class SoapHelper:
    def __init__(self,app):
        self.app=app

    def get_project_list(self, username, password):
        client=Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        projects_list=[]
        projects=client.service.mc_projects_get_user_accessible(username,password)
        for element in projects:
            text=element.name
            projects_list.append(Project(name=text))
        return list(projects_list)
