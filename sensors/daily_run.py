from st2reactor.sensor.base import PollingSensor


class DailyRunSensor(PollingSensor):
    def __init__(self, sensor_service, config, poll_interval=60):
        super(DailyRunSensor, self).__init__(
            sensor_service=sensor_service, config=config, poll_interval=poll_interval
        )
        self._trigger_ref = "test.daily_run"

    def setup(self):
        pass

    def poll(self):
        payload = {}
        self.sensor_service.dispatch(trigger=self._trigger_ref, payload=payload)

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
