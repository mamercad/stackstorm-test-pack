import statsd
import time


class StatsDClient:
    def __init__(self, host="localhost", port=9125):
        self.client = statsd.StatsClient(host=host, port=port)
        self.start = time.time()

    def incr(self, counter="foo"):
        self.client.incr(counter)

    def gauge(self, stat="foo", value=1, delta=True):
        self.client.gauge(stat=stat, value=value, delta=delta)

    def timing(self, stat="foo", delta=None):
        # You must convert to milliseconds:
        if not delta:
            delta = int((time.time() - self.start) * 1000)
        else:
            delta = delta * 1000
        self.client.timing(stat=stat, delta=delta)
