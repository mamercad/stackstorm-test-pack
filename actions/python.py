#!/usr/bin/env python3

import time
from st2common.runners.base_action import Action
from statsd_client import StatsDClient


class PythonAction(Action):
    def run(self, *args, **kwargs):
        print("Python works!")
        statsd = StatsDClient()
        statsd.incr(counter="foo1")
        time.sleep(2)
        statsd.timing(stat="foo2")
        statsd.gauge(stat="foo3")
        return True, {"foo": "bar"}
