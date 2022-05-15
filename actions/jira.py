#!/usr/bin/env python3

from st2common.runners.base_action import Action
from lib import jira


class TestAction(Action):
    def run(self, *args, **kwargs):
        j = jira.Jira(*args, **kwargs)
