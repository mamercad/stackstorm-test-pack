from random import randint
from st2reactor.sensor.base import PollingSensor


class YumSensor(PollingSensor):

    def __init__(self):
        self._poll_interval = 60

    def poll(self):
        payload = {
            "host1": randint(0,10),
            "host2": randint(0,10),
            "host3": randint(0,10),
            "host4": randint(0,10),
            "host5": randint(0,10),
        }
        self.sensor_service.dispatch(trigger=self._trigger_ref, payload=payload)
