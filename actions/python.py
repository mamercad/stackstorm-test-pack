#!/usr/bin/env python3

from st2common.runners.base_action import Action
from lib.statsd_client import StatsDClient


class PythonAction(Action):
    def run(self, *args, **kwargs):
        print("Python works!")
        statsd = StatsDClient()
        statsd.emit()
        return True, {"foo": "bar"}
