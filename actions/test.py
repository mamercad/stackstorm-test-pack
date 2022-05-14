#!/usr/bin/env python3

from st2common.runners.base_action import Action
import os


class TestAction(Action):
    def run(self, *args, **kwargs):
        print(os.environ)
