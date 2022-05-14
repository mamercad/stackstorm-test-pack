#!/usr/bin/env python3

from st2common.runners.base_action import Action
from awx import AWX


class AWXJTAction(Action):
    def run(self, tower_host, tower_oauth_token, job_template_id, inventory_id, limit):
        a = AWX(tower_host, tower_oauth_token, job_template_id, inventory_id, limit)
        a.ping()
        a.launch()
        a.poll()
        a.summary()
