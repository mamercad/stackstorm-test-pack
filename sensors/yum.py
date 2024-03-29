from random import randint
from st2reactor.sensor.base import PollingSensor


class YumSensor(PollingSensor):
    def __init__(self, sensor_service, config, poll_interval=60):
        super(YumSensor, self).__init__(
            sensor_service=sensor_service, config=config, poll_interval=poll_interval
    )

    def setup(self):
        pass

    def poll(self):
        payload = {
            "host1": randint(0,10),
            "host2": randint(0,10),
            "host3": randint(0,10),
            "host4": randint(0,10),
            "host5": randint(0,10),
        }
        self._sensor_service.dispatch(trigger="test.yum", payload=payload)

    def cleanup(self):
        # This is called when the st2 system goes down. You can perform cleanup operations like
        # closing the connections to external system here.
        pass

    def add_trigger(self, trigger):
        # This method is called when trigger is created
        pass

    def update_trigger(self, trigger):
        # This method is called when trigger is updated
        pass

    def remove_trigger(self, trigger):
        # This method is called when trigger is deleted
        pass
