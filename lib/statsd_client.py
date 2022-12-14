import statsd
import time
from datetime import datetime

class StatsDClient:
    def __init__(self, host="localhost", port=9125):
        self.client = statsd.StatsClient(host=host, port=port)
        self.start = time.time()

    def incr(self, counter="foo"):
        self.client.incr(counter)

    def gauge(self, stat="foo", value=0, delta=True):
        self.client.gauge(stat=stat, value=value)

    def timing(self, stat="foo"):
        # You must convert to milliseconds:
        dt = int((time.time() - self.start) * 1000)
        self.client.timing(stat=stat, delta=dt)
