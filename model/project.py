class Project:
    def __init__(self, name, status=None, view_state=None, description=None):
        self.name=name
        self.status=status
        self.view_state=view_state
        self.description=description

    def __repr__(self):
        return "%s" % (self.name)

    def __eq__(self,other):
        return self.name==other.name

    def sortname(self):
        if self.name:
            return self.name

