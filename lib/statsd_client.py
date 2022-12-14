import statsd

class StatsDClient:
    def __init__(self, host="localhost", port=9125):
        self.client = statsd.StatsClient(host=host, port=port)

    def incr(self, counter="foo"):
        self.client.incr(counter)
