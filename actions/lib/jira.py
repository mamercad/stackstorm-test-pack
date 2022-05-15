class Jira(object):
    def __init__(self, *args, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        api_token = kwargs.get("api_token")
        create = kwargs.get("create")
        comment = kwargs.get("comment")

    def create(self):
        print("create")

    def comment(self):
        print("comment")
