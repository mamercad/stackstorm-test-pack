import statsd

class StatsDClient:
    def __init__(self):
        self.client = statsd.StatsClient('localhost', 9125)

    def emit(self):
        self.client.incr('foo')
