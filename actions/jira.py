#!/usr/bin/env python3

from st2common.runners.base_action import Action
from lib import jira


class TestAction(Action):
    def run(self, *args, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        api_token = kwargs.get("api_token")
        create = kwargs.get("create")
        comment = kwargs.get("comment")

        j = jira.Jira(*args, **kwargs)

        if create:
            j.create()

        if comment:
            j.comment()
