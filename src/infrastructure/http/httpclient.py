import httpx

from src.domain.entities.monitor import Monitor


class HttpClient:
    def __init__(self, monitor: Monitor):
        self._monitor = monitor

    def request(self):
        return httpx.request(
            method=self._monitor.method,
            url=self._monitor.url,
            timeout=self._monitor.timeout,
        )
