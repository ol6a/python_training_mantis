import pytest
import random
import string
from model.project import Project

def random_string_name(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_status():
    status = ['development', 'release', 'stable', 'obsolete']
    return random.choice(status)

def random_string_view_state():
    view_state = ['public', 'private']
    return random.choice(view_state)

def random_string_description(maxlen):
    symbols = string.ascii_letters + string.digits + ""*15 + string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata =[
    Project(name=random_string_name(20), status=random_string_status(), view_state=random_string_view_state(),
            description=random_string_description(30)
            )
    for i in range(1)
]

@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])

def test_add_project(app, project):
    #old_projects=app.soap.get_project_list(config['webadmin']["username"], config['webadmin']["password"])
    old_projects = app.soap.get_project_list(username="administrator", password="root")
    app.project.create_project(project)
    app.project.return_to_project_page()
    new_projects=app.soap.get_project_list(username="administrator", password="root")
    #new_projects=app.soap.get_project_list(config['webadmin']["username"], config['webadmin']["password"])
    #assert len(old_projects)+1==len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.sortname)==sorted(new_projects, key=Project.sortname)
    app.session.logout()