from datetime import datetime
from run_count_lock import RunCountLock
from st2reactor.sensor.base import PollingSensor


class DailyRunSensor(PollingSensor):
    def __init__(self, sensor_service, config, poll_interval=60):
        super(DailyRunSensor, self).__init__(
            sensor_service=sensor_service, config=config, poll_interval=poll_interval
        )
        self._trigger_ref = "test.daily_run"

    def setup(self):
        self.rcl = RunCountLock(
            lock_path=f"/tmp/test_daily_run/{datetime.today().strftime('%Y-%m-%d')}"
        )

    def poll(self):
        self.rcl.increment()
        payload = {
            "foo": "bar",
            "count": self.rcl.count(),
        }
        if self.rcl.count() < 10:
            payload = {
                "count": self.rcl.count(),
                "dispatch": True,
            }
        else:
            payload = {
                "count": self.rcl.count(),
                "dispatch": False,
            }
        if self.rcl.count() < 10:
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
