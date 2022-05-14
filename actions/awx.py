#!/usr/bin/env python3

import json
import os
import requests
import time
import logging

from st2common.runners.base_action import Action


class AWX(object):
    def __init__(
        self, tower_host, tower_oauth_token, job_template_id, inventory_id, limit
    ) -> None:
        self.tower_host = tower_host
        self.tower_oauth_token = tower_oauth_token
        self.job_template_id = job_template_id
        self.inventory_id = inventory_id
        self.limit = limit
        self.headers = {
            "Authorization": f"Bearer {self.tower_oauth_token}",
            "Content-type": "application/json",
        }

    def ping(self):
        r = requests.get(url=self.tower_host)
        if r.status_code != 200:
            raise RuntimeError(f"Couldn't ping AWX; status code is {r.status_code}")
        logging.debug(f"Hello from AWX at {self.tower_host}")

    def launch(self):
        r = requests.post(
            url=self.tower_host
            + f"/api/v2/job_templates/{self.job_template_id}/launch/",
            json={
                "inventory": self.inventory_id,
                "limit": self.limit,
            },
            headers=self.headers,
        )
        if r.status_code != 201:
            raise RuntimeError(f"Didn't launch AWX job; status code is {r.status_code}")

        job_id = r.json().get("job")
        if not job_id:
            raise RuntimeError(f"Didn't get a job ID or URL")

        self.job_id = job_id
        logging.debug(
            f"Launched job template {self.job_template_id} (inventory {self.inventory_id}, limit '{self.limit}'); job ID is {self.job_id}"
        )

    def poll(self):
        finished = False
        while not finished:
            r = requests.get(
                url=self.tower_host + f"/api/v2/jobs/{self.job_id}",
                headers=self.headers,
            )
            if r.status_code != 200:
                raise RuntimeError(f"Couldn't poll job; status code is {r.status_code}")
            j = r.json()
            finished = r.json().get("finished")
            elapsed = r.json().get("elapsed")
            status = r.json().get("status")
            logging.debug(f"Polling job {self.job_id}: {status}, {elapsed}s elapsed")
            time.sleep(1)

    def summary(self):
        next = f"/api/v2/jobs/{self.job_id}/job_host_summaries/?page_size=1"
        self.results = {}
        while next:
            r = requests.get(url=self.tower_host + next, headers=self.headers)
            if r.status_code != 200:
                raise RuntimeError(
                    f"Couldn't get job host summary; status code is {r.status_code}"
                )
            j = r.json()
            next = j.get("next")
            results = j.get("results")
            for result in results:
                status = "failed" if result.get("failed") else "passed"
                hostname = result.get("host_name")
                logging.debug(f"{hostname} {status}")
                self.results[hostname] = status
        print(json.dumps(self.results))


class AWXAction(object):
    def run(
        self,
        tower_host,
        tower_oauth_token,
        job_template_id,
        inventory_id,
        limit,
    ):
        a = AWX(tower_host, tower_oauth_token, job_template_id, inventory_id, limit)
        a.ping()
        a.launch()
        a.poll()
        a.summary()


class AWXAction(Action):
    def run(self, tower_host, tower_oauth_token, job_template_id, inventory_id, limit):
        logging.basicConfig(level=logging.INFO)
        awx = AWXAction()
        awx.run(
            tower_host=tower_host,
            tower_oauth_token=tower_oauth_token,
            job_template_id=job_template_id,
            inventory_id=inventory_id,
            limit=limit,
        )
