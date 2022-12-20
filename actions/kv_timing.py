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
        epoch_now = int(time.time())

        if start:
            client.keys.update(KeyValuePair(name=name, value=str(epoch_now)))
            return True, {"epoch_now": epoch_now}

        key_pair = client.keys.get_by_name(name=name)
        epoch_start = key_pair.value
        duration_seconds = int(epoch_now - int(epoch_start))
        client.keys.delete(key_pair)
        return True, {"duration_seconds": duration_seconds}
