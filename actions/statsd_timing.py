#!/usr/bin/env python3

from st2common.runners.base_action import Action
from statsd_client import StatsDClient


class StatsDCounterAction(Action):
    def run(self, *args, **kwargs):
        name = kwargs.get("name")
        delta = kwargs.get("delta")

        statsd = StatsDClient()
        statsd.timing(stat=name, delta=delta)

        return True
