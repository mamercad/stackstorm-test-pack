#!/usr/bin/env python3

import time
from st2common.runners.base_action import Action
from statsd_client import StatsDClient


class PythonAction(Action):
    def run(self, *args, **kwargs):
        print("Python works!")
        statsd = StatsDClient()
        statsd.incr(counter="foo")
        time.sleep(2)
        statsd.timing(timer="foo")
        return True, {"foo": "bar"}
k
