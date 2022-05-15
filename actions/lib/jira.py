from jira import JIRA

class Jira(object):
    def __init__(self, *args, **kwargs):
        self.endpoint = kwargs.get("endpoint")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.api_token = kwargs.get("api_token")
        self.create = kwargs.get("create")
        self.comment = kwargs.get("comment")

        if self.username and self.api_token:
            self.jira = JIRA(self.endpoint, auth=(self.username, self.api_token))

        if self.username and self.password:
            self.jira = JIRA(self.endpoint, auth=(self.username, self.password))

    def create(self):
        print("create")
        self.jira.create_issue(
            project=self.create.get("project"),
            summary=self.create.get("summary"),
            description=self.create.get("description"),
            issuetype=self.create.get("issuetype"),
        )

    def comment(self):
        print("comment")
        self.jira.comment(
            ticket=self.comment.get("ticket"),
            comment=self.comment.get("comment"),
        )
