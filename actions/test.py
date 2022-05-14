#!/usr/bin/env python3

from st2common.runners.base_action import Action
from pprint import pprint

class TestAction(Action):
    def run(self, env):
        pprint(env)
