#!/usr/bin/env python3

import time
from st2common.runners.base_action import Action
from st2client.client import Client
from st2client.models import KeyValuePair

class StatsDCounterAction(Action):
    def run(self, *args, **kwargs):
        client = Client(base_url='http://localhost')

        name = kwargs.get("name")
        start = kwargs.get("start")
        epoch_now = time.time()

        if start:
            client.keys.update(KeyValuePair(name=name, value=epoch_now))
            return True, {"epoch_now": epoch_now}

        epoch_start = client.keys.get_by_name(name=name).value
        duration_seconds = epoch_now - epoch_start
        client.keys.delete(epoch_start)
        return True, {"duration_seconds": duration_seconds}
