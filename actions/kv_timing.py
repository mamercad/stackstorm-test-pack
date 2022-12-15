#!/usr/bin/env python3

# import time
from st2common.runners.base_action import Action
from st2client.client import Client
from st2client.models import KeyValuePair

class StatsDCounterAction(Action):
    def run(self, *args, **kwargs):
        client = Client(base_url='http://localhost')
        client.keys.update(KeyValuePair(name='foo', value='bar'))
        return True
