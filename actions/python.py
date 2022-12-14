#!/usr/bin/env python3

from st2common.runners.base_action import Action


class PythonAction(Action):
    def run(self, *args, **kwargs):
        print("Python works!")
        return True, {"foo": "bar"}
