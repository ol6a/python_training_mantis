import random
from model.project import Project

def test_soap_remove_project(app):
    if len(app.soap.get_project_list(username="administrator", password="root"))==0:
        app.project.create_project(Project(name="New Project"))
    old_projects=app.soap.get_project_list(username="administrator", password="root")
    project=random.choice(old_projects)
    app.project.delete_project(project.name)
    new_projects=app.soap.get_project_list(username="administrator", password="root")
    assert len(old_projects)-1==len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.sortname)==sorted(new_projects, key=Project.sortname)
    app.session.logout()