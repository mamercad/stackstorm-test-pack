#!/usr/bin/env python3

import time
from st2common.runners.base_action import Action
from statsd_client import StatsDClient


class StatsDCounterAction(Action):
    def run(self, *args, **kwargs):
        name = kwargs.get("name")

        statsd = StatsDClient()
        statsd.incr(counter=name)

        return True
