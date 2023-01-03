#!/usr/bin/env python3

import time
from st2common.runners.base_action import Action


class HelloAction(Action):
    def run(self):
        return (True, {"epoch": time.time()})
